from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

from .lesson import LessonPublic

class HomeworkBase(BaseModel):
    desc: str = Field(examples=['Написать очередное сочинение'])
    lesson: int = Field(examples=[101])
    due_date: date = Field(examples=[date(2025, 3, 31)])

class HomeworkUpdate(HomeworkBase):
    desc: Optional[str] = Field(examples=['Написать очередное сочинение']) 
    lesson: Optional[int] = Field(examples=[101])
    due_date: Optional[date] = Field(examples=[date(2025, 3, 31)])

class HomeworkPublic(HomeworkBase):
    lesson: LessonPublic