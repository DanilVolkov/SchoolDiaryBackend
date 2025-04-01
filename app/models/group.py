from pydantic import BaseModel, Field
from typing import Optional

from .student import StudentPublic
from .teacher import TeacherPublic

class GroupBase(BaseModel):
    name: str = Field(examples=['11А'])
    teacher: int = Field(examples=[101])

class GroupUpdate(GroupBase):
    name: Optional[str] = Field(None, examples=['11А'])
    teacher: Optional[int] = Field(None, examples=[101])
    students: Optional[list[int]] = Field(None, examples=[[201, 202, 203]])

class GroupPublic(GroupBase):
    id: int = Field(examples=[101])
    teacher: TeacherPublic
    students: list[StudentPublic]