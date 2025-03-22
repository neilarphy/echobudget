from datetime import datetime
from app.domain.user import User
from app.domain.entry import Entry
from app.domain.category import Category

class ParsedEntry:
    def __init__(
        self,
        trans_id: int,
        entry: Entry,
        user: User,
        amount: float,
        category: Category,
        comment: str,
        model_name: str,
        created_at: datetime = None
    ):
        self.__trans_id = trans_id
        self.__entry = entry
        self.__user = user
        self.__amount = amount
        self.__category = category
        self.__comment = comment
        self.__model_name = model_name
        self.__created_at = created_at or datetime.now()

    def get_category(self) -> Category:
        return self.__category

    def get_summary(self) -> str:
        return f"{self.__amount} ₽ на '{self.__category}' ({self.__comment})"

    def get_amount(self) -> float:
        return self.__amount

    def get_created_at(self) -> datetime:
        return self.__created_at

    def get_summary(self) -> str:
        return f"{self.__amount} ₽ на '{self.__category}' ({self.__comment})"