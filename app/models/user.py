from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import date

class UserBase(SQLModel):
    username: str = Field(schema_extra={'examples': ['yuraskamaz']})
    first_name: str = Field(schema_extra={'examples': ['Юрий']})
    last_name: str = Field(schema_extra={'examples': ['Коршунов']})
    middle_name: Optional[str] = Field(None, schema_extra={'examples': ['Владимирович']})
    date_of_birth: date = Field(schema_extra={'examples': [date(2003, 8, 15)]})
    role_id: int = Field(schema_extra={'examples': [101]})
    group_id: int = Field(schema_extra={'examples': [101]})

class UserUpdate(UserBase):
    username: Optional[str] = Field(None, schema_extra={'examples': ['yuraskamaz']})
    first_name: Optional[str] = Field(None, schema_extra={'examples': ['Юрий']})
    last_name: Optional[str] = Field(None, schema_extra={'examples': ['Коршунов']})
    middle_name: Optional[str] = Field(None, schema_extra={'examples': ['Владимирович']})
    date_of_birth: Optional[date] = Field(None, schema_extra={'examples': [date(2003, 8, 15)]})
    role_id: Optional[int] = Field(None, schema_extra={'examples': [101]})
    group_id: Optional[int] = Field(None, schema_extra={'examples': [101]})

class UserPublic(UserBase):
    id: int = Field(schema_extra={'examples': ['101']})

class User(UserBase, table=True):
    __tablename__ = "users"

    id: int = Field(primary_key=True)
    password: str
    role_id: int = Field(foreign_key="roles.id")
    group_id: int = Field(foreign_key="groups.id")