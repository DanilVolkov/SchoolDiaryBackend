from sqlmodel import SQLModel, Field
import datetime as dt

from .misc import ID
from .user import UserPublic
from .subject import SubjectPublic
from .student import StudentPublic
from .mark import MarkPublic

class TeacherPublic(UserPublic, ID):
    role: str = Field(schema_extra={'examples': ['Учитель']})
    groups: list[str] = Field(schema_extra={'examples': [['11А', '11Б']]})

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
