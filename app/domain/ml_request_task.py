from app.domain.enums import TaskStatus
from app.domain.user import User
from app.domain.entry import Entry
from app.domain.ml_model import MLModel
from app.domain.parsed_entry import ParsedEntry

class MLRequestTask:
    def __init__(
            self, 
            task_id: int, 
            user: User, 
            entry: Entry, 
            model: MLModel
    ):
        self.__task_id = task_id
        self.__user = user
        self.__entry = entry
        self.__model = model
        self.__status = TaskStatus.QUEUED
        self.__result = None

    def mark_processing(self):
        self.__status = TaskStatus.PROCESSING

    def mark_done(self, result: ParsedEntry):
        self.__status = TaskStatus.DONE
        self.__result = result

    def mark_failed(self):
        self.__status = TaskStatus.FAILED

    def get_model(self) -> MLModel:
        return self.__model

    def get_status(self) -> TaskStatus:
        return self.__status

    def get_entry(self) -> Entry:
        return self.__entry

    def get_user(self) -> User:
        return self.__user

    def get_result(self) -> ParsedEntry:
        return self.__result