from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class Quiz(Base):
    __tablename__ = "quizes"

    id: Mapped[int] = mapped_column(primary_key=True)
    ai_token: Mapped[str]
    quiz_category_id: Mapped[int]
    title: Mapped[Optional[str]]
    title_limit: Mapped[Optional[datetime]]
    question_count: Mapped[int]

    # relationship
    category: Mapped["QuizCategory"] = relationship("QuizCategory", back_populates="quizes")