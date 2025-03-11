from datetime import timedelta
from fastapi import status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from app.models.user import User
from app.schemas.jwt_schema import Token
from app.schemas.user_schema import UserResponse
from app.services import jwt_service
from sqlalchemy.orm import Session
from app.utils.security import verify_password

def authenticate_user(db:Session, username: str, password: str)->UserResponse|None:
    stmt = select(User).where(User.username == username)
    user = db.execute(stmt).scalars().first()

    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    
    # Convert pydantic object to dictionary
    return UserResponse.model_validate(user).model_dump()

def login_for_access_token(form_data:OAuth2PasswordRequestForm, db:Session)->Token:
    user = authenticate_user(db, form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=jwt_service.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwt_service.create_access_token(
        data={"sub": user}, expires_delta=access_token_expires
    )

    return Token(access_token=access_token, token_type="bearer")
