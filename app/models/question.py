from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class Question(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    quiz_id: Mapped[int] = mapped_column(foreign_key="quizes.id", nullable=False)
    question_text: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[Optional[datetime]]
    updated_at: Mapped[Optional[datetime]]

    # relationship
    quiz: Mapped["Quiz"] = relationship("Quiz", back_populates="questions")
    question_options: Mapped[list["QuestionOption"]] = relationship("QuestionOption", back_populates="question")