from fastapi import Path

def ID(which: str = ''):
    return Path(..., description=f'Уникальный идентификатор {which}')