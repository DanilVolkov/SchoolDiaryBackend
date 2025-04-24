from fastapi import APIRouter, Body, HTTPException

from app import crud
from app.api.deps import SessionDep, RequireRoleDep
from app.schemas.user import UserCreate, UserUpdate, UserPublic
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
def get_users(
    session: SessionDep,
    skip: int = 0,
    limit: int = 100
) -> list[UserPublic]:
    return crud.get_users(session, skip, limit)

@router.post(
    '/',
    summary="Создать пользователя",
    description="Создает нового пользователя.",
)
def create_user(
    session: SessionDep,
    admin: RequireRoleDep('admin'),
    u: UserCreate = Body(..., description="Данные нового пользователя")
) -> UserPublic:
    return crud.create_user(session, u)

@router.get(
    '/{id}',
    summary="Получить пользователя по ID",
    description="Возвращает информацию о пользователе по его идентификатору.",
)
def get_user(
    session: SessionDep,
    id: int = ID('пользователя')
) -> UserPublic:
    user = crud.get_user(session, id)
    if user is None:
        raise HTTPException(
            status_code=404,
            detail='User not found'
        )
    return user

@router.put(
    '/{id}',
    summary="Обновить пользователя",
    description="Обновляет информацию о пользователе по его идентификатору.",
)
def update_user(
    session: SessionDep,
    admin: RequireRoleDep('admin'),
    id: int = ID('пользователя'),
    u: UserUpdate = Body(..., description="Данные для обновления пользователя")
) -> UserPublic:
    user = crud.update_user(session, id, u)
    if user is None:
        raise HTTPException(
            status_code=404,
            detail='User not found'
        )
    return user

@router.delete(
    '/{id}',
    summary="Удалить пользователя",
    description="Удаляет пользователя по его идентификатору.",
)
def delete_user(
    session: SessionDep,
    admin: RequireRoleDep('admin'),
    id: int = ID('пользователя')
): return crud.delete_user(session, id)
