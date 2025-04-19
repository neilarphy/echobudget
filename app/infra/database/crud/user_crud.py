from sqlalchemy.orm import Session
from app.infra.database.models.users import UserORM
from app.domain.enums import UserRole


def create_user(
        db: Session, 
        username: str,
        email: str, 
        password_hash: str, 
        role: str = UserRole.USER.value
    ) -> UserORM:
    user = UserORM(
        username=username,
        email=email,
        password_hash=password_hash,
        role=role,
        balance=0
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_id(db: Session, user_id: int) -> UserORM | None:
    return db.query(UserORM).filter_by(id=user_id).first()


def get_user_by_username(db: Session, username: str) -> UserORM | None:
    return db.query(UserORM).filter_by(username=username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(UserORM).filter_by(email=email).first()


def list_users(db: Session) -> list[UserORM]:
    return db.query(UserORM).all()


def delete_user(db: Session, user_id: int) -> bool:
    user = get_user_by_id(db, user_id)
    if user:
        db.delete(user)
        db.commit()
        return True
    return False
