from sqlmodel import SQLModel, Field

from .misc import ID

class SubjectBase(SQLModel):
    name: str = Field(schema_extra={'examples': ['Математика']})

class SubjectUpdate(SubjectBase): ...

class SubjectPublic(SubjectBase, ID): ...