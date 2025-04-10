from fastapi import APIRouter, Query, Body, HTTPException
from typing import Optional

from app import crud
from app.api.deps import SessionDep
from app.schemas.homework import HomeworkBase, HomeworkUpdate, HomeworkPublic
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
    session: SessionDep,
    student: Optional[int] = Query(None, description="ID ученика для фильтрации"),
    group: Optional[str] = Query(None, description="Название группы для фильтрации"),
    teacher: Optional[int] = Query(None, description="ID учителя для фильтрации"),
    from_: Optional[str] = Query(None, alias='from', description="Начальная дата для фильтрации (YYYY-MM-DD)"),
    to: Optional[str] = Query(None, description="Конечная дата для фильтрации (YYYY-MM-DD)")
) -> list[HomeworkPublic]:
    homeworks = crud.get_homeworks(session,
        student, group, teacher,
        from_, to
    )
    return homeworks

@router.post(
    '/',
    summary="Создать домашнее задание",
    description="Создает новое домашнее задание.",
)
def create_homework(
    session: SessionDep,
    h: HomeworkBase = Body(..., description="Данные нового домашнего задания")
) -> HomeworkPublic: 
    return crud.create_homework(session, h)

@router.get(
    '/{id}',
    summary="Получить домашнее задание по ID",
    description="Возвращает информацию о домашнем задании по его идентификатору.",
)
def get_homework(
    session: SessionDep,
    id: int = ID('домашнего задания')
) -> HomeworkPublic: 
    homework = crud.get_homework_by_id(session, id)
    if homework is None:
        raise HTTPException(
            status_code=404,
            detail='Homework not found'
        )
    return homework

@router.put(
    '/{id}',
    summary="Обновить домашнее задание",
    description="Обновляет информацию о домашнем задании по его идентификатору.",
)
def update_homework(
    session: SessionDep,
    id: int = ID('домашнего задания'),
    h: HomeworkUpdate = Body(..., description="Данные для обновления домашнего задания")
) -> HomeworkPublic:
    homework = crud.update_homework(session, id, h)
    if homework is None:
        raise HTTPException(
            status_code=404,
            detail='Homework not found'
        )
    return homework

@router.delete(
    '/{id}',
    summary="Удалить домашнее задание",
    description="Удаляет домашнее задание по его идентификатору.",
)
def delete_homework(
    session: SessionDep,
    id: int = ID('домашнего задания')
): return crud.delete_homework(session, id)
