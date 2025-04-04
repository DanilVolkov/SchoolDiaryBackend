from sqlmodel import create_engine, SQLModel, Session
import os
from dotenv import load_dotenv
from models.misc import MarkValue
from models.user import User
from models.group import Group
from models.subject import Subject
from models.schedule import Schedule
from models.homework import Homework
from models.mark import Mark
from models.misc import Classroom
from models.misc import Role
from models.lesson import Lesson
import migrations

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