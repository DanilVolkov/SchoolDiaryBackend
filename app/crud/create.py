from sqlmodel import Session

from app.schemas.group import GroupBase
from app.schemas.homework import HomeworkBase
from app.schemas.lesson import LessonBase
from app.schemas.mark import MarkBase
from app.schemas.misc import ClassroomBase, RoleBase, MarkValueBase
from app.schemas.schedule import ScheduleObjectBase
from app.schemas.subject import SubjectBase
from app.schemas.user import UserCreate
from app.models import MarkValue, User, Group, Subject, Schedule, Homework, Mark, Classroom, Lesson, Role

def create_user(session: Session, user: UserCreate) -> User:
    db_user = User.model_validate(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

def create_group(session: Session, group: GroupBase) -> Group:
    db_group = Group.model_validate(group)
    session.add(db_group)
    session.commit()
    session.refresh(db_group)
    return db_group

def create_subject(session: Session, subject: SubjectBase) -> Subject:
    db_subject = Subject.model_validate(subject)
    session.add(db_subject)
    session.commit()
    session.refresh(db_subject)
    return db_subject

def create_schedule(session: Session, schedule: ScheduleObjectBase) -> Schedule:
    db_schedule = Schedule.model_validate(schedule)
    session.add(db_schedule)
    session.commit()
    session.refresh(db_schedule)
    return db_schedule

def create_classroom(session: Session, classroom: ClassroomBase) -> Classroom:
    db_classroom = Classroom.model_validate(classroom)
    session.add(db_classroom)
    session.commit()
    session.refresh(db_classroom)
    return db_classroom

def create_role(session: Session, role: RoleBase) -> Role:
    db_role = Role.model_validate(role)
    session.add(db_role)
    session.commit()
    session.refresh(db_role)
    return db_role

def create_mark_value(session: Session, mark_value: MarkValueBase):
    db_mark_value = MarkValue.model_validate(mark_value)
    session.add(db_mark_value)
    session.commit()
    session.refresh(db_mark_value)
    return db_mark_value

def create_mark(session: Session, mark: MarkBase) -> Mark:
    db_mark = Mark.model_validate(mark)
    session.add(db_mark)
    session.commit()
    session.refresh(db_mark)
    return db_mark

def create_lesson(session: Session, lesson: LessonBase) -> Lesson:
    db_lesson = Lesson.model_validate(lesson)
    session.add(db_lesson)
    session.commit()
    session.refresh(db_lesson)
    return db_lesson

def create_homework(session: Session, homework: HomeworkBase) -> Homework:
    db_homework = Homework.model_validate(homework)
    session.add(db_homework)
    session.commit()
    session.refresh(db_homework)
    return db_homework
    