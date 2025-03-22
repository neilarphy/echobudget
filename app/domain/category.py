from typing import Optional
from app.domain.user import User
from app.domain.enums import TransactionCategory

class Category:
    def __init__(
            self, 
            category_id: int, 
            name: str, 
            user: Optional[User] = None, 
            base_type: Optional[TransactionCategory] = None
        ):
        self.__category_id = category_id
        self.__name = name
        self.__user = user
        self.__base_type = base_type

    def is_user_defined(self) -> bool:
        return self.__user is not None

    def get_name(self) -> str:
        return self.__name

    def get_owner(self) -> Optional[User]:
        return self.__user

    def get_base_type(self) -> Optional[TransactionCategory]:
        return self.__base_type