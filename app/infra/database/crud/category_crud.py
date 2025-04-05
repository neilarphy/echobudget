from sqlalchemy.orm import Session
from app.infra.database.models.category import CategoryORM


def create_category(
    db: Session,
    name: str,
    user_id: int | None = None,
    is_system: bool = False
) -> CategoryORM:
    category = CategoryORM(
        name=name,
        user_id=user_id,
        is_system=is_system
    )
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def get_user_categories(
    db: Session,
    user_id: int
) -> list[CategoryORM]:
    return db.query(CategoryORM).filter(CategoryORM.user_id == user_id).all()


def get_system_categories(
    db: Session
) -> list[CategoryORM]:
    return db.query(CategoryORM).filter(CategoryORM.is_system == True).all()


def get_category_by_id(
    db: Session,
    category_id: int
) -> CategoryORM | None:
    return db.query(CategoryORM).filter(CategoryORM.id == category_id).first()


def delete_category(
    db: Session,
    category_id: int
) -> bool:
    category = db.query(CategoryORM).filter(CategoryORM.id == category_id).first()
    if category:
        db.delete(category)
        db.commit()
        return True
    return False
