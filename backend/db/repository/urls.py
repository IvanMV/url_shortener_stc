from db.models.urls import Url
from pydantic import HttpUrl
from sqlalchemy.orm import Session


# создание новой ссылки
def create_new_url(url_1: HttpUrl, url_2: HttpUrl, db: Session):
    # проверка существования данного url в БД
    existing_url = db.query(Url).filter(Url.url == url_1)
    # запись в БД, если полного url в БД нет
    if not existing_url.first():
        url_object = Url(url=url_1, short_url=url_2)
        db.add(url_object)
        db.commit()
        db.refresh(url_object)
        return None
    # проверка, не изменился ли короткий url, и перезапись если изменился
    else:
        existing_short_url = db.query(Url).filter(Url.short_url == url_2)
        if existing_short_url != url_2:
            existing_url.update({"short_url": url_2})
            db.commit()
            return None


# удаление ссылки
def delete_short_url(url: HttpUrl, db: Session):
    # проверка существования данного url в БД
    existing_url = db.query(Url).filter(Url.short_url == url)
    if not existing_url.first():
        return 0
    # удаление ссылки, если она существует
    existing_url.delete(synchronize_session=False)
    db.commit()
    return 1


# получение полной ссылки из БД по короткой ссылке
def get_full_url(url: HttpUrl, db: Session):
    # проверка существования данного url в БД
    existing_url = db.query(Url).filter(Url.short_url == url).first()
    if not existing_url:
        return 0
    full_url = existing_url.url
    return full_url
