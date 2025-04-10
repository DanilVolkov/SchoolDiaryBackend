from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import field_validator, model_validator
import datetime as dt

from .subject import SubjectPublic
from .misc import ID, ClassroomPublic
from .group import GroupPublic
from .lesson import LessonPublic
from .mark import MarkPublic
from .homework import HomeworkBase
from .user import UserPublic

class ScheduleObjectBase(SQLModel):
    group_id: int = Field(schema_extra={'examples': [101]})
    subject_id: int = Field(schema_extra={'examples': [101]})
    teacher_id: int = Field(schema_extra={'examples': [101]})
    classroom_id: int = Field(schema_extra={'examples': [101]})
    day_of_week: int = Field(schema_extra={'examples': [4]})
    lesson_order: int = Field(schema_extra={'examples': [2]})

class ScheduleObjectUpdate(ScheduleObjectBase):
    group_id: Optional[int] = Field(None, schema_extra={'examples': [101]})
    subject_id: Optional[int] = Field(None, schema_extra={'examples': [101]})
    teacher_id: Optional[int] = Field(None, schema_extra={'examples': [101]})
    classroom_id: Optional[int] = Field(None, schema_extra={'examples': [101]})
    day_of_week: Optional[int] = Field(None, schema_extra={'examples': [4]})
    lesson_order: Optional[int] = Field(None, schema_extra={'examples': [2]})

class ScheduleObjectPublic(ScheduleObjectBase, ID):
    group: GroupPublic
    subject: SubjectPublic
    teacher: UserPublic
    classroom: ClassroomPublic

class ScheduleObjectExt(SQLModel):
    lesson: LessonPublic
    homework: HomeworkBase | None

class SchedulePublic(SQLModel):
    day_of_week: int = Field(schema_extra={'examples': [4]})
    day_of_week_str: str = Field(default='', schema_extra={'examples': ['Четверг']})
    date: dt.date = Field(default=dt.date(2000, 2, 2), schema_extra={'examples': [dt.date(2025, 3, 31)]})
    content: list[ScheduleObjectExt]

    @model_validator(mode='after')
    def set_day_of_week_str(self) -> 'SchedulePublic':
        days = {
            1: 'Понедельник',
            2: 'Вторник',
            3: 'Среда',
            4: 'Четверг',
            5: 'Пятница',
            6: 'Суббота',
            7: 'Воскресенье'
        }
        self.day_of_week_str = days.get(self.day_of_week)
        return self

    @model_validator(mode='after')
    def set_date(self) -> 'SchedulePublic':
        self.date = self.content[0].lesson.date
        return self

class StudentScheduleObject(ScheduleObjectExt):
    marks: list[MarkPublic] | None

class StudentSchedule(SchedulePublic):
    content: list[StudentScheduleObject]