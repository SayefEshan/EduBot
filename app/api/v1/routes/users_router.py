from fastapi import APIRouter
from app.schemas.user_schema import UserCreate, UserResponse
import app.services.user_service as user_service
from app.dependencies.oauth2 import oauth2_dependency
from app.dependencies.user import get_current_user_dependency
from app.dependencies.db import db_dependency

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
async def create_user(user: UserCreate, db: db_dependency):
    return user_service.create_user(user, db)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, token:oauth2_dependency):
    return user_service.get_user(user_id)

@router.get("/me", response_model=UserResponse)
def get_current_user(current_user:get_current_user_dependency):
    return current_user