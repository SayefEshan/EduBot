from datetime import datetime
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from .quiz import Quiz
from .question_option import QuestionOption


class Question(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    quiz_id: Mapped[int] = mapped_column(
        ForeignKey("quizes.id"), nullable=False)
    question_text: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[Optional[datetime]] = mapped_column(default=None)
    updated_at: Mapped[Optional[datetime]] = mapped_column(default=None)

    # relationship
    quiz: Mapped["Quiz"] = relationship("Quiz", back_populates="questions")
    question_options: Mapped[list["QuestionOption"]] = relationship(
        "QuestionOption", back_populates="question")
