from sqlmodel import Field
from typing import Optional

from .user import UserBase, UserUpdate

class StudentBase(UserBase):
    group: str = Field(schema_extra={'examples': ['11A']})

class StudentUpdate(UserUpdate):
    group: Optional[str] = Field(None, schema_extra={'examples': ['11A']})

class StudentPublic(StudentBase):
    id: int = Field(schema_extra={'examples': [101]})