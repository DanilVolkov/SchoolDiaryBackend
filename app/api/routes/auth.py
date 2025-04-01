from fastapi import APIRouter, Query
from app.models.auth import Auth

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@router.get(
    '/login',
    summary="Вход пользователя",
    description="Аутентифицирует пользователя и возвращает токен.",
)
def login(
    login: str = Query(..., description="Логин пользователя"),
    secret: str = Query(..., description="Пароль пользователя")
) -> Auth: return
