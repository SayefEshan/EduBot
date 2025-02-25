from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "EDU BOT"
    admin_email: str
    model_config = SettingsConfigDict(env_file=".env") # reads .env file

settings = Settings()