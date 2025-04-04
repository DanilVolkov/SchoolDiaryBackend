from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import time, date

from .subject import SubjectPublic
from .teacher import TeacherPublic

class LessonBase(SQLModel):
    schedule_id: int = Field(schema_extra={'examples': [101]})
    group_id: int = Field(schema_extra={'examples': [101]})
    subject_id: int = Field(schema_extra={'examples': [101]})
    teacher_id: int = Field(schema_extra={'examples': [101]})
    lesson_date: date = Field(schema_extra={'examples': [date(2025, 3, 31)]})
    time_start: time = Field(schema_extra={'examples': [time(8, 30)]})
    time_end: time = Field(schema_extra={'examples': [time(9, 10)]})

class LessonUpdate(LessonBase):
    schedule_id: Optional[int] = Field(None, schema_extra={'examples': [101]})
    group_id: Optional[int] = Field(None, schema_extra={'examples': [101]})
    subject_id: Optional[int] = Field(None, schema_extra={'examples': [101]})
    teacher_id: Optional[int] = Field(None, schema_extra={'examples': [101]})
    lesson_date: Optional[str] = Field(None, schema_extra={'examples': [date(2025, 3, 31)]})
    time_start: Optional[str] = Field(None, schema_extra={'examples': [time(8, 30)]})
    time_end: Optional[str] = Field(None, schema_extra={'examples': [time(9, 10)]})

class LessonPublic(LessonBase):
    id: int = Field(schema_extra={'examples': [101]})
    subject: SubjectPublic
    teacher: TeacherPublic

class Lesson(LessonBase, table=True):
    __tablename__ = "lessons"

    id: int = Field(primary_key=True)
    schedule_id: int = Field(foreign_key="schedule.id")
    group_id: int = Field(foreign_key="groups.id")
    subject_id: int = Field(foreign_key="subjects.id")
    teacher_id: int = Field(foreign_key="users.id")
    classroom_id: int = Field(foreign_key="classrooms.id")

    subject: 'Subject' = Relationship()
    teacher: 'User' = Relationship()