from app.infra.database.crud.entry_crud import (
    get_entry,
    update_entry_status,
)
from app.infra.services.balance_manager import BalanceManagerORM
from app.infra.database.crud.user_crud import get_user_by_id
from app.infra.database.crud.parsedentry_crud import create_parsed_entry
from app.domain.enums import EntryStatus, InputType
from app.domain.ml_factory import MLModelFactory
from app.domain.ml_model import SpeechToTextParser, EntryClassifier
from app.infra.services.minio_service import download_file
from app.domain.ml_request_task import MLRequestTask
from app.utils.logger import get_logger
from sqlalchemy.orm import Session

logger = get_logger(__name__)

class EntryProcessor:
    def __init__(
            self,
            db: Session,
    ):
        self.db = db
    
    def process(
            self, 
            ml_task: MLRequestTask
    ):
        entry = ml_task.get_entry()
        user = ml_task.get_user()
        model = ml_task.get_model()

        entry_input_type = entry.input_type
        entry_data = entry.data
        entry_id = entry.id

        user_id = user.id

        update_entry_status(self.db, entry_id, EntryStatus.PROCESSING)
        ml_task.mark_processing()
        logger.info(f"Entry #{entry_id} marked as PROCESSING")

        bm = BalanceManagerORM(self.db, user)
        success, log = bm.deduct_balance(model.get_cost())

        if not success:
            raise ValueError("Недостаточно средств")        

        try:
            if entry_input_type == "text":
                if not isinstance(model, EntryClassifier):
                    logger.warning(f"Заменяем модель {model.get_name()} на entry_classifier")
                    model = MLModelFactory.get_model("entry_classifier")

                result = model.predict(entry_data)
            
            elif entry_input_type == "voice":
                audio_bytes = download_file(entry_data)
                if not isinstance(model, SpeechToTextParser):
                    logger.warning(f"Заменяем модель {model.get_name()} на speech_to_text")
                    model = MLModelFactory.get_model("speech_to_text")

                transcription_result = model.predict(audio_bytes)
                text = transcription_result["text"]

                classifier = MLModelFactory.get_model("entry_classifier")
                result = classifier.predict(text)
            else:
                raise ValueError(f"Unknown input_type: {entry.input_type}")

            parsed = create_parsed_entry(
                db=self.db,
                entry_id=entry_id,
                user_id=user_id,
                amount=result["amount"],
                category=result["category"],
                comment=result["comment"],
                model_name=model.get_name()
            )

            update_entry_status(
                self.db,
                entry_id=entry_id,
                new_status=EntryStatus.PROCESSED,
            )
            ml_task.mark_done(parsed)
            logger.info(f"Entry #{entry_id} processed successfully")
            self.db.commit()
        except Exception as e:
            ml_task.mark_failed()
            logger.error(f"Failed to process entry #{entry_id}: {e}")
            update_entry_status(self.db, entry_id, EntryStatus.FAULTED,error_reason=str(e))




