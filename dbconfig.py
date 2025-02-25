from sqlmodel import SQLModel, create_engine
from . import models
from config import settings

db_host = settings.DB_HOST
db_name = settings.DB_NAME

engine = create_engine(db_host, echo=True)