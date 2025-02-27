import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

# Manually load .env file
load_dotenv(override=True)

class Settings(BaseSettings):
    # attribute mentioned here must be present in .env as well
    app_name: str
    db_name:str
    db_host:str
    db_port:int=5432
    db_user:str
    db_password:str
    
    model_config = SettingsConfigDict(env_file=".env") # reads .env file

settings = Settings()