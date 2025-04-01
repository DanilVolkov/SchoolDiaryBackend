from pydantic import BaseModel, Field
from typing import Optional
from datetime import time, date

from .subject import SubjectPublic
from .teacher import TeacherPublic

class LessonBase(BaseModel):
    subject: int = Field(examples=[201])
    teacher: int = Field(examples=[301])
    time_start: time = Field(examples=[time(8, 30)])
    time_end: time = Field(examples=[time(9, 10)])
    date_: date = Field(examples=[date(2025, 3, 31)], alias='date')

class LessonUpdate(LessonBase):
    subject: Optional[int] = Field(None, examples=[201])
    teacher: Optional[int] = Field(None, examples=[301])
    time_start: Optional[str] = Field(None, examples=[time(8, 30)])
    time_end: Optional[str] = Field(None, examples=[time(9, 10)])
    date_: Optional[str] = Field(None, examples=[date(2025, 3, 31)], alias='date')

class LessonPublic(LessonBase):
    id: int = Field(examples=[101])
    subject: SubjectPublic
    teacher: TeacherPublic