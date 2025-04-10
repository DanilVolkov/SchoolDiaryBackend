from sqlmodel import Session, select, func, and_
from typing import List, Optional
from datetime import date, datetime

from app.models import MarkValue, User, Group, Subject, Schedule, Homework, Mark, Classroom, Lesson, Role

def get_user(session: Session, user_id: int) -> User:
    return session.get(User, user_id)

def get_users(session: Session, skip: int = 0, limit: int = 100) -> List[User]:
    return session.exec(select(User).offset(skip).limit(limit)).all()

def get_group(session: Session, group_id: int) -> Group:
    return session.get(Group, group_id)

def get_student(session: Session, student_id: int) -> User:
    role = session.exec(select(Role).where(Role.name == 'student')).first()
    statement = select(User)\
                .where(User.id == student_id)\
                .where(User.role_id == role.id)
    result = session.exec(statement).first()
    return result

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
    result = session.exec(statement).all()
    return result

def get_student_homework(
    session: Session,
    student_id: int,
    from_: date | None = None,
    to: date | None = None
) -> List[Homework]:
    role_id = session.exec(select(Role).where(Role.name == 'student')).first().id
    user = session.exec(select(User).where((User.id == student_id) & (User.role_id == role_id))).first()
    if not user: return None
    statement = select(Homework).join(Lesson).where(Lesson.group_id == user.group_id)
    if from_:
        statement = statement.filter(Homework.date >= from_)
    if to:
        statement = statement.filter(Homework.date <= to)
    result = session.exec(statement).all()
    return result

def get_student_schedule(session: Session, student_id: int) -> List[Schedule]:
    role_id = session.exec(select(Role).where(Role.name == 'student')).first().id
    user = session.exec(select(User).where((User.id == student_id) & (User.role_id == role_id))).first()
    if not user: return None
    statement = select(Schedule).join(Group).where(Group.id == user.group_id)
    result = session.exec(statement).all()
    return result

def get_student_schedule_full(
    session: Session,
    student_id: int,
    from_: date | None = None,
    to: date | None = None
):
    role_id = session.exec(select(Role).where(Role.name == 'student')).first().id
    user = session.exec(select(User).where((User.id == student_id) & (User.role_id == role_id))).first()
    if not user: return None

    lessons = select(Lesson).where(Lesson.group_id == user.group_id)
    if from_:
        lessons = lessons.filter(Lesson.date >= from_)
    if to:
        lessons = lessons.filter(Lesson.date <= to)
    lessons = session.exec(lessons.order_by(Lesson.date)).all()

    data = dict()
    for lesson in lessons:
        dow = session.exec(select(Schedule.day_of_week).join(Lesson).where(Schedule.id == lesson.schedule_id)).first()
        datestr = str(lesson.date)

        content = data.get(f'{dow}/{datestr}', [])

        marks = session.exec(select(Mark).where(Mark.lesson_id == lesson.id, Mark.student_id == user.id)).all()
        homework = session.exec(select(Homework).where(Homework.lesson_id == lesson.id)).first()

        content.append({
            'lesson': lesson,
            'marks': marks,
            'homework': homework
        })

        data[f'{dow}/{datestr}'] = content

    result = [{'day_of_week': k[0], 'content': v} for k, v in data.items()]
    return result

def get_teacher(session: Session, teacher_id: int) -> User:
    statement = select(User).where(User.id == teacher_id).where(User.role_id == 2)
    result = session.exec(statement).first()
    return result

def get_teacher_schedule(
    session: Session, 
    teacher_id: int,
    from_: date | None = None,
    to: date | None = None
) -> List[Schedule]:
    statement = select(Schedule).where(Schedule.teacher_id == teacher_id)
    if from_:
        statement = statement.filter(Schedule.date >= from_)
    if to:
        statement = statement.filter(Schedule.date <= to)
    result = session.exec(statement).all()
    return result

def get_teacher_homeworks(
    session: Session, 
    teacher_id: int,
    from_: date | None = None,
    to: date | None = None
) -> List[Homework]:
    statement = select(Homework).where(Homework.teacher_id == teacher_id)
    if from_:
        statement = statement.filter(Homework.date >= from_)
    if to:
        statement = statement.filter(Homework.date <= to)
    result = session.exec(statement).all()
    return result

def get_teacher_marks(
    session: Session,
    teacher_id: int,
    from_: date | None = None,
    to: date | None = None
) -> List[Mark]:
    role_id = session.exec(select(Role).where(Role.name == 'teacher')).first().id
    user = session.exec(select(User).where((User.id == teacher_id) & User.role_id == role_id)).first()
    if not user: return None
    lesson = session.exec(select(Lesson).where(Lesson.teacher_id == user.id)).first()
    if from_:
        lesson = lesson.filter(Lesson.date >= from_)
    if to:
        lesson = lesson.filter(Lesson.date <= to)
    statement = select(Mark).where(Mark.lesson_id == lesson.id)
    result = session.exec(statement).all()
    return result

def get_all_subjects(session: Session) -> List[Subject]:
    statement = select(Subject)
    result = session.exec(statement).all()
    return result

def get_subject(session: Session, subject_id: int) -> Subject:
    statement = select(Subject).where(Subject.id == subject_id)
    result = session.exec(statement).first()
    return result

def get_all_classrooms(session: Session) -> List[Classroom]:
    statement = select(Classroom)
    result = session.exec(statement).all()
    return result

def get_classroom(session: Session, classroom_id: int) -> Classroom:
    statement = select(Classroom).where(Classroom.id == classroom_id)
    result = session.exec(statement).first()
    return result

def get_all_roles(session: Session) -> List[Role]:
    statement = select(Role)
    result = session.exec(statement).all()
    return result

def get_role(session: Session, role_id: int) -> Role:
    statement = select(Role).where(Role.id == role_id)
    result = session.exec(statement).first()
    return result

def get_mark_values(session: Session) -> List[MarkValue]:
    statement = select(MarkValue)
    result = session.exec(statement).all()
    return result

def get_mark_value(session: Session, mark_value_id: int) -> MarkValue:
    statement = select(MarkValue).where(MarkValue.id == mark_value_id)
    result = session.exec(statement).first()
    return result

def get_schedule(
    session: Session, 
    group: str | None = None, 
    teacher: int | None = None,
    from_: date | None = None,
    to: date | None = None
) -> List[Schedule]:
    statement = select(Schedule)
    if group:
        group_id = session.exec(select(Group).where(Group.name == group)).first().id
        statement = statement.filter(Schedule.group_id == group_id)
    if teacher:
        statement = statement.filter(Schedule.teacher_id == teacher)
    if from_:
        statement = statement.filter(Schedule.date >= from_)
    if to:
        statement = statement.filter(Schedule.date <= to)
    result = session.exec(statement).all()
    return result

def get_schedule_by_id(session: Session, schedule_id) -> Schedule:
    statement = select(Schedule).where(Schedule.id == schedule_id)
    result = session.exec(statement).first()
    return result

def get_marks(
    session: Session,
    student: int | None = None,
    group: str | None = None,
    subject: str | None = None,
    from_: date | None = None,
    to: date | None = None
) -> List[Mark]:
    statement = select(Mark)
    if student:
        statement = statement.filter(Mark.student_id == student)
    if group:
        group_id = session.exec(select(Group).where(Group.name == group)).first().id
        lesson = session.exec(select(Lesson).where(Lesson.group_id == group_id)).first()
        statement = statement.filter(Mark.lesson_id == lesson.id)
    if subject:
        subject_id = session.exec(select(Subject).where(Subject.name == subject)).first().id
        lesson = session.exec(select(Lesson).where(Lesson.subject_id == subject_id)).first()
        statement = statement.filter(Mark.lesson_id == lesson.id)
    if from_:
        statement = statement.filter(Mark.date >= from_)
    if to:
        statement = statement.filter(Mark.date <= to)
    result = session.exec(statement).all()
    return result

def get_mark_by_id(session: Session, mark_id: int):
    statement = select(Mark).where(Mark.id == mark_id)
    result = session.exec(statement).first()
    return result

def get_lessons(
    session: Session,
    group: str | None = None,
    teacher: int | None = None,
    from_: date | None = None,
    to: date | None = None
) -> List[Lesson]:
    statement = select(Lesson)
    if group:
        group_id = session.exec(select(Group).where(Group.name == group)).first().id
        statement = statement.filter(Lesson.group_id == group_id)
    if teacher:
        statement = statement.filter(Lesson.teacher_id == teacher)
    if from_:
        statement = statement.filter(Lesson.date >= from_)
    if to:
        statement = statement.filter(Lesson.date <= to)
    result = session.exec(statement).all()
    return result

def get_lesson_by_id(session: Session, lesson_id: int) -> Lesson:
    statement = select(Lesson).where(Lesson.id == lesson_id)
    result = session.exec(statement).first()
    return result

def get_homeworks(
    session: Session, 
    student: int | None = None,
    group: str | None = None,
    teacher: int | None = None,
    from_: date | None = None,
    to: date | None = None
) -> List[Homework]:
    statement = select(Homework)
    if student:
        group_id = session.exec(select(User).where(User.id == student)).first().group_id
        lesson = session.exec(select(Lesson).where(Lesson.group_id == group_id)).first()
        statement = statement.filter(Homework.lesson_id == lesson)
    if group:
        group_id = session.exec(select(Group).where(Group.name == group)).first().id
        lesson = session.exec(select(Lesson).where(Lesson.group_id == group_id)).first()
        statement = statement.filter(Homework.lesson_id == lesson.id)
    if teacher:
        statement = statement.filter(Homework.teacher_id == teacher)
    if from_:
        statement = statement.filter(Homework.date >= from_)
    if to:
        statement = statement.filter(Homework.date <= to)
    result = session.exec(statement).all()
    return result

def get_homework_by_id(session: Session, homework_id: int):
    statement = select(Homework).where(Homework.id == homework_id)
    result = session.exec(statement).first()
    return result