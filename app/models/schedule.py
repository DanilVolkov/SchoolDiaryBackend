from sqlmodel import SQLModel, Field
from typing import Optional

from .teacher import TeacherPublic
from .subject import SubjectPublic

from .lesson import LessonPublic
from .mark import MarkPublic
from .homework import HomeworkBase

class ScheduleObjectBase(SQLModel):
    group: int = Field(schema_extra={'examples': [201]})
    subject: int = Field(schema_extra={'examples': [301]})
    teacher: int = Field(schema_extra={'examples': [401]})
    day_of_week: int = Field(schema_extra={'examples': [4]})
    lesson_order: int = Field(schema_extra={'examples': [2]})

class ScheduleObjectUpdate(ScheduleObjectBase):
    group: Optional[int] = Field(None, schema_extra={'examples': [201]})
    subject: Optional[int] = Field(None, schema_extra={'examples': [301]})
    teacher: Optional[int] = Field(None, schema_extra={'examples': [401]})
    day_of_week: Optional[int] = Field(None, schema_extra={'examples': [4]})
    lesson_order: Optional[int] = Field(None, schema_extra={'examples': [2]})

class ScheduleObjectPublic(ScheduleObjectBase):
    id: int = Field(None, schema_extra={'examples': [101]})
    group: str = Field(schema_extra={'examples': ['11А']})
    subject: SubjectPublic
    teacher: TeacherPublic

class ScheduleObjectExt(SQLModel):
    lesson: LessonPublic
    mark: MarkPublic
    homework: HomeworkBase

class SchedulePublic(SQLModel):
    day_of_week: str = Field(schema_extra={'examples': ['thursday']})
    content: list[ScheduleObjectExt]

class Schedule(SQLModel, table=True):
    __tablename__ = "schedule"

    id: int = Field(primary_key=True)
    group_id: int = Field(foreign_key="groups.id")
    subject_id: int = Field(foreign_key="subjects.id")
    teacher_id: int = Field(foreign_key="users.id")
    classroom_id: int = Field(foreign_key="classrooms.id") 
    day_of_week: int
    lesson_order: int