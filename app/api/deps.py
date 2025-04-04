from fastapi import Depends
from sqlmodel import Session
from typing import Annotated

from app.db import get_session

SessionDep = Annotated[Session, Depends(get_session)]