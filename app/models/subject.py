from sqlmodel import SQLModel, Field

class SubjectBase(SQLModel):
    name: str = Field(schema_extra={'examples': ['Математика']})

class SubjectUpdate(SubjectBase):
    ...

class SubjectPublic(SubjectBase):
    id: int = Field(schema_extra={'examples': [101]})

class Subject(SubjectBase, table=True):
    __tablename__ = "subjects"

    id: int = Field(primary_key=True)