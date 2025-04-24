from fastapi import APIRouter, Query, HTTPException

from app import crud
from app.api.deps import SessionDep, CurrentUser, RequireRole
from app.schemas.teacher import TeacherPublic, TeacherMarks
from app.schemas.homework import HomeworkPublic
from app.schemas.schedule import SchedulePublic

from app.helpers.path import ID

router = APIRouter(
    prefix='/teachers',
    tags=['teachers'],
    dependencies=[RequireRole('teacher')]
)

@router.get(
    '/me',
    summary="Получить текущего учителя",
    description="Возвращает информацию о текущем аутентифицированном учителе.",
)
def get_current_teacher(
    session: SessionDep,
    teacher: CurrentUser
) -> TeacherPublic:
    return get_teacher(session, teacher.id)

@router.get(
    '/{id}',
    summary="Получить учителя по ID",
    description="Возвращает информацию об учителе по его идентификатору.",
)
def get_teacher(
    session: SessionDep,
    id: int = ID('учителя (пользователя)')
) -> TeacherPublic:
    teacher = crud.get_teacher(session, id)
    if teacher is None:
        raise HTTPException(
            status_code=404,
            detail='Teacher not found'
        )
    return teacher

@router.get(
    '/{id}/homeworks',
    summary="Получить домашние задания, выданные учителем",
    description="Возвращает список домашних заданий, выданных указанным учителем.",
    include_in_schema=False
)
def get_teacher_homeworks(
    session: SessionDep,
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
    session: SessionDep,
    id: int = ID('учителя (пользователя)'),
    group: str = Query(description='Группа', example='11Б'),
    subject: str = Query(description='Предмет', example='Алгебра'),
    # from_: str = Query(None, alias='from', description="Начальная дата для фильтрации (YYYY-MM-DD)"),
    # to: str = Query(None, description="Конечная дата для фильтрации (YYYY-MM-DD)")
) -> TeacherMarks: 
    return crud.get_teacher_marks_full(
        session, id, group, subject
    )

@router.get(
    '/{id}/schedule',
    summary="Получить расписание учителя",
    description="Возвращает расписание для указанного учителя.",
)
def get_teacher_schedule(
    session: SessionDep,
    id: int = ID('учителя (пользователя)'),
    from_: str = Query(None, alias='from', description="Начальная дата для фильтрации (YYYY-MM-DD)"),
    to: str = Query(None, description="Конечная дата для фильтрации (YYYY-MM-DD)")
) -> list[SchedulePublic]:
    schedule = crud.get_teacher_schedule_full(session, id, from_, to)
    if schedule is None:
        raise HTTPException(
            status_code=404,
            detail='Teacher not found'
        )
    return schedule
