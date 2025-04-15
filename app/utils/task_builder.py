from sqlalchemy.orm import Session
from app.domain.ml_factory import MLModelFactory
from app.domain.user import User as DomainUser
from app.domain.entry import Entry as DomainEntry
from app.domain.ml_request_task import MLRequestTask
from app.infra.database.crud.user_crud import get_user_by_id
from app.infra.database.crud.entry_crud import get_entry


def build_ml_task_from_dict(task_data: dict, db: Session) -> MLRequestTask:
    user_orm = get_user_by_id(db, task_data["user_id"])
    entry_orm = get_entry(db, task_data["entry_id"])
    model = MLModelFactory.get_model(task_data["model_type"])

    # user = DomainUser(
    #     user_id=user_orm.id,
    #     username=user_orm.username,
    #     email=user_orm.email,
    #     password_hash=user_orm.password_hash,
    #     role=user_orm.role
    # )
    # entry = DomainEntry(
    #     entry_id=entry_orm.id,
    #     user = user,
    #     input_type=entry_orm.input_type,
    #     data=entry_orm.data,
    # )

    return MLRequestTask(
        task_id=entry_orm.id,
        user=user_orm,
        entry=entry_orm,
        model=model
    )
