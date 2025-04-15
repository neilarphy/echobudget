from app.infra.database.base import Base
from app.infra.database.session import engine, SessionLocal
from app.domain.enums import (
    UserRole, 
    TransactionSource, 
    TransactionType,
    InputType,
    EntryStatus,
    )
from app.infra.database.crud.user_crud import create_user, get_user_by_username
from app.infra.database.crud.category_crud import create_category
from app.infra.database.crud.entry_crud import create_entry
from app.infra.database.crud.parsedentry_crud import create_parsed_entry
from app.infra.services.balance_manager import BalanceManagerORM
from app.domain.auth import AuthService

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Таблицы созданы")


def seed_demo_data():
    session = SessionLocal()

    try:
        if not get_user_by_username(session, "user"):
            user = create_user(
                db=session,
                username="user",
                email="user@example.com",
                password_hash=AuthService.hash_password("123"),
                role=UserRole.USER.value
            )
        else:
            user = get_user_by_username(session, "user")

        if not get_user_by_username(session, "admin"):
            admin = create_user(
                db=session,
                username="admin",
                email="admin@example.com",
                password_hash=AuthService.hash_password("123"),
                role=UserRole.ADMIN.value
            )
        else:
            admin = get_user_by_username(session, "admin")

        user_bm = BalanceManagerORM(db=session, user=user)
        user_bm.add_balance(amount=100)

        admin_bm = BalanceManagerORM(db=session, user=admin)
        admin_bm.add_balance(amount=999)

        base_categories = ["food", "transport", "entertainment", "health", "education"]
        for cat in base_categories:
            create_category(db=session, name=cat, is_system=True)

        entry = create_entry(
            db=session,
            user_id=user.id,
            input_type=InputType.TEXT,
            data="Купил обед за 300 рублей",
            status=EntryStatus.PROCESSED
        )

        create_parsed_entry(
            db=session,
            entry_id=entry.id,
            user_id=user.id,
            amount=300.0,
            category="food",
            comment="обед",
            model_name="entry_classifier"
        )

        session.commit()
        print("Демо данные добавлены")

    except Exception as e:
        session.rollback()
        print(f"Ошибка при добавлении данных: {e}")

    finally:
        session.close()


if __name__ == "__main__":
    create_tables()
    seed_demo_data()
