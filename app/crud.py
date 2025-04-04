from sqlmodel import Session, select, func, and_
from typing import List, Optional
from datetime import date, datetime
from models.user import User
from models.group import Group
from models.subject import Subject
from models.schedule import Schedule
from models.homework import Homework
from models.mark import Mark
from models.lesson import Lesson

def get_user(session: Session, user_id: int) -> User:
    return session.get(User, user_id)

def get_users(session: Session, skip: int = 0, limit: int = 100) -> List[User]:
    return session.exec(select(User).offset(skip).limit(limit)).all()

def update_user(session: Session, user_id: int, user: User) -> User:
    session_user = session.get(User, user_id)
    if not session_user: return None
    update_data  = user.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(session_user, key, value)
    session.add(session_user)
    session.commit()
    session.refresh(session_user)
    return session_user

def create_user(session: Session, user: User) -> User:
    session_user = session.from_orm(user)
    session.add(session_user)
    session.commit()
    session.refresh(session_user)
    return session_user

def delete_user(session: Session, user_id: int) -> bool:
    session_user = session.get(User, user_id)
    if not session_user: return False
    session.delete(session_user)
    session.commit()
    return True

def get_group(session: Session, group_id: int) -> Group:
    return session.get(Group, group_id)

def update_group(session: Session, group_id: int, group: Group) -> Group:
    session_group = session.get(Group, group_id)
    if not session_group: return None
    update_data  = group.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(session_group, key, value)
    session.add(session_group)
    session.commit()
    session.refresh(session_group)
    return session_group

def delete_group(session: Session, group_id: int) -> bool:
    session_group = session.get(Group, group_id)
    if not session_group: return False
    session.delete(session_group)
    session.commit()
    return True

def get_student(session: Session, student_id: int) -> User:
    return session.exec(
        select(User)
        .where(User.id == student_id)
        .where(User.role_id == 0)
    ).first()

def get_student_marks(session: Session, student_id: int) -> List[Mark]:
    return session.exec(
        select(Mark)
        .where(Mark.student_id == student_id)
    ).all()

def get_student_homework(session: Session, student_id: int) -> List[Homework]:
    user = session.exec(select(User).where((User.id == student_id) & (User.role_id == 0))).first()
    if not user: return None
    statement = select(Homework).join(Lesson).where(Lesson.group_id == user.group_id)
    return session.exec(statement).all()

def get_student_schedule(session: Session, student_id: int) -> List[Schedule]:
    user = session.exec(select(User).where((User.id == student_id) & (User.role_id == 0))).first()
    if not user: return None
    statement = select(Schedule).join(Group).where(Group.id == user.group_id)
    return session.exec(statement).all()

