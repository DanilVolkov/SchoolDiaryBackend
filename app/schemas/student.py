from sqlmodel import SQLModel, Field

from .misc import ID
from .user import UserPublic
from .subject import SubjectPublic
from .mark import MarkPublic

class StudentPublic(UserPublic, ID):
    role: str = Field(schema_extra={'examples': ['Ученик']})
    group: str = Field(schema_extra={'examples': ['11A']})

class StudentMarks(SQLModel):
    subject: SubjectPublic
    marks: list[MarkPublic]
    average: str = Field(schema_extra={'examples': ['4.6']})