from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

from .lesson import LessonPublic

class HomeworkBase(SQLModel):
    desc: str = Field(schema_extra={'examples': ['Написать очередное сочинение']})
    lesson: int = Field(schema_extra={'examples': [101]})
    due_date: date = Field(schema_extra={'examples': [date(2025, 3, 31)]})

class HomeworkUpdate(HomeworkBase):
    desc: Optional[str] = Field(None, schema_extra={'examples': ['Написать очередное сочинение']}) 
    lesson: Optional[int] = Field(None, schema_extra={'examples': [101]})
    due_date: Optional[date] = Field(None, schema_extra={'examples': [date(2025, 3, 31)]})

class HomeworkPublic(HomeworkBase):
    id: int = Field(schema_extra={'examples': [101]})
    lesson: LessonPublic

class Homework(SQLModel, table=True):
    __tablename__ = "homework"

    id: int = Field(primary_key=True)
    lesson_id: int = Field(foreign_key="lessons.id")
    teacher_id: int = Field(foreign_key="users.id")
    desc: str
    date: date