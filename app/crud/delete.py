from sqlmodel import Session

from app.models import MarkValue, User, Group, Subject, Schedule, Homework, Mark, Classroom, Lesson, Role

def delete_user(session: Session, user_id: int) -> bool:
    db_user = session.get(User, user_id)
    if not db_user: return False
    session.delete(db_user)
    session.commit()
    return True

def delete_group(session: Session, group_id: int) -> bool:
    db_group = session.get(Group, group_id)
    if not db_group: return False
    session.delete(db_group)
    session.commit()
    return True

def delete_homework(session: Session, homework_id: int) -> bool:
    db_homework = session.get(Homework, homework_id)
    if not db_homework: return False
    session.delete(db_homework)
    session.commit()
    return True

def delete_lesson(session: Session, lesson_id: int) -> bool:
    db_lesson = session.get(Lesson, lesson_id)
    if not db_lesson: return False
    session.delete(db_lesson)
    session.commit()
    return True

def delete_mark(session: Session, mark_id: int) -> bool:
    db_mark = session.get(Mark, mark_id)
    if not db_mark: return False
    session.delete(db_mark)
    session.commit()
    return True

def delete_classroom(session: Session, classroom_id: int) -> bool:
    db_classroom = session.get(Classroom, classroom_id)
    if not db_classroom: return False
    session.delete(db_classroom)
    session.commit()
    return True

def delete_role(session: Session, role_id: int) -> bool:
    db_role = session.get(Role, role_id)
    if not db_role: return False
    session.delete(db_role)
    session.commit()
    return True

def delete_mark_value(session: Session, mark_value_id: int) -> bool:
    db_mark_value = session.get(MarkValue, mark_value_id)
    if not db_mark_value: return False
    session.delete(db_mark_value)
    session.commit()
    return True

def delete_schedule(session: Session, schedule_id: int) -> bool:
    db_schedule = session.get(Schedule, schedule_id)
    if not db_schedule: return False
    session.delete(db_schedule)
    session.commit()
    return True

def delete_subject(session: Session, subject_id: int) -> bool:
    db_subject = session.get(Subject, subject_id)
    if not db_subject: return False
    session.delete(db_subject)
    session.commit()
    return True