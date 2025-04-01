from fastapi import APIRouter, Query

from app.models.teacher import TeacherPublic
from app.models.homework import HomeworkPublic
from app.models.mark import MarkPublic
from app.models.schedule import SchedulePublic

from app.helpers.path import ID

router = APIRouter(
    prefix='/teachers',
    tags=['teachers']
)

@router.get(
    '/me',
    summary="Получить текущего учителя",
    description="Возвращает информацию о текущем аутентифицированном учителе.",
)
def get_current_teacher() -> TeacherPublic: return

@router.get(
    '/{id}/homeworks',
    summary="Получить домашние задания, выданные учителем",
    description="Возвращает список домашних заданий, выданных указанным учителем.",
)
def get_teacher_homeworks(
    id: int = ID('учителя (пользователя)'),
    from_: str = Query(None, alias='from', description="Начальная дата для фильтрации (YYYY-MM-DD)"),
    to: str = Query(None, description="Конечная дата для фильтрации (YYYY-MM-DD)")
) -> list[HomeworkPublic]: return

@router.get(
    '/{id}/marks',
    summary="Получить оценки, выставленные учителем",
    description="Возвращает список оценок, выставленных указанным учителем.",
)
def get_teacher_marks(
    id: int = ID('учителя (пользователя)'),
    from_: str = Query(None, alias='from', description="Начальная дата для фильтрации (YYYY-MM-DD)"),
    to: str = Query(None, description="Конечная дата для фильтрации (YYYY-MM-DD)")
) -> list[MarkPublic]: return

@router.get(
    '/{id}/schedule',
    summary="Получить расписание учителя",
    description="Возвращает расписание для указанного учителя.",
)
def get_teacher_schedule(
    id: int = ID('учителя (пользователя)'),
    from_: str = Query(None, alias='from', description="Начальная дата для фильтрации (YYYY-MM-DD)"),
    to: str = Query(None, description="Конечная дата для фильтрации (YYYY-MM-DD)")
) -> list[SchedulePublic]: return
