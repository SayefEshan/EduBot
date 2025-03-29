from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class UserQuizHistory(Base):
    __tablename__ = "user_quiz_history"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    quiz_id: Mapped[int] = mapped_column(ForeignKey("quizes.id"), nullable=False)
    satus: Mapped[str]
    mark: Mapped[int]
    created_at: Mapped[Optional[datetime]]
    updated_at: Mapped[Optional[datetime]]

    # relationship
    user: Mapped["User"] = relationship("User", back_populates="user_quiz_history")
    quiz: Mapped["Quiz"] = relationship("Quiz", back_populates="user_quiz_history")