from fastapi import FastAPI
from database import engine
from config import settings
from app.models.base import Base

from app.api.v1.routes import auth_router, users_router

#connects to DB and create tables
Base.metadata.create_all(engine)

app = FastAPI()

# Register routers
app.include_router(auth_router.router)
app.include_router(users_router.router)

@app.get("/")
async def home():
    return {"message": f"Welcome to the {settings.app_name} API!"}