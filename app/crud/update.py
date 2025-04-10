from sqlmodel import Session

from app.schemas.group import GroupUpdate
from app.schemas.homework import HomeworkUpdate
from app.schemas.lesson import LessonUpdate
from app.schemas.mark import MarkUpdate
from app.schemas.misc import ClassroomUpdate, RoleUpdate, MarkValueUpdate
from app.schemas.schedule import ScheduleObjectUpdate
from app.schemas.subject import SubjectUpdate
from app.schemas.user import UserUpdate
from app.models import MarkValue, User, Group, Subject, Schedule, Homework, Mark, Classroom, Lesson, Role

def update_user(session: Session, user_id: int, user: UserUpdate) -> User:
    db_user = session.get(User, user_id)
    if not db_user: return None
    update_data = user.model_dump(exclude_unset=True)
    db_user.sqlmodel_update(update_data)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

def update_group(session: Session, group_id: int, group: GroupUpdate) -> Group:
    db_group = session.get(Group, group_id)
    if not db_group: return None
    update_data  = group.model_dump(exclude_unset=True)
    db_group.sqlmodel_update(update_data)
    session.add(db_group)
    session.commit()
    session.refresh(db_group)
    return db_group

def update_homework(session: Session, homework_id: int, homework: HomeworkUpdate) -> Homework:
    db_homework = session.get(Homework, homework_id)
    if not db_homework: return None
    update_data = homework.model_dump(exclude_unset=True)
    db_homework.sqlmodel_update(update_data)
    session.add(db_homework)
    session.commit()
    session.refresh(db_homework)
    return db_homework

def update_lesson(session: Session, lesson_id: int, lesson: LessonUpdate) -> Lesson:
    db_lesson = session.get(Lesson, lesson_id)
    if not db_lesson: return None
    update_data = lesson.model_dump(exclude_unset=True)
    db_lesson.sqlmodel_update(update_data)
    session.add(db_lesson)
    session.commit()
    session.refresh(db_lesson)
    return db_lesson

def update_mark(session: Session, mark_id: int, mark: MarkUpdate) -> Mark:
    db_mark = session.get(Mark, mark_id)
    if not db_mark: return None
    update_data = mark.model_dump(exclude_unset=True)
    db_mark.sqlmodel_update(update_data)
    session.add(db_mark)
    session.commit()
    session.refresh(db_mark)
    return db_mark

def update_classroom(session: Session, classroom_id: int, classroom: ClassroomUpdate) -> Classroom:
    db_classroom = session.get(Classroom, classroom_id)
    if not db_classroom: return None
    update_data = classroom.model_dump(exclude_unset=True)
    db_classroom.sqlmodel_update(update_data)
    session.add(db_classroom)
    session.commit()
    session.refresh(db_classroom)
    return db_classroom

def update_role(session: Session, role_id: int, role: RoleUpdate) -> Role:
    db_role = session.get(Role, role_id)
    if not db_role: return None
    update_data = role.model_dump(exclude_unset=True)
    db_role.sqlmodel_update(update_data)
    session.add(db_role)
    session.commit()
    session.refresh(db_role)
    return db_role

def update_mark_value(session: Session, mark_value_id: int, mark_value: MarkValueUpdate) -> MarkValue:
    db_mark_value = session.get(MarkValue, mark_value_id)
    if not db_mark_value: return None
    update_data = mark_value.model_dump(exclude_unset=True)
    db_mark_value.sqlmodel_update(update_data)
    session.add(db_mark_value)
    session.commit()
    session.refresh(db_mark_value)
    return db_mark_value

def update_schedule(session: Session, schedule_id: int, schedule: ScheduleObjectUpdate) -> Schedule:
    db_schedule = session.get(Schedule, schedule_id)
    if not db_schedule: return None
    update_data = schedule.model_dump(exclude_unset=True)
    db_schedule.sqlmodel_update(update_data)
    session.add(db_schedule)
    session.commit()
    session.refresh(db_schedule)
    return db_schedule

def update_subject(session: Session, subject_id: int, subject: SubjectUpdate) -> SubjectUpdate:
    db_subject = session.get(Subject, subject_id)
    if not db_subject: return None
    update_data = subject.model_dump(exclude_unset=True)
    db_subject.sqlmodel_update(update_data)
    session.add(db_subject)
    session.commit()
    session.refresh(db_subject)
    return db_subject 