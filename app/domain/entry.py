from app.domain.enums import InputType, EntryStatus
from app.domain.user  import User

class Entry:
    def __init__(
            self, 
            entry_id: int, 
            user: User, 
            input_type: InputType, 
            data: str
    ):
        self.__entry_id = entry_id
        self.__user = user
        self.__input_type = input_type
        self.__data = data
        self.__status = EntryStatus.CREATED
        self.__error_reason = None

    def mark_processing(self):
        self.__status = EntryStatus.PROCESSING

    def mark_done(self):
        self.__status = EntryStatus.PROCESSED

    def mark_error(self, reason: str):
        self.__status = EntryStatus.FAULTED
        self.__error_reason = reason

    def get_data(self) -> str:
        return self.__data
    
    def get_user(self) -> User:
        return self.__user
    
    def get_status(self) -> EntryStatus:
        return self.__status
    
    def get_id(self) -> int:
        return self.__entry_id