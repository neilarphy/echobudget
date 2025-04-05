from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.infra.database.base import Base
from app.domain.enums import TransactionType, TransactionSource

class TransactionLogORM(Base):
    __tablename__ = "transaction_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Integer, nullable=False)
    type = Column(String(50), nullable=False, default=TransactionType.CREDIT.value)
    source = Column(String(50), nullable=False, default=TransactionSource.TOPUP.value)

    user = relationship("UserORM", back_populates="transactions")

    def __repr__(self):
        return f"<TransactionLogORM(id={self.id}, user_id={self.user_id}, amount={self.amount}, type={self.type}, source={self.source})>"