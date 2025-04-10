from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.infra.database.base import Base
from app.domain.enums import UserRole
from app.infra.database.models.category import CategoryORM
from app.infra.database.models.entries import EntryORM
from app.infra.database.models.parsed_entry import ParsedEntryORM
from app.infra.database.models.transactionlog import TransactionLogORM

class UserORM(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(30), default=UserRole.USER.value)
    balance = Column(Integer, default=0)

    transactions = relationship("TransactionLogORM", back_populates="user")
    entries = relationship("EntryORM", back_populates="user")
    parsed_entries = relationship("ParsedEntryORM", back_populates="user")
    categories = relationship("CategoryORM", back_populates="user")


    def get_role_enum(self) -> UserRole:
        return UserRole(self.role)

    def is_admin(self) -> bool:
        return self.get_role_enum() == UserRole.ADMIN

    def __repr__(self):
        return f"<UserORM(id={self.id}, username='{self.username}', email='{self.email}', role='{self.role}')>"
