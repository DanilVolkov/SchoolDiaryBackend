from fastapi import APIRouter, Body

from app.models.misc import (
    ClassroomBase, ClassroomUpdate, Classroom,
    RoleBase, RoleUpdate, Role,
    MarkValueBase, MarkValueUpdate, MarkValue
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
def get_classrooms() -> list[Classroom]: return

@router.post(
    '/classrooms',
    summary="Создать аудиторию",
    description="Создает новую аудиторию.",
)
def create_classroom(
    c: ClassroomBase = Body(..., description="Данные новой аудитории")
) -> Classroom: return

@router.get(
    '/classrooms/{id}',
    summary="Получить аудиторию по ID",
    description="Возвращает информацию об аудитории по её идентификатору.",
)
def get_classroom(
    id: int = ID('аудитории')
) -> Classroom: return

@router.put(
    '/classrooms/{id}',
    summary="Обновить аудиторию",
    description="Обновляет информацию об аудитории по её идентификатору.",
)
def update_classroom(
    id: int = ID('аудитории'), 
    c: ClassroomUpdate = Body(..., description="Данные для обновления аудитории")
) -> Classroom: return

@router.delete(
    '/classrooms/{id}',
    summary="Удалить аудиторию",
    description="Удаляет аудиторию по её идентификатору.",
)
def delete_classroom(
    id: int = ID('аудитории')
): return



@router.get(
    '/roles',
    summary="Получить список ролей",
    description="Возвращает список ролей.",
)
def get_roles() -> list[Role]: return

@router.post(
    '/roles',
    summary="Создать роль",
    description="Создает новую роль.",
)
def create_role(
    r: RoleBase = Body(..., description="Данные новой роли")
) -> Role: return

@router.get(
    '/roles/{id}',
    summary="Получить роль по ID",
    description="Возвращает информацию о роли по её идентификатору.",
)
def get_role(
    id: int = ID('роли')
) -> Role: return

@router.put(
    '/roles/{id}',
    summary="Обновить роль",
    description="Обновляет информацию о роли по её идентификатору.",
)
def update_role(
    id: int = ID('роли'), 
    r: RoleUpdate = Body(..., description="Данные для обновления роли")
) -> Role: return

@router.delete(
    '/roles/{id}',
    summary="Удалить роль",
    description="Удаляет роль по её идентификатору.",
)
def delete_role(
    id: int = ID('роли')
): return



@router.get(
    '/markvalues',
    summary="Получить список значений оценок",
    description="Возвращает список значений оценок.",
)
def get_mark_values() -> list[MarkValue]: return

@router.post(
    '/markvalues',
    summary="Создать значение оценки",
    description="Создает новое значение оценки.",
)
def create_mark_value(
    c: MarkValueBase = Body(..., description="Данные нового значения оценки")
) -> MarkValue: return

@router.get(
    '/markvalues/{id}',
    summary="Получить значение оценки по ID",
    description="Возвращает информацию о значении оценки по идентификатору.",
)
def get_mark_value(
    id: int = ID('значения оценки')
) -> MarkValue: return

@router.put(
    '/markvalues/{id}',
    summary="Обновить значение оценки",
    description="Обновляет информацию о значении оценки по идентификатору.",
)
def update_mark_value(
    id: int = ID('значения оценки'), 
    c: MarkValueUpdate = Body(..., description="Данные для обновления значения оценки")
) -> MarkValue: return

@router.delete(
    '/markvalues/{id}',
    summary="Удалить значение оценки",
    description="Удаляет значение оценки по идентификатору.",
)
def delete_mark_value(
    id: int = ID('значения оценки')
): return