from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user,get_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate):
    return create_user(user)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return get_user(user_id)