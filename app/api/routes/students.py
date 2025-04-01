from fastapi import APIRouter, Query

from app.models.student import StudentPublic
from app.models.homework import HomeworkPublic
from app.models.mark import MarkPublic
from app.models.schedule import SchedulePublic

from app.helpers.path import ID

router = APIRouter(
    prefix='/students',
    tags=['students']
)

@router.get(
    '/me',
    summary="Получить текущего ученика",
    description="Возвращает информацию о текущем аутентифицированном ученике.",
)
def get_current_student() -> StudentPublic: return

@router.get(
    '/{id}/homeworks',
    summary="Получить домашние задания ученика",
    description="Возвращает список домашних заданий для указанного ученика.",
)
def get_student_homeworks(
    id: int = ID('ученика (пользователя)'),
    from_: str = Query(None, alias='from', description="Начальная дата для фильтрации (YYYY-MM-DD)"),
    to: str = Query(None, description="Конечная дата для фильтрации (YYYY-MM-DD)")
) -> list[HomeworkPublic]: return

@router.get(
    '/{id}/marks',
    summary="Получить оценки ученика",
    description="Возвращает список оценок для указанного ученика.",
)
def get_student_marks(
    id: int = ID('ученика (пользователя)'),
    from_: str = Query(None, alias='from', description="Начальная дата для фильтрации (YYYY-MM-DD)"),
    to: str = Query(None, description="Конечная дата для фильтрации (YYYY-MM-DD)")
) -> list[MarkPublic]: return

@router.get(
    '/{id}/schedule',
    summary="Получить расписание ученика",
    description="Возвращает расписание для указанного ученика.",
)
def get_student_schedule(
    id: int = ID('ученика (пользователя)'),
    from_: str = Query(None, alias='from', description="Начальная дата для фильтрации (YYYY-MM-DD)"),
    to: str = Query(None, description="Конечная дата для фильтрации (YYYY-MM-DD)")
) -> list[SchedulePublic]: return
