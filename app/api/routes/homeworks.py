from fastapi import APIRouter, Query, Body
from typing import Optional

from app.models.homework import HomeworkBase, HomeworkUpdate, HomeworkPublic
from app.helpers.path import ID

router = APIRouter(
    prefix='/homeworks',
    tags=['homeworks']
)

@router.get(
    '/',
    summary="Получить список домашних заданий",
    description="Возвращает список домашних заданий с возможностью фильтрации.",
)
def get_homeworks(
    student: Optional[int] = Query(None, description="ID ученика для фильтрации"),
    group: Optional[str] = Query(None, description="Название группы для фильтрации"),
    teacher: Optional[int] = Query(None, description="ID учителя для фильтрации"),
    from_: Optional[str] = Query(None, alias='from', description="Начальная дата для фильтрации (YYYY-MM-DD)"),
    to: Optional[str] = Query(None, description="Конечная дата для фильтрации (YYYY-MM-DD)")
) -> list[HomeworkPublic]: return

@router.post(
    '/',
    summary="Создать домашнее задание",
    description="Создает новое домашнее задание.",
)
def create_homework(
    h: HomeworkBase = Body(..., description="Данные нового домашнего задания")
) -> HomeworkPublic: return

@router.get(
    '/{id}',
    summary="Получить домашнее задание по ID",
    description="Возвращает информацию о домашнем задании по его идентификатору.",
)
def get_homework(
    id: int = ID('домашнего задания')
) -> HomeworkPublic: return

@router.put(
    '/{id}',
    summary="Обновить домашнее задание",
    description="Обновляет информацию о домашнем задании по его идентификатору.",
)
def update_homework(
    id: int = ID('домашнего задания'),
    h: HomeworkUpdate = Body(..., description="Данные для обновления домашнего задания")
) -> HomeworkPublic: return

@router.delete(
    '/{id}',
    summary="Удалить домашнее задание",
    description="Удаляет домашнее задание по его идентификатору.",
)
def delete_homework(
    id: int = ID('домашнего задания')
): return
