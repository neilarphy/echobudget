from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.infra.database.base import Base


class CategoryORM(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    is_system = Column(Boolean, default=False)

    user = relationship("UserORM", back_populates="categories")

    def __repr__(self):
        owner = "system" if self.user_id is None else f"user_id={self.user_id}"
        return f"<CategoryORM(id={self.id}, name='{self.name}', {owner})>"
