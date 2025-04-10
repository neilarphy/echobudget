from fastapi import APIRouter, HTTPException, status
from app.schemas.sch_auth import (
    RegisterRequest, 
    LoginRequest, 
    AuthResponse,
)
from app.domain.auth import AuthService
from app.infra.database.session import SessionLocal
from app.infra.database.crud.user_crud import (
     create_user, 
     get_user_by_username,
)

router = APIRouter()

@router.post("/register", response_model=AuthResponse)
def register_user(data: RegisterRequest):
    db = SessionLocal()
    try:
        existing_user = get_user_by_username(db, data.username)
        if existing_user:
            raise HTTPException(status_code=400, detail="Пользователь с таким username уже существует")
        
        hashed_password = AuthService.hash_password(data.password)
        user = create_user(
            db=db,
            username=data.username,
            email=data.email,
            password_hash=hashed_password,
            role="user"
        )

        return AuthResponse(
            id=user.id,
            username=user.username,
            email=user.email,
            token="mock-token"
        )
    finally:
        db.close()

@router.post("/login", response_model=AuthResponse)
def login_user(data: LoginRequest):
    db = SessionLocal()
    try:
        user = get_user_by_username(db, data.username)
        if not user or not AuthService.verify_password(data.password):
            raise HTTPException(status_code=401, detail="Неверный пароль или юзера не существует")
        
        return AuthResponse(
            id=user.id,
            username=user.username,
            emai=user.email,
            token="mock-token"
        )

    finally:
        db.close()