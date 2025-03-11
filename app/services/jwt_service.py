from datetime import datetime, timedelta, timezone
import jwt
from jwt.exceptions import InvalidTokenError

SECRET_KEY = "a749137f4528c2976b06127b68006fd4e8c1a6a9ece4e04d27d4fff4c8db9fba"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta | None = None)->str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
