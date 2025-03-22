from abc import ABC, abstractmethod


class MLModel(ABC):
    def __init__(
            self, 
            model_name: str,
            cost: int
        ):
        self.__model_name=model_name
        self.__cost=cost
    
    @abstractmethod
    def predict(self, text: str) -> dict:
        pass

    def get_cost(self) -> int:
        return self._cost

    def get_name(self) -> str:
        return self._model_name
    

class EntryClassifier(MLModel):
    def predict(self, text: str) -> dict:
        return {#пример
            "amount": 250.0,
            "category": "еда",
            "comment": "кофе в Старбаксе"
        }

class SpeechToTextParser(MLModel):
    def predict(self, audio_path: str) -> dict:
        return {#пример
            "text": "Купил кофе за 250 рублей"
        }