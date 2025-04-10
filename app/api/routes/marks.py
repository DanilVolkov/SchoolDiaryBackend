from fastapi import APIRouter, Query, Body
from typing import Optional

from app.schemas.mark import MarkBase, MarkUpdate, MarkPublic
from app.helpers.path import ID

router = APIRouter(
    prefix='/marks',
    tags=['marks']
)

@router.get(
    '/',
    summary="Получить список оценок",
    description="Возвращает список оценок с возможностью фильтрации.",
)
def get_marks(
    student: Optional[int] = Query(None, description="ID ученика для фильтрации"),
    group: Optional[str] = Query(None, description="Название группы для фильтрации"),
    subject: Optional[str] = Query(None, description="Название предмета для фильтрации"),
    from_: Optional[str] = Query(None, alias='from', description="Начальная дата для фильтрации (YYYY-MM-DD)"),
    to: Optional[str] = Query(None, description="Конечная дата для фильтрации (YYYY-MM-DD)")
) -> list[MarkPublic]: return

@router.post(
    '/',
    summary="Создать оценку",
    description="Создает новую оценку.",
)
def create_mark(
    m: MarkBase = Body(..., description="Данные новой оценки или списка оценок")
) -> MarkPublic: return

@router.get(
    '/{id}',
    summary="Получить оценку по ID",
    description="Возвращает информацию об оценке по её идентификатору.",
)
def get_mark(
    id: int = ID('оценки')
) -> MarkPublic: return

@router.put(
    '/{id}',
    summary="Обновить оценку",
    description="Обновляет информацию об оценке по её идентификатору.",
)
def update_mark(
    id: int = ID('оценки'),
    m: MarkUpdate = Body(..., description="Данные для обновления оценки")
) -> MarkPublic: return

@router.delete(
    '/{id}',
    summary="Удалить оценку",
    description="Удаляет оценку по её идентификатору.",
)
def delete_mark(
    id: int = ID('оценки')
): return
