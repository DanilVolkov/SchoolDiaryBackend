from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class UserBase(BaseModel):
    first_name: str = Field(examples=['Юрий'])
    last_name: str = Field(examples=['Коршунов'])
    middle_name: str = Field(examples=['Владимирович'])
    email: str = Field(examples=['yuraskamaz@mail.com'])
    birthdate: date = Field(examples=[date(2003, 8, 15)])

class UserUpdate(UserBase):
    first_name: Optional[str] = Field(None, examples=['Юрий'])
    last_name: Optional[str] = Field(None, examples=['Коршунов'])
    middle_name: Optional[str] = Field(None, examples=['Владимирович'])
    email: Optional[str] = Field(None, examples=['yuraskamaz@mail.com'])
    birthdate: Optional[date] = Field(None, examples=[date(2003, 8, 15)])

class UserPublic(UserBase):
    id: int = Field(examples=[101])