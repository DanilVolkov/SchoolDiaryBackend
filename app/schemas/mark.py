from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
import datetime as dt

from .misc import MarkValuePublic

class MarkBase(SQLModel):
    lesson_id: int = Field(schema_extra={'examples': [101]})
    student_id: int = Field(schema_extra={'examples': [101]})
    mark_value_id: int = Field(schema_extra={'examples': [101]})
    date: dt.date = Field(schema_extra={'examples': [dt.date(2025, 3, 31)]}) 

class MarkUpdate(SQLModel):
    mark_value_id: Optional[str] = Field(None, schema_extra={'examples': [101]})
    date: Optional[dt.date] = Field(schema_extra={'examples': [dt.date(2025, 3, 31)]}) 

class MarkPublic(MarkBase):
    id: int = Field(schema_extra={'examples': [101]})
    mark_value: MarkValuePublic