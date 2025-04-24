from datetime import timedelta
from fastapi import APIRouter, HTTPException

from app import security, crud
from app.api.deps import SessionDep, OAuthDep, CurrentUser
from app.schemas.auth import Token, TokenData
from app.schemas.user import UserPublic
from app.config import settings

router = APIRouter(
    prefix='',
    tags=['auth']
)

@router.post(
    '/login',
    summary="Вход пользователя",
    description="Аутентифицирует пользователя и возвращает токен.",
)
def login(
    session: SessionDep,
    data: OAuthDep
) -> Token:
    user = crud.authenticate(
        session=session, username=data.username, password=data.password
    )
    if not user:
        raise HTTPException(
            status_code=400,
            detail='Incorrect credentials'
        )
    token_expires = timedelta(days=settings.ACCESS_TOKEN_EXPIRES_DAYS)
    return Token(
        access_token=security.create_access_token(
            data=TokenData(
                id=user.id, username=user.username, role=user.role.name
            ),
            expires_delta=token_expires
        )
    )

@router.post(
    '/test-token',
    summary="Тест токена",
    description="Проверка корректности Bearer-токена на соответствие пользователю.",
)
def test_token(user: CurrentUser) -> UserPublic:
    return user
