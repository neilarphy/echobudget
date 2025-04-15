from fastapi import APIRouter

from app.infra.api import (
    auth,
    balance,
    history,
    predict,
    entry,
)

router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["Auth"])
router.include_router(balance.router, prefix="/balance", tags=["Balance"])
router.include_router(history.router, prefix="/history", tags=["History"])
router.include_router(predict.router, prefix="/predict", tags=["Prediction"])
router.include_router(entry.router, prefix="/entry", tags=["Upload"])