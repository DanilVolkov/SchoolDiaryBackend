from fastapi import APIRouter, Body

from app.schemas.group import GroupUpdate, GroupPublic
from app.helpers.path import ID 

router = APIRouter(
    prefix='/groups',
    tags=['groups']
)

@router.get(
    '/{id}',
    summary="Получить группу по ID",
    description="Возвращает информацию о группе по её идентификатору.",
)
def get_group(
    id: int = ID('группы')
) -> GroupPublic: return

@router.put(
    '/{id}',
    summary="Обновить группу",
    description="Обновляет информацию о группе по её идентификатору.",
)
def update_group(
    id: int = ID('группы'),
    g: GroupUpdate = Body(..., description="Данные для обновления группы")
) -> GroupPublic: return

@router.delete(
    '/{id}',
    summary="Удалить группу",
    description="Удаляет группу по её идентификатору.",
)
def delete_group(
    id: int = ID('группы')
): return
