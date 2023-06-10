from db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String


class Url(Base):
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)
    short_url = Column(String, nullable=False)


class One(Base):
    id = Column(Integer, primary_key=True, index=True)
    temp = Column(String, nullable=False)


class Two(Base):
    id = Column(Integer, primary_key=True, index=True)
    temp = Column(String, nullable=False)
    second = Column(String, nullable=False)
