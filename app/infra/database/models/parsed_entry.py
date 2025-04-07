from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.infra.database.base import Base


class ParsedEntryORM(Base):
    __tablename__ = "parsed_entries"

    id = Column(Integer, primary_key=True, index=True)
    entry_id = Column(Integer, ForeignKey("entries.id"), nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    amount = Column(Float, nullable=False)
    category = Column(String(50), nullable=False)
    comment = Column(String(255), nullable=True)
    model_name = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    entry = relationship("EntryORM", back_populates="parsed_entry")
    user = relationship("UserORM", back_populates="parsed_entries")

    def __repr__(self):
        return f"<ParsedEntryORM(id={self.id}, user_id={self.user_id}, category={self.category}, amount={self.amount})>"
