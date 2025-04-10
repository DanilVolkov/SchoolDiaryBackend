from sqlmodel import SQLModel, Field
from typing import Optional

class ID(SQLModel):
    id: int = Field(schema_extra={'examples': [101]})

class ClassroomBase(SQLModel):
    name: str = Field(schema_extra={"examples": ["404 ауд."]})

class ClassroomUpdate(ClassroomBase):
    name: Optional[str] = Field(None, schema_extra={"examples": ["404 ауд."]})

class ClassroomPublic(ClassroomBase, ID): ...

class RoleBase(SQLModel):
    name: str = Field(schema_extra={"examples": ["Ученик"]})

class RoleUpdate(RoleBase):
    name: Optional[str] = Field(None, schema_extra={"examples": ["Ученик"]})

class RolePublic(RoleBase, ID): ...

class MarkValueBase(SQLModel):
    name: str = Field(schema_extra={"examples": ["5"]})

class MarkValueUpdate(MarkValueBase):
    name: Optional[str] = Field(None, schema_extra={"examples": ["5"]})

class MarkValuePublic(MarkValueBase, ID): ...