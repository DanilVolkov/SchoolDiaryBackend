from fastapi import APIRouter, Body

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
def get_classrooms() -> list[ClassroomPublic]: return

@router.post(
    '/classrooms',
    summary="Создать аудиторию",
    description="Создает новую аудиторию.",
)
def create_classroom(
    c: ClassroomBase = Body(..., description="Данные новой аудитории")
) -> ClassroomPublic: return

@router.get(
    '/classrooms/{id}',
    summary="Получить аудиторию по ID",
    description="Возвращает информацию об аудитории по её идентификатору.",
)
def get_classroom(
    id: int = ID('аудитории')
) -> ClassroomPublic: return

@router.put(
    '/classrooms/{id}',
    summary="Обновить аудиторию",
    description="Обновляет информацию об аудитории по её идентификатору.",
)
def update_classroom(
    id: int = ID('аудитории'), 
    c: ClassroomUpdate = Body(..., description="Данные для обновления аудитории")
) -> ClassroomPublic: return

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
def get_roles() -> list[RolePublic]: return

@router.post(
    '/roles',
    summary="Создать роль",
    description="Создает новую роль.",
)
def create_role(
    r: RoleBase = Body(..., description="Данные новой роли")
) -> RolePublic: return

@router.get(
    '/roles/{id}',
    summary="Получить роль по ID",
    description="Возвращает информацию о роли по её идентификатору.",
)
def get_role(
    id: int = ID('роли')
) -> RolePublic: return

@router.put(
    '/roles/{id}',
    summary="Обновить роль",
    description="Обновляет информацию о роли по её идентификатору.",
)
def update_role(
    id: int = ID('роли'), 
    r: RoleUpdate = Body(..., description="Данные для обновления роли")
) -> RolePublic: return

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
def get_mark_values() -> list[MarkValuePublic]: return

@router.post(
    '/markvalues',
    summary="Создать значение оценки",
    description="Создает новое значение оценки.",
)
def create_mark_value(
    c: MarkValueBase = Body(..., description="Данные нового значения оценки")
) -> MarkValuePublic: return

@router.get(
    '/markvalues/{id}',
    summary="Получить значение оценки по ID",
    description="Возвращает информацию о значении оценки по идентификатору.",
)
def get_mark_value(
    id: int = ID('значения оценки')
) -> MarkValuePublic: return

@router.put(
    '/markvalues/{id}',
    summary="Обновить значение оценки",
    description="Обновляет информацию о значении оценки по идентификатору.",
)
def update_mark_value(
    id: int = ID('значения оценки'), 
    c: MarkValueUpdate = Body(..., description="Данные для обновления значения оценки")
) -> MarkValuePublic: return

@router.delete(
    '/markvalues/{id}',
    summary="Удалить значение оценки",
    description="Удаляет значение оценки по идентификатору.",
)
def delete_mark_value(
    id: int = ID('значения оценки')
): return