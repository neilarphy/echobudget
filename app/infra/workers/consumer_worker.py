import json
from app.infra.workers.base_consumer import BaseRabbitConsumer
from app.utils.task_builder import build_ml_task_from_dict
from app.infra.workers.entry_processor import EntryProcessor
from app.infra.database.session import SessionLocal
from app.utils.logger import get_logger

logger = get_logger(__name__)

class EntryTaskConsumer(BaseRabbitConsumer):
    def callback(
            self,
            ch,
            method,
            properties,
            body,
    ):
        logger.info("Message received, starting processing...")

        task_data = json.loads(body)
        logger.debug(f"Parsed message: {task_data}")

        db = SessionLocal()
        try:
            ml_task = build_ml_task_from_dict(task_data, db)
            processor = EntryProcessor(db=db)
            processor.process(ml_task)
        except Exception as e:
            logger.exception(f"Failed to process task: {e}")
            raise 
        finally:
            db.close()

def start_worker():
    consumer = EntryTaskConsumer()
    consumer.start_consuming()