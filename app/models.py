from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
import datetime as dt

class Enum(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    name: str

class Role(Enum, table=True): ...

class Group(Enum, table=True): ...

class Subject(Enum, table=True): ...

class Classroom(Enum, table=True): ...

class MarkValue(Enum, table=True): ...

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str
    first_name: str
    middle_name: str | None = None
    last_name: str
    date_of_birth: dt.date
    role_id: int | None = Field(default=None, foreign_key='role.id')
    group_id: int | None = Field(default=None, foreign_key='group.id')

    role: Optional[Role] = Relationship()
    group: Optional[Group] = Relationship()

class Lesson(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    schedule_id: int = Field(foreign_key='schedule.id')
    group_id: int = Field(foreign_key='group.id')
    subject_id: int = Field(foreign_key='subject.id')
    teacher_id: int = Field(foreign_key='user.id')
    classroom_id: int = Field(foreign_key='classroom.id')
    date: dt.date
    time_start: dt.time
    time_end: dt.time

    group: Optional[Group] = Relationship()
    subject: Optional[Subject] = Relationship()
    teacher: Optional[User] = Relationship()
    classroom: Optional[Classroom] = Relationship()

class Homework(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    lesson_id: int = Field(foreign_key='lesson.id')
    teacher_id: int = Field(foreign_key='user.id')
    description: str
    date: dt.date

class Schedule(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    group_id: int = Field(foreign_key='group.id')
    subject_id: int = Field(foreign_key='subject.id')
    teacher_id: int = Field(foreign_key='user.id')
    classroom_id: int = Field(foreign_key='classroom.id')
    day_of_week: int
    lesson_order: int

class Mark(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    lesson_id: int = Field(foreign_key='lesson.id')
    student_id: int = Field(foreign_key='user.id')
    value_id: int = Field(foreign_key='markvalue.id')
    date: dt.date

    lesson: Optional[Lesson] = Relationship()
    value: Optional[MarkValue] = Relationship()