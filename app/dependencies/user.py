from typing import Annotated
from fastapi import Depends
from .oauth2 import oauth2_dependency
from app.schemas.user_schema import UserResponse

async def get_current_user(token: oauth2_dependency):
    return UserResponse

get_current_user_dependency = Annotated[UserResponse, Depends(get_current_user)]