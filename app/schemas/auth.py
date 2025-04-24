from sqlmodel import SQLModel

class Token(SQLModel):
    access_token: str
    toekn_type: str = 'bearer'

class TokenData(SQLModel):
    id: int | None = None
    username: str | None = None
    role: str | None = None
