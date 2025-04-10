from fastapi import APIRouter, Query, Body, HTTPException
from typing import Optional

from app import crud
from app.api.deps import SessionDep
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
    session: SessionDep,
    student: Optional[int] = Query(None, description="ID ученика для фильтрации"),
    group: Optional[str] = Query(None, description="Название группы для фильтрации"),
    subject: Optional[str] = Query(None, description="Название предмета для фильтрации"),
    from_: Optional[str] = Query(None, alias='from', description="Начальная дата для фильтрации (YYYY-MM-DD)"),
    to: Optional[str] = Query(None, description="Конечная дата для фильтрации (YYYY-MM-DD)")
) -> list[MarkPublic]:
    marks = crud.get_marks(session,
        student, group, subject,
        from_, to
    )
    return marks
@router.post(
    '/',
    summary="Создать оценку",
    description="Создает новую оценку.",
)
def create_mark(
    session: SessionDep,
    m: MarkBase = Body(..., description="Данные новой оценки или списка оценок")
) -> MarkPublic: 
    return crud.create_mark(session, m)

@router.get(
    '/{id}',
    summary="Получить оценку по ID",
    description="Возвращает информацию об оценке по её идентификатору.",
)
def get_mark(
    session: SessionDep,
    id: int = ID('оценки')
) -> MarkPublic:
    mark = crud.get_mark_by_id(session, id)
    if mark is None:
        raise HTTPException(
            status_code=404,
            detail='Mark not found'
        )
    return mark

@router.put(
    '/{id}',
    summary="Обновить оценку",
    description="Обновляет информацию об оценке по её идентификатору.",
)
def update_mark(
    session: SessionDep,
    id: int = ID('оценки'),
    m: MarkUpdate = Body(..., description="Данные для обновления оценки")
) -> MarkPublic:
    mark = crud.update_homework(session, id, m)
    if mark is None:
        raise HTTPException(
            status_code=404,
            detail='Mark not found'
        )
    return mark

@router.delete(
    '/{id}',
    summary="Удалить оценку",
    description="Удаляет оценку по её идентификатору.",
)
def delete_mark(
    session: SessionDep,
    id: int = ID('оценки')
): return crud.delete_mark(session, id)
