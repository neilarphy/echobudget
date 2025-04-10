from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.infra.database.session import get_db
from app.infra.database.crud.user_crud import get_user_by_username
from app.infra.services.balance_manager import BalanceManagerORM
from app.schemas.sch_balance import BalanceUpdateRequest, BalanceResponse
from app.domain.enums import TransactionSource

router = APIRouter()


# Мок-пользователь, пока нет настоящей авторизации
def get_mock_user(
        db: Session = Depends(get_db)
):
    user = get_user_by_username(db, "user")
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/", response_model=BalanceResponse)
def get_balance(
    user=Depends(get_mock_user), 
    db: Session = Depends(get_db)
):
    bm = BalanceManagerORM(db=db, user=user)
    return {"balance": bm.get_balance()}


@router.post("/topup", response_model=BalanceResponse)
def top_up_balance(
    data: BalanceUpdateRequest,
    user=Depends(get_mock_user),
    db: Session = Depends(get_db)
):
    bm = BalanceManagerORM(db=db, user=user)
    bm.add_balance(amount=data.amount, source=data.source)
    db.commit()
    return {"balance": bm.get_balance()}
