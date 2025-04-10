from fastapi import APIRouter, Query, HTTPException

from app import crud
from app.api.deps import SessionDep
from app.schemas.student import StudentPublic, StudentMarks, StudentSchedule
from app.schemas.homework import HomeworkPublic
from app.schemas.mark import MarkPublic
from app.schemas.schedule import SchedulePublic

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
    include_in_schema=False
)
def get_student_homeworks(
    session: SessionDep,
    id: int = ID('ученика (пользователя)'),
    from_: str = Query(None, alias='from', description="Начальная дата для фильтрации (YYYY-MM-DD)"),
    to: str = Query(None, description="Конечная дата для фильтрации (YYYY-MM-DD)")
) -> list[HomeworkPublic]:
    homeworks = crud.get_student_homework(session, id, from_, to)
    if homeworks is None:
        raise HTTPException(
            status_code=404,
            detail='Student not found'
        )
    return homeworks

@router.get(
    '/{id}/marks',
    summary="Получить оценки ученика",
    description="Возвращает список оценок для указанного ученика.",
)
def get_student_marks(
    session: SessionDep,
    id: int = ID('ученика (пользователя)'),
    from_: str = Query(None, alias='from', description="Начальная дата для фильтрации (YYYY-MM-DD)"),
    to: str = Query(None, description="Конечная дата для фильтрации (YYYY-MM-DD)")
) -> list[StudentMarks]:
    return

@router.get(
    '/{id}/schedule',
    summary="Получить расписание ученика",
    description="Возвращает расписание для указанного ученика.",
)
def get_student_schedule(
    session: SessionDep,
    id: int = ID('ученика (пользователя)'),
    from_: str = Query(None, alias='from', description="Начальная дата для фильтрации (YYYY-MM-DD)"),
    to: str = Query(None, description="Конечная дата для фильтрации (YYYY-MM-DD)")
) -> list[StudentSchedule]:
    schedule = crud.get_student_schedule_full(session, id, from_, to)
    if schedule is None:
        raise HTTPException(
            status_code=404,
            detail='Student not found'
        )
    return schedule
