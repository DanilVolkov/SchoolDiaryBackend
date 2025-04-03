from sqlmodel import SQLModel, Field

class Classroom(SQLModel, table=True):
    __tablename__ = "classrooms"

    id: int = Field(primary_key=True)
    name: str

class Role(SQLModel, table=True):
    __tablename__ = "roles"

    id: int = Field(primary_key=True)
    name: str

class MarkValue(SQLModel, table=True):
    __tablename__ = "mark_values"

    id: int = Field(primary_key=True)
    value_name: str