from sqlmodel import Session, select

from app.models import User

def get_user_by_username(session: Session, username: str) -> User | None:
    statement = select(User).where(User.username == username)
    result = session.exec(statement).first()
    return result

def authenticate(session: Session, username: str, password: str) -> User | None:
    db_user = get_user_by_username(session, username)
    if not db_user or db_user.password != password:
        return None
    return db_user
