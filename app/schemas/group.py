from sqlmodel import SQLModel, Field
from typing import Optional

from .misc import ID

class GroupBase(SQLModel):
    name: str = Field(schema_extra={'examples': ['11А']})

class GroupUpdate(GroupBase):
    name: Optional[str] = Field(None, schema_extra={'examples': ['11А']})

class GroupPublic(GroupBase, ID): ...