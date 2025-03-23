from app.domain.ml_model import MLModel, EntryClassifier, SpeechToTextParser
from app.domain.enums import MLModelType

class MLModelFactory:
    @staticmethod
    def get_model(model_type: str) -> MLModel:
        if model_type == MLModelType.ENTRY_CLASSIFIER.value:
            return EntryClassifier("entry_classifier", cost=1)
        if model_type == MLModelType.SPEECH_TO_TEXT.value:
            return SpeechToTextParser("speech_to_text", cost=2)
        raise ValueError(f"Unknown model type: {model_type}")
