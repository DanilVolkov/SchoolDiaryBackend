from sqlmodel import Session, select, func, and_
from typing import List, Optional
from datetime import date, datetime

from app.models.user import User
from app.models.group import Group
from app.models.subject import Subject
from app.models.schedule import Schedule
from app.models.homework import Homework
from app.models.mark import Mark
from app.models.lesson import Lesson

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
        .where(User.role_id == 1)
    ).first()

def get_student_marks(
    session: Session, 
    student_id: int,
    from_: date | None = None,
    to: date | None = None
) -> List[Mark]:
    statement = select(Mark).where(Mark.student_id == student_id)
    if from_:
        statement = statement.filter(Mark.date >= from_)
    if to:
        statement = statement.filter(Mark.date <= to)
    return session.exec(statement).all()

def get_student_homework(
    session: Session,
    student_id: int,
    from_: date | None = None,
    to: date | None = None
) -> List[Homework]:
    user = session.exec(select(User).where((User.id == student_id) & (User.role_id == 1))).first()
    if not user: return None
    statement = select(Homework).join(Lesson).where(Lesson.group_id == user.group_id)
    if from_:
        statement = statement.filter(Homework.date >= from_)
    if to:
        statement = statement.filter(Homework.date <= to)
    return session.exec(statement).all()

def get_student_schedule(session: Session, student_id: int) -> List[Schedule]:
    user = session.exec(select(User).where((User.id == student_id) & (User.role_id == 1))).first()
    if not user: return None
    statement = select(Schedule).join(Group).where(Group.id == user.group_id)
    return session.exec(statement).all()

def get_student_schedule_full(
    session: Session,
    student_id: int,
    from_: date | None = None,
    to: date | None = None
):
    user = session.exec(select(User).where((User.id == student_id) & (User.role_id == 1))).first()
    if not user: return None

    lessons = select(Lesson).where(Lesson.group_id == user.group_id)
    if from_:
        lessons = lessons.filter(Lesson.lesson_date >= from_)
    if to:
        lessons = lessons.filter(Lesson.lesson_date <= to)
    lessons = session.exec(lessons).all()

    data = dict()
    for lesson in lessons:
        dof = session.exec(select(Schedule.day_of_week).join(Lesson).where(Schedule.id == lesson.id)).first()

        content = data.get(dof, [])

        mark = session.exec(select(Mark).where(Mark.lesson_id == lesson.id, Mark.student_id == user.id)).first()
        homework = session.exec(select(Homework).where(Homework.lesson_id == lesson.id)).first()

        content.append({
            'lesson': lesson,
            'mark': mark,
            'homework': homework
        })

        data[dof] = content

    result = [{'day_of_week': k, 'content': v} for k, v in data.items()]
    return result