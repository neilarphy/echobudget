from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class EntryOut(BaseModel):
    id: int
    input_type: str
    data: str
    status: str

    model_config = dict(from_attributes=True)


class ParsedEntryOut(BaseModel):
    id: int
    entry_id: int
    user_id: int
    amount: float
    category: str
    comment: Optional[str]
    model_name: str
    created_at: Optional[datetime]

    model_config = dict(from_attributes=True)


class PredictionHistoryItem(BaseModel):
    entry: EntryOut
    parsed: Optional[ParsedEntryOut] = None

class PredictionHistoryResponse(BaseModel):
    history: list[PredictionHistoryItem]
