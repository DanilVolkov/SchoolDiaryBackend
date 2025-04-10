from fastapi import APIRouter, Body, HTTPException

from app import crud
from app.api.deps import SessionDep
from app.schemas.misc import (
    ClassroomBase, ClassroomUpdate, ClassroomPublic,
    RoleBase, RoleUpdate, RolePublic,
    MarkValueBase, MarkValueUpdate, MarkValuePublic
)
from app.helpers.path import ID

router = APIRouter(
    prefix='',
    tags=['misc']
)

@router.get(
    '/classrooms',
    summary="Получить список аудиторий",
    description="Возвращает список аудиторий.",
)
def get_classrooms(session: SessionDep) -> list[ClassroomPublic]: 
    return crud.get_all_classrooms(session)

@router.post(
    '/classrooms',
    summary="Создать аудиторию",
    description="Создает новую аудиторию.",
)
def create_classroom(
    session: SessionDep,
    c: ClassroomBase = Body(..., description="Данные новой аудитории")
) -> ClassroomPublic:
    return crud.create_classroom(session, c)

@router.get(
    '/classrooms/{id}',
    summary="Получить аудиторию по ID",
    description="Возвращает информацию об аудитории по её идентификатору.",
)
def get_classroom(
    session: SessionDep,
    id: int = ID('аудитории')
) -> ClassroomPublic:
    result = crud.get_classroom(session, id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail='Classroom not found'
        )
    return result

@router.put(
    '/classrooms/{id}',
    summary="Обновить аудиторию",
    description="Обновляет информацию об аудитории по её идентификатору.",
)
def update_classroom(
    session: SessionDep,
    id: int = ID('аудитории'), 
    c: ClassroomUpdate = Body(..., description="Данные для обновления аудитории")
) -> ClassroomPublic:
    result = crud.update_classroom(session, id, c)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail='Classroom not found'
        )
    return result

@router.delete(
    '/classrooms/{id}',
    summary="Удалить аудиторию",
    description="Удаляет аудиторию по её идентификатору.",
)
def delete_classroom(
    session: SessionDep,
    id: int = ID('аудитории')
): return crud.delete_classroom(session, id)



@router.get(
    '/roles',
    summary="Получить список ролей",
    description="Возвращает список ролей.",
)
def get_roles(session: SessionDep) -> list[RolePublic]:
    return crud.get_all_roles(session)

@router.post(
    '/roles',
    summary="Создать роль",
    description="Создает новую роль.",
)
def create_role(
    session: SessionDep,
    r: RoleBase = Body(..., description="Данные новой роли")
) -> RolePublic:
    return crud.create_role(session, r)

@router.get(
    '/roles/{id}',
    summary="Получить роль по ID",
    description="Возвращает информацию о роли по её идентификатору.",
)
def get_role(
    session: SessionDep,
    id: int = ID('роли')
) -> RolePublic:
    result = crud.get_role(session, id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail='Role not found'
        )
    return result

@router.put(
    '/roles/{id}',
    summary="Обновить роль",
    description="Обновляет информацию о роли по её идентификатору.",
)
def update_role(
    session: SessionDep,
    id: int = ID('роли'), 
    r: RoleUpdate = Body(..., description="Данные для обновления роли")
) -> RolePublic:
    result = crud.update_role(session, id, r)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail='Role not found'
        )
    return result

@router.delete(
    '/roles/{id}',
    summary="Удалить роль",
    description="Удаляет роль по её идентификатору.",
)
def delete_role(
    session: SessionDep,
    id: int = ID('роли')
): return crud.delete_role(session, id)



@router.get(
    '/markvalues',
    summary="Получить список значений оценок",
    description="Возвращает список значений оценок.",
)
def get_mark_values(session: SessionDep) -> list[MarkValuePublic]:
    return crud.get_mark_values(session)

@router.post(
    '/markvalues',
    summary="Создать значение оценки",
    description="Создает новое значение оценки.",
)
def create_mark_value(
    session: SessionDep,
    m: MarkValueBase = Body(..., description="Данные нового значения оценки")
) -> MarkValuePublic:
    return crud.create_mark_value(session, m)

@router.get(
    '/markvalues/{id}',
    summary="Получить значение оценки по ID",
    description="Возвращает информацию о значении оценки по идентификатору.",
)
def get_mark_value(
    session: SessionDep,
    id: int = ID('значения оценки')
) -> MarkValuePublic:
    result = crud.get_mark_value(session, id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail='MarkValue not found'
        )
    return result

@router.put(
    '/markvalues/{id}',
    summary="Обновить значение оценки",
    description="Обновляет информацию о значении оценки по идентификатору.",
)
def update_mark_value(
    session: SessionDep,
    id: int = ID('значения оценки'), 
    m: MarkValueUpdate = Body(..., description="Данные для обновления значения оценки")
) -> MarkValuePublic:
    result = crud.update_mark_value(session, id, m)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail='MarkValue not found'
        )
    return result

@router.delete(
    '/markvalues/{id}',
    summary="Удалить значение оценки",
    description="Удаляет значение оценки по идентификатору.",
)
def delete_mark_value(
    session: SessionDep,
    id: int = ID('значения оценки')
): return crud.delete_mark_value(session, id)