from fastapi import APIRouter, Body

from app.schemas.subject import SubjectBase, SubjectUpdate, SubjectPublic
from app.helpers.path import ID

router = APIRouter(
    prefix='/subjects',
    tags=['subjects']
)

@router.get(
    '/',
    summary="Получить список предметов",
    description="Возвращает список всех учебных предметов.",
)
def get_subjects() -> list[SubjectPublic]: return

@router.post(
    '/',
    summary="Создать предмет",
    description="Создает новый учебный предмет.",
)
def create_subject(
    s: SubjectBase = Body(..., description="Данные нового учебного предмета")
) -> SubjectPublic: return

@router.get(
    '/{id}',
    summary="Получить предмет по ID",
    description="Возвращает информацию о предмете по его идентификатору.",
)
def get_subject(
    id: int = ID('предмета')
) -> SubjectPublic: return

@router.put(
    '/{id}',
    summary="Обновить предмет",
    description="Обновляет информацию о предмете по его идентификатору.",
)
def update_subject(
    id: int = ID('предмета'),
    s: SubjectUpdate = Body(..., description="Данные для обновления предмета")
) -> SubjectPublic: return

@router.delete(
    '/{id}',
    summary="Удалить предмет",
    description="Удаляет предмет по его идентификатору.",
)
def delete_subject(
    id: int = ID('предмета')
): return
