from sqlmodel import SQLModel, Field
from typing import Optional

class GroupBase(SQLModel):
    name: str = Field(schema_extra={'examples': ['11А']})

class GroupUpdate(GroupBase):
    name: Optional[str] = Field(None, schema_extra={'examples': ['11А']})

class GroupPublic(GroupBase):
    id: int = Field(schema_extra={'examples': [101]})

class Group(GroupBase, table=True):
    __tablename__ = 'groups'

    id: int = Field(primary_key=True)