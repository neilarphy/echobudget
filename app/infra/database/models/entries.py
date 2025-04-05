from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.infra.database.base import Base
from app.domain.enums import InputType, EntryStatus


class EntryORM(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    input_type = Column(String(20), nullable=False, default=InputType.TEXT.value)
    data = Column(String, nullable=False)
    status = Column(String(20), nullable=False, default=EntryStatus.CREATED.value)
    error_reason = Column(String, nullable=True)

    user = relationship("UserORM", back_populates="entries")
    parsed_entry = relationship("ParsedEntryORM", back_populates="entry", uselist=False)

    def __repr__(self):
        return f"<EntryORM(id={self.id}, user_id={self.user_id}, type={self.input_type}, status={self.status})>"
