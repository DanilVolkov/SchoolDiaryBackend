from fastapi import APIRouter, Body

from app.models.user import UserBase, UserUpdate, UserPublic
from app.helpers.path import ID

router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.get(
    '/',
    summary="Получить список пользователей",
    description="Возвращает список всех пользователей.",
)
def get_users() -> list[UserPublic]: return

@router.post(
    '/',
    summary="Создать пользователя",
    description="Создает нового пользователя.",
)
def create_user(
    body: UserBase = Body(..., description="Данные нового пользователя")
) -> UserPublic: return

@router.get(
    '/{id}',
    summary="Получить пользователя по ID",
    description="Возвращает информацию о пользователе по его идентификатору.",
)
def get_user(
    id: int = ID('пользователя')
) -> UserPublic: return

@router.put(
    '/{id}',
    summary="Обновить пользователя",
    description="Обновляет информацию о пользователе по его идентификатору.",
)
def update_user(
    id: int = ID('пользователя'),
    u: UserUpdate = Body(..., description="Данные для обновления пользователя")
) -> UserPublic: return

@router.delete(
    '/{id}',
    summary="Удалить пользователя",
    description="Удаляет пользователя по его идентификатору.",
)
def delete_user(
    id: int = ID('пользователя')
) -> UserPublic: return
