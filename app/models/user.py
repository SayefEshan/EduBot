from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    password: Mapped[str]
    first_name: Mapped[Optional[str]]
    last_name: Mapped[Optional[str]]
    username: Mapped[str]
    mobile: Mapped[Optional[int]]
    created_at: Mapped[Optional[datetime]]
    updated_at: Mapped[Optional[datetime]]