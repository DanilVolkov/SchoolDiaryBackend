from fastapi import APIRouter

from app.api.routes import auth, users
from app.api.routes import students, teachers, groups
from app.api.routes import subjects, lessons, marks, homeworks, schedule

api_router = APIRouter()

api_router.include_router(auth.router)

api_router.include_router(users.router)
api_router.include_router(students.router)
api_router.include_router(teachers.router)
api_router.include_router(groups.router)

api_router.include_router(subjects.router)
api_router.include_router(lessons.router)
api_router.include_router(homeworks.router)
api_router.include_router(marks.router)
api_router.include_router(schedule.router)
