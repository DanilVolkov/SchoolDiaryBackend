from sqlmodel import SQLModel, Field
from typing import Optional

class ClassroomBase(SQLModel):
    name: str = Field(schema_extra={"examples": ["404 ауд."]})

class ClassroomUpdate(ClassroomBase):
    name: Optional[str] = Field(None, schema_extra={"examples": ["404 ауд."]})

class Classroom(SQLModel, table=True):
    __tablename__ = "classrooms"

    id: int = Field(primary_key=True)
    name: str

class RoleBase(SQLModel):
    name: str = Field(schema_extra={"examples": ["ученик"]})

class RoleUpdate(RoleBase):
    name: Optional[str] = Field(None, schema_extra={"examples": ["ученик"]})

class Role(SQLModel, table=True):
    __tablename__ = "roles"

    id: int = Field(primary_key=True)
    name: str

class MarkValueBase(SQLModel):
    value_name: str = Field(schema_extra={"examples": ["5"]})

class MarkValueUpdate(MarkValueBase):
    value_name: Optional[str] = Field(None, schema_extra={"examples": ["5"]})

class MarkValue(SQLModel, table=True):
    __tablename__ = "mark_values"

    id: int = Field(primary_key=True)
    value_name: str