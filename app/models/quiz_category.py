from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class QuizCategory(Base):
    __tablename__ = "quiz_categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    # relationship
    quizes: Mapped[list["Quiz"]] = relationship("Quiz", back_populates="category")