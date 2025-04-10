from sqlmodel import SQLModel, Field
from pydantic import field_validator

from .misc import ID
from .user import UserPublic
from .subject import SubjectPublic
from .mark import MarkPublic

class StudentPublic(UserPublic, ID):
    role: str = Field(schema_extra={'examples': ['Ученик']})
    group: str = Field(schema_extra={'examples': ['11A']})

    @field_validator('role', mode='before')
    @classmethod
    def _get_role(cls, v):
        if hasattr(v, 'name'):
            return v.name
        return ''
    
    @field_validator('group', mode='before')
    @classmethod
    def _get_group(cls, v):
        if hasattr(v, 'name'):
            return v.name
        return ''

class StudentMarks(SQLModel):
    subject: SubjectPublic
    marks: list[MarkPublic]
    average: float = Field(schema_extra={'examples': [4.6]})