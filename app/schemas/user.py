from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# Schema for creating a new user
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Schema for returning user data (response model)
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True  # Allows ORM model to work with Pydantic

# Schema for updating a user (optional fields)
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None