from pydantic import BaseModel, Field
from typing import Literal, Optional
from app.domain.enums import MLModelType

class PredictRequest(BaseModel):
    model_type: MLModelType = Field(..., example="speech_to_text")
    data: str = Field(..., example="Потратил 300 рублей на обед")  # base64-encoded аудио или текст

    class Config:
        use_enum_values = True
        schema_extra = {
            "example": {
                "model_type": "text_parser",
                "data": "Потратил 300 рублей на обед"
            }
        }


class PredictResponse(BaseModel):
    result: dict
    model_used: MLModelType
    comment: Optional[str] = None