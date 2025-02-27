from app.models.user import User
from app.schemas.user import UserCreate
from sqlalchemy.orm import Session


def create_user(user: UserCreate, db: Session):
    user = User(
        username="muttakin",
        email="muttakin@gmail.com",
        password="1234",
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(user_id: int):
    pass