from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.infra.database.session import get_db
from app.infra.database.crud.user_crud import get_user_by_username
from app.schemas.sch_predict import PredictRequest, PredictResponse
from app.domain.ml_factory import MLModelFactory
from app.infra.services.balance_manager import BalanceManagerORM
from app.domain.enums import TransactionSource

router = APIRouter()

# Временно мок-юзер
def get_mock_user(db: Session = Depends(get_db)):
    user = get_user_by_username(db, "user")
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=PredictResponse)
def make_prediction(
    request: PredictRequest, 
    db: Session = Depends(get_db),
    user=Depends(get_mock_user)
):
    try:
        model = MLModelFactory.get_model(request.model_type)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    bm = BalanceManagerORM(db=db, user=user)
    success, _ = bm.deduct_balance(amount=model.get_cost(), source=TransactionSource.INFERENCE)
    if not success:
        raise HTTPException(status_code=403, detail="Недостаточно средств для проведение предсказания")
    
    try:
        result = model.predict(request.data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")

    db.commit()
    
    return PredictResponse(
        result=result,
        model_used=request.model_type,
        comment="Предсказание выполнено успешно"
    )
