from fastapi import APIRouter
from app.schemas.jwt_schema import Token
from app.dependencies.oauth2 import oauth2_password_request_form_dependency
import app.services.auth_service as auth_service
from app.dependencies.db import db_dependency

router = APIRouter(tags=["Authentication"])

@router.post("/token")
async def login_for_access_token(form_data: oauth2_password_request_form_dependency, 
    db:db_dependency) -> Token:
    return auth_service.login_for_access_token(form_data, db)