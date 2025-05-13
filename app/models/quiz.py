from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.question import Question
from app.models.quiz_category import QuizCategory
from app.models.user_quiz_history import UserQuizHistory
from .base import Base


class Quiz(Base):
    __tablename__ = "quizes"

    id: Mapped[int] = mapped_column(primary_key=True)
    ai_token: Mapped[str]
    quiz_category_id: Mapped[int]
    title: Mapped[Optional[str]]
    title_limit: Mapped[Optional[datetime]]
    question_count: Mapped[int]
    created_at: Mapped[Optional[datetime]]
    updated_at: Mapped[Optional[datetime]]

    # relationship
    category: Mapped["QuizCategory"] = relationship(
        "QuizCategory", back_populates="quizes")
    questions: Mapped[list["Question"]] = relationship(
        "Question", back_populates="quiz")
    user_quiz_history: Mapped[list["UserQuizHistory"]] = relationship(
        "UserQuizHistory", back_populates="quiz")
