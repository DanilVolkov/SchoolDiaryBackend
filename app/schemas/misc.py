from sqlmodel import SQLModel, Field
from typing import Optional

class ClassroomBase(SQLModel):
    name: str = Field(schema_extra={"examples": ["404 ауд."]})

class ClassroomUpdate(ClassroomBase):
    name: Optional[str] = Field(None, schema_extra={"examples": ["404 ауд."]})

class ClassroomPublic(ClassroomBase):
    id: int = Field(schema_extra={'examples': [101]})

class RoleBase(SQLModel):
    name: str = Field(schema_extra={"examples": ["ученик"]})

class RoleUpdate(RoleBase):
    name: Optional[str] = Field(None, schema_extra={"examples": ["ученик"]})

class RolePublic(RoleBase):
    id: int = Field(schema_extra={'examples': [101]})

class MarkValueBase(SQLModel):
    value_name: str = Field(schema_extra={"examples": ["5"]})

class MarkValueUpdate(MarkValueBase):
    value_name: Optional[str] = Field(None, schema_extra={"examples": ["5"]})

class MarkValuePublic(MarkValueBase):
    id: int = Field(schema_extra={'examples': [101]})