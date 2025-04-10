from sqlmodel import create_engine, SQLModel, Session
import os
from dotenv import load_dotenv

from models import MarkValue, User, Group, Subject, Schedule, Homework, Mark, Classroom, Lesson, Role

load_dotenv()

DB_URL = (
    f"postgresql://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

engine = create_engine(DB_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine, tables=None)

def get_session():
    with Session(engine) as session:
        yield session

if __name__ == "__main__":
    init_db()
    #migrations.run_migrations()