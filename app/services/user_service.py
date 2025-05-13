from fastapi import HTTPException, status
from app.models.user import User
from app.schemas.jwt_schema import TokenData
from app.schemas.user_schema import UserCreate
from sqlalchemy.orm import Session
from app.dependencies.oauth2 import oauth2_dependency
import jwt
from jwt.exceptions import InvalidTokenError
from app.services import jwt_service
from app.utils.security import hash_password


def create_user(user: UserCreate, db: Session):

    user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(user_id: int, db: Session):
    pass


async def get_current_user(token: oauth2_dependency):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, jwt_service.SECRET_KEY,
                             algorithms=[jwt_service.ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception

    user = get_user(1, username=token_data.username)

    if user is None:
        raise credentials_exception
    return user
