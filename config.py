from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # attribute mentioned here must be present in .env as well
    app_name: str
    db_host:str
    db_name:str
    db_secret:str
    db_port:int|str
    
    model_config = SettingsConfigDict(env_file=".env") # reads .env file

settings = Settings()