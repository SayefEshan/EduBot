from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

oauth2_dependency = Annotated[str, Depends(oauth2_scheme)]

oauth2_password_request_form_dependency = Annotated[OAuth2PasswordRequestForm, Depends()]