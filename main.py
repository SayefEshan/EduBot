from typing import Union
from fastapi import FastAPI
from dbconfig import SQLModel, engine
from config import settings

from app.api.v1.routes import user

SQLModel.metadata.create_all(engine) #connect to DB and create tables

app = FastAPI()

# Register routers
app.include_router(user.router)

@app.get("/")
async def home():
    return {"message": f"Welcome to the {settings.app_name} API!"}