from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class MarkBase(BaseModel):
    value: str = Field(examples=['5'])
    student: int = Field(examples=[201])
    lesson: int = Field(examples=[301])
    date_: date = Field(examples=[date(2025, 3, 31)], alias='date') 

class MarkUpdate(BaseModel):
    value: Optional[str] = Field(None, examples=['5'])
    date_: Optional[date] = Field(examples=[date(2025, 3, 31)], alias='date') 

class MarkPublic(MarkBase):
    id: int = Field(examples=[101])