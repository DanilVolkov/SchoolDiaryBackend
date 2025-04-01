from sqlmodel import SQLModel, Field
from typing import Optional

from .student import StudentPublic
from .teacher import TeacherPublic

class GroupBase(SQLModel):
    name: str = Field(schema_extra={'examples': ['11А']})
    teacher: int = Field(schema_extra={'examples': [101]})

class GroupUpdate(GroupBase):
    name: Optional[str] = Field(None, schema_extra={'examples': ['11А']})
    teacher: Optional[int] = Field(None, schema_extra={'examples': [101]})
    students: Optional[list[int]] = Field(None, schema_extra={'examples': [[201, 202, 203]]})

class GroupPublic(GroupBase):
    id: int = Field(schema_extra={'examples': [101]})
    teacher: TeacherPublic
    students: list[StudentPublic]