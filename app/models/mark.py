from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class MarkBase(SQLModel):
    value: str = Field(schema_extra={'examples': ['5']})
    student: int = Field(schema_extra={'examples': [201]})
    lesson: int = Field(schema_extra={'examples': [301]})
    date_: date = Field(schema_extra={'examples': [date(2025, 3, 31)]}, alias='date') 

class MarkUpdate(SQLModel):
    value: Optional[str] = Field(None, schema_extra={'examples': ['5']})
    date_: Optional[date] = Field(schema_extra={'examples': [date(2025, 3, 31)]}, alias='date') 

class MarkPublic(MarkBase):
    id: int = Field(schema_extra={'examples': [101]})