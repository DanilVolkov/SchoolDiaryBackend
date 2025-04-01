from pydantic import BaseModel, Field
from typing import Optional

from .teacher import TeacherPublic
from .subject import SubjectPublic

from .lesson import LessonPublic
from .mark import MarkPublic
from .homework import HomeworkBase

class ScheduleObjectBase(BaseModel):
    group: int = Field(examples=[201])
    subject: int = Field(examples=[301])
    teacher: int = Field(examples=[401])
    day_of_week: int = Field(examples=[4])
    lesson_order: int = Field(examples=[2])

class ScheduleObjectUpdate(ScheduleObjectBase):
    group: Optional[int] = Field(None, examples=[201])
    subject: Optional[int] = Field(None, examples=[301])
    teacher: Optional[int] = Field(None, examples=[401])
    day_of_week: Optional[int] = Field(None, examples=[4])
    lesson_order: Optional[int] = Field(None, examples=[2])

class ScheduleObjectPublic(ScheduleObjectBase):
    id: int = Field(None, examples=[101])
    group: str = Field(examples=['11А'])
    subject: SubjectPublic
    teacher: TeacherPublic

class ScheduleObjectExt(BaseModel):
    lesson: LessonPublic
    mark: MarkPublic
    homework: HomeworkBase

class SchedulePublic(BaseModel):
    day_of_week: str = Field(examples=['thursday'])
    content: list[ScheduleObjectExt]