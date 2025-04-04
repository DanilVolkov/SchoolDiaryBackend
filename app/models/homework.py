from sqlmodel import SQLModel, Field
from typing import Optional
import datetime as dt

from .lesson import LessonPublic
from .teacher import TeacherPublic

class HomeworkBase(SQLModel):
    lesson_id: int = Field(schema_extra={'examples': [101]})
    teacher_id: int = Field(schema_extra={'examples': [101]})
    description: str = Field(schema_extra={'examples': ['Написать очередное сочинение']})
    date: dt.date = Field(schema_extra={'examples': [dt.date(2025, 3, 31)]})

class HomeworkUpdate(HomeworkBase):
    lesson_id: Optional[int] = Field(None, schema_extra={'examples': [101]})
    teacher_id: Optional[int] = Field(None, schema_extra={'examples': [101]})
    description: Optional[str] = Field(None, schema_extra={'examples': ['Написать очередное сочинение']}) 
    date: Optional[dt.date] = Field(None, schema_extra={'examples': [dt.date(2025, 3, 31)]})

class HomeworkPublic(HomeworkBase):
    id: int = Field(schema_extra={'examples': [101]})
    # lesson: LessonPublic
    # teacher: TeacherPublic

class Homework(HomeworkBase, table=True):
    __tablename__ = "homework"

    id: int = Field(primary_key=True)
    lesson_id: int = Field(foreign_key="lessons.id")
    teacher_id: int = Field(foreign_key="users.id")