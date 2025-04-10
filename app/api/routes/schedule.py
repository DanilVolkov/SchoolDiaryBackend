from fastapi import APIRouter, Query, Body
from typing import Optional

from app.schemas.schedule import (
    ScheduleObjectBase, ScheduleObjectUpdate, ScheduleObjectPublic,
    SchedulePublic
)
from app.helpers.path import ID

router = APIRouter(
    prefix='/schedule',
    tags=['schedule']
)

@router.get(
    '/',
    summary="Получить расписание",
    description="Возвращает расписание с возможностью фильтрации по группе, учителю и датам.",
)
def get_schedule(
    group: Optional[str] = Query(None, description="Название группы для фильтрации"),
    teacher: Optional[int] = Query(None, description="ID учителя для фильтрации"),
    from_: Optional[str] = Query(None, alias='from', description="Начальная дата для фильтрации (YYYY-MM-DD)"),
    to: Optional[str] = Query(None, description="Конечная дата для фильтрации (YYYY-MM-DD)")
) -> list[SchedulePublic]: return

@router.post(
    '/',
    summary="Создать элемент расписания",
    description="Создает новый элемент в расписании.",
)
def create_schedule_object(
    s: ScheduleObjectBase = Body(..., description="Данные нового элемента расписания")
) -> ScheduleObjectPublic: return

@router.get(
    '/{id}',
    summary="Получить элемент расписания по ID",
    description="Возвращает информацию об элементе расписания по его идентификатору.",
)
def get_schedule_object(
    id: int = ID('элемента расписания')
) -> ScheduleObjectPublic: return

@router.put(
    '/{id}',
    summary="Обновить элемент расписания",
    description="Обновляет информацию об элементе расписания по его идентификатору.",
)
def update_schedule_object(
    id: int = ID('элемента расписания'),
    s: ScheduleObjectUpdate = Body(..., description="Данные для обновления элемента расписания")
) -> ScheduleObjectPublic: return

@router.delete(
    '/{id}',
    summary="Удалить элемент расписания",
    description="Удаляет элемент расписания по его идентификатору.",
)
def delete_schedule_object(
    id: int = ID('элемента расписания')
): return
