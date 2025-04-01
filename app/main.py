from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from app.api.main import api_router

app = FastAPI()

app.include_router(api_router)

@app.get('/', include_in_schema=False)
def root():
    return {
        'message': 'Ey, druzhok-pirozhok. Toboy vybrana nepravilnaya dver. Klub kozhevennogo remesla nakhoditsya dvumya blokami nizhe.',
        'docs_link': 'https://api.nkkz.dev/docs'
    }

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Школьный Дневник",
        version="0.2.0",
        summary='Школа...',
        description=
        """
        Существует исключительно в виде документации.
        Авторизация пока не работает, можно даже не пытаться.
        Возможные ошибки запросов будут описаны по мере их добавления в бизнес-логику.
        """,
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi