from pydantic import BaseModel, Field
from app.domain.enums import TransactionType, TransactionSource

class BalanceUpdateRequest(BaseModel):
    amount: int = Field(..., gt=0, example=100)
    source: TransactionSource = Field(..., example=TransactionSource.TOPUP)

    class Config:
        use_enum_values = True

class BalanceResponse(BaseModel):
    balance: int = Field(..., example=500)


class TransactionLogOut(BaseModel):
    id: int
    amount: int
    type: TransactionType
    source: TransactionSource

    class Config:
        orm_mode = True
        use_enum_values = True