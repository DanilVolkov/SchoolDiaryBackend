from sqlmodel import SQLModel, Field
from typing import Optional

from .teacher import TeacherPublic
from .subject import SubjectPublic
from .misc import ClassroomPublic
from .group import GroupPublic
from .lesson import LessonPublic
from .mark import MarkPublic
from .homework import HomeworkBase

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

class ScheduleObjectPublic(ScheduleObjectBase):
    id: int = Field(None, schema_extra={'examples': [101]})
    group: GroupPublic
    subject: SubjectPublic
    teacher: TeacherPublic
    classroom: ClassroomPublic

class ScheduleObjectExt(SQLModel):
    lesson: LessonPublic
    mark: MarkPublic
    homework: HomeworkBase

class SchedulePublic(SQLModel):
    day_of_week: str = Field(schema_extra={'examples': ['thursday']})
    content: list[ScheduleObjectExt]

class Schedule(ScheduleObjectBase, table=True):
    __tablename__ = "schedule"

    id: int = Field(primary_key=True)
    group_id: int = Field(foreign_key="groups.id")
    subject_id: int = Field(foreign_key="subjects.id")
    teacher_id: int = Field(foreign_key="users.id")
    classroom_id: int = Field(foreign_key="classrooms.id") 