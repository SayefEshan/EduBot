from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings

db_url = f"postgresql://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"

engine = create_engine(db_url, echo=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    try:
        db = SessionLocal()
        print("connected to db!")
        yield db
    except Exception as e:
        raise e
    finally:
        db.close()
        print("db connection closed!")
        
get_db()