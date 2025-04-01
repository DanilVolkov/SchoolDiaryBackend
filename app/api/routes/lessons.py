from fastapi import APIRouter, Query, Body

from app.models.lesson import LessonBase, LessonUpdate, LessonPublic
from app.helpers.path import ID

router = APIRouter(
    prefix='/lessons',
    tags=['lessons']
)

@router.get(
    '/',
    summary="Получить список уроков",
    description="Возвращает список уроков с возможностью фильтрации.",
)
def get_lessons(
    group: str = Query(None, description="Название группы для фильтрации"),
    teacher: int = Query(None, description="ID учителя для фильтрации"),
    from_: str = Query(None, alias='from', description="Начальная дата для фильтрации (YYYY-MM-DD)"),
    to: str = Query(None, description="Конечная дата для фильтрации (YYYY-MM-DD)")
) -> list[LessonPublic]: return

@router.post(
    '/',
    summary="Создать урок",
    description="Создает новый урок.",
)
def create_lesson(
    l: LessonBase = Body(..., description="Данные нового урока")
) -> LessonPublic: return

@router.get(
    '/{id}',
    summary="Получить урок по ID",
    description="Возвращает информацию об уроке по его идентификатору.",
)
def get_lesson(
    id: int = ID('урока')
) -> LessonPublic: return

@router.put(
    '/{id}',
    summary="Обновить урок",
    description="Обновляет информацию об уроке по его идентификатору.",
)
def update_lesson(
    id: int = ID('урока'),
    l: LessonUpdate = Body(..., description="Данные для обновления урока")
) -> LessonPublic: return
