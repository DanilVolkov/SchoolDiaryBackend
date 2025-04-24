from fastapi import APIRouter, Query, HTTPException

from app import crud
from app.api.deps import SessionDep, CurrentUser, RequireRole
from app.schemas.student import StudentPublic, StudentMarks
from app.schemas.homework import HomeworkPublic
from app.schemas.schedule import StudentSchedule

from app.helpers.path import ID

router = APIRouter(
    prefix='/students',
    tags=['students'],
    dependencies=[RequireRole('student')]
)

@router.get(
    '/me',
    summary="Получить текущего ученика",
    description="Возвращает информацию о текущем аутентифицированном ученике.",
)
def get_current_student(
    session: SessionDep,
    student: CurrentUser
) -> StudentPublic:
    return get_student(session, student.id)

@router.get(
    '/{id}',
    summary="Получить ученика по ID",
    description="Возвращает информацию об ученике по его идентификатору.",
)
def get_student(
    session: SessionDep,
    id: int = ID('ученика (пользователя)')
) -> StudentPublic: 
    student = crud.get_student(session, id)
    if student is None:
        raise HTTPException(
            status_code=404,
            detail='Student not found'
        )
    return student

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
    marks = crud.get_student_marks(session, id, from_, to)
    data = dict()
    for mark in marks:
        subject = mark.lesson.subject.name
        if data.get(subject) is None:
            data[subject] = {'marks': [], 'sum': 0}
        content = data[subject]
        content['marks'].append(mark)
        if mark.value.name in ['н', 'б']:
            continue
        content['sum'] += int(mark.value.name)
    result = []
    subjects = crud.get_all_subjects(session)
    for subject in subjects:
        content = data.get(subject.name)
        if content is None:
            continue
        marks=sorted(content['marks'], key=lambda m: m.date)
        result.append(StudentMarks(
            subject=subject,
            marks=marks,
            average=round(content['sum']/len(marks), 2)
        ))
    return result

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
