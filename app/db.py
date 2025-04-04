from sqlmodel import create_engine, SQLModel, Session
import os
from dotenv import load_dotenv

from app.models.misc import MarkValue
from app.models.user import User
from app.models.group import Group
from app.models.subject import Subject
from app.models.schedule import Schedule
from app.models.homework import Homework
from app.models.mark import Mark
from app.models.misc import Classroom, Role
from app.models.lesson import Lesson

from app import migrations

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
    migrations.run_migrations()