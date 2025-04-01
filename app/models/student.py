from pydantic import Field
from typing import Optional

from .user import UserBase, UserUpdate

class StudentBase(UserBase):
    group: str = Field(examples=['11А'])

class StudentUpdate(UserUpdate):
    group: Optional[str] = Field(None, examples=['11А'])

class StudentPublic(StudentBase):
    id: int = Field(examples=[101])