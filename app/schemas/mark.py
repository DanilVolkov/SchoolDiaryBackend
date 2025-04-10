from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
import datetime as dt

from .misc import ID, MarkValuePublic

class MarkBase(SQLModel):
    lesson_id: int = Field(schema_extra={'examples': [101]})
    student_id: int = Field(schema_extra={'examples': [101]})
    value_id: int = Field(schema_extra={'examples': [101]})
    date: dt.date = Field(schema_extra={'examples': [dt.date(2025, 3, 31)]}) 

class MarkUpdate(SQLModel):
    value_id: Optional[str] = Field(None, schema_extra={'examples': [101]})
    date: Optional[dt.date] = Field(schema_extra={'examples': [dt.date(2025, 3, 31)]}) 

class MarkPublic(ID, MarkBase):
    value: MarkValuePublic