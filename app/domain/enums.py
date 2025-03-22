from enum import Enum

class InputType(Enum):
    VOICE = "voice"
    Text = "text"

class EntryStatus(Enum):
    CREATED = "created"
    PROCESSING  = "processing"
    PROCESSED = "processed"
    FAULTED = "faulted"

class UserRole(Enum):
    USER = "user"
    ADMIN = "admin"

class TaskStatus(Enum):
    QUEUED = "queued"
    PROCESSING = "processing"
    DONE = "done"
    FAILED = "failed"

class TransactionType(Enum):
    CREDIT = "пополнение"
    DEBIT = "списание"

class TransactionSource(Enum):
    TOPUP = "topup"
    INFERENCE = "inference"

class TransactionCategory(Enum):
    FOOD = "еда"
    TRANSPORT = "транспорт"
    HEALTH = "здоровье"
    ENTERTAINMENT = "развлечения"
    BILLS = "коммуналка"
    OTHER = "другое"

class MLModelType(Enum):
    TRANSACTION_CLASSIFIER = "transaction_classifier"
    SPEECH_TO_TEXT = "speech_to_text"

