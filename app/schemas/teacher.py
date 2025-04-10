from sqlmodel import SQLModel, Field
from pydantic import field_validator
import datetime as dt

from .misc import ID
from .user import UserPublic
from .subject import SubjectPublic
from .student import StudentPublic
from .mark import MarkPublic

class TeacherPublic(UserPublic, ID):
    role: str = Field(schema_extra={'examples': ['Учитель']})
    groups: list[str] | None = Field(default=None, schema_extra={'examples': [['11А', '11Б']]})

    @field_validator('role', mode='before')
    @classmethod
    def _get_role(cls, v):
        if hasattr(v, 'name'):
            return v.name
        return ''
    
    @field_validator('groups', mode='before')
    @classmethod
    def _get_group(cls, v):
        return []

class StudentEntry(SQLModel):
    student: StudentPublic
    average_mark: float

class LessonEntry(SQLModel):
    id: int
    date: dt.date
    marks: list[MarkPublic]

class TeacherMarks(SQLModel):
    group: str = Field(schema_extra={'examples': ['11A']})
    subject: SubjectPublic
    students: list[StudentEntry]
    lessons: list[LessonEntry]
