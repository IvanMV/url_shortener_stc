from typing import Any

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative


# создание базового класса модели для работы с БД
@as_declarative()
class Base:
    id: Any
    __name__: str

    # создание имен таблиц из имен классов
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
