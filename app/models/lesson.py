from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import time, date

from .subject import SubjectPublic
from .teacher import TeacherPublic

class LessonBase(SQLModel):
    subject: int = Field(schema_extra={'examples': [201]})
    teacher: int = Field(schema_extra={'examples': [301]})
    time_start: time = Field(schema_extra={'examples': [time(8, 30)]})
    time_end: time = Field(schema_extra={'examples': [time(9, 10)]})
    date_: date = Field(schema_extra={'examples': [date(2025, 3, 31)]}, alias='date')

class LessonUpdate(LessonBase):
    subject: Optional[int] = Field(None, schema_extra={'examples': [201]})
    teacher: Optional[int] = Field(None, schema_extra={'examples': [301]})
    time_start: Optional[str] = Field(None, schema_extra={'examples': [time(8, 30)]})
    time_end: Optional[str] = Field(None, schema_extra={'examples': [time(9, 10)]})
    date_: Optional[str] = Field(None, schema_extra={'examples': [date(2025, 3, 31)]}, alias='date')

class LessonPublic(LessonBase):
    id: int = Field(schema_extra={'examples': [101]})
    subject: SubjectPublic
    teacher: TeacherPublic

class Lesson(SQLModel, table=True):
    __tablename__ = "lessons"

    id: int = Field(primary_key=True)
    schedule_id: int = Field(foreign_key="schedule.id")
    group_id: int = Field(foreign_key="groups.id")
    subject_id: int = Field(foreign_key="subjects.id")
    teacher_id: int = Field(foreign_key="users.id")
    classroom_id: int = Field(foreign_key="classrooms.id")
    lesson_date: date
    time_start: time
    time_end: time