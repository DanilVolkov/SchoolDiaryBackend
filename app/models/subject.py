from pydantic import BaseModel, Field

class SubjectBase(BaseModel):
    name: str = Field(examples=['Математика'])

class SubjectUpdate(SubjectBase):
    ...

class SubjectPublic(SubjectBase):
    id: int = Field(examples=[101])