from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
import datetime as dt

from .subject import SubjectPublic
from .teacher import TeacherPublic
from .misc import ClassroomPublic

class LessonBase(SQLModel):
    schedule_id: int = Field(schema_extra={'examples': [101]})
    group_id: int = Field(schema_extra={'examples': [101]})
    subject_id: int = Field(schema_extra={'examples': [101]})
    teacher_id: int = Field(schema_extra={'examples': [101]})
    classroom_id: int = Field(schema_extra={'examples': [101]})
    date: dt.date = Field(schema_extra={'examples': [dt.date(2025, 3, 31)]})
    time_start: dt.time = Field(schema_extra={'examples': [dt.time(8, 30)]})
    time_end: dt.time = Field(schema_extra={'examples': [dt.time(9, 10)]})

class LessonUpdate(LessonBase):
    schedule_id: Optional[int] = Field(None, schema_extra={'examples': [101]})
    group_id: Optional[int] = Field(None, schema_extra={'examples': [101]})
    subject_id: Optional[int] = Field(None, schema_extra={'examples': [101]})
    teacher_id: Optional[int] = Field(None, schema_extra={'examples': [101]})
    classroom_id: Optional[int] = Field(None, schema_extra={'examples': [101]})
    lesson_date: Optional[str] = Field(None, schema_extra={'examples': [dt.date(2025, 3, 31)]})
    time_start: Optional[str] = Field(None, schema_extra={'examples': [dt.time(8, 30)]})
    time_end: Optional[str] = Field(None, schema_extra={'examples': [dt.time(9, 10)]})

class LessonPublic(LessonBase):
    id: int = Field(schema_extra={'examples': [101]})
    subject: SubjectPublic
    teacher: TeacherPublic
    classroom: ClassroomPublic