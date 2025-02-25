from sqlmodel import Field, SQLModel, create_engine


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str
    password: str
    username: str
    age: int | None = None