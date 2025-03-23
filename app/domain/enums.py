from enum import Enum

class InputType(Enum):
    VOICE = "voice"
    TEXT = "text"

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
    CREDIT = "credit"
    DEBIT = "debit"

class TransactionSource(Enum):
    TOPUP = "topup"
    INFERENCE = "inference"

class TransactionCategory(Enum):
    FOOD = "food"
    TRANSPORT = "transport"
    HEALTH = "health"
    ENTERTAINMENT = "entertainment"
    BILLS = "bills"
    OTHER = "other"

class MLModelType(Enum):
    ENTRY_CLASSIFIER = "entry_classifier"
    SPEECH_TO_TEXT = "speech_to_text"

