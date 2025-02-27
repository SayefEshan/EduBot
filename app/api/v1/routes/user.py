from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserResponse
import app.services.user_service as user_service
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
async def create_user(user: UserCreate, db: Session=Depends(get_db)):
    return user_service.create_user(user, db)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return user_service.get_user(user_id)