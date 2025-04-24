import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import Session
from pydantic import ValidationError
from typing import Annotated

from app.db import get_session
from app.models import User
from app.schemas.auth import TokenData
from app.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SessionDep = Annotated[Session, Depends(get_session)]
OAuthDep = Annotated[OAuth2PasswordRequestForm, Depends()]
TokenDep = Annotated[str, Depends(oauth2_scheme)]

def get_current_user(session: SessionDep, token: TokenDep) -> User:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.HASH_ALGORITHM]
        )
        data = TokenData(**payload)
    except (InvalidTokenError, ValidationError):
        raise HTTPException(
            status_code=403,
            detail='Could not validate credentials'
        )
    user = session.get(User, data.id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail='User not found'
        )
    return user

CurrentUser = Annotated[User, Depends(get_current_user)]
