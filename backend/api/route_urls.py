from api.utils import make_short
from db.repository.urls import create_new_url
from db.repository.urls import delete_short_url
from db.repository.urls import get_full_url
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from pydantic import HttpUrl
from sqlalchemy.orm import Session


router = APIRouter()


# создание короткого url и запись в БД
@router.post("/create/")
async def new_url(url: HttpUrl, db: Session = Depends(get_db)):
    data = await make_short(url)
    create_new_url(url, data, db)
    return data


# удаление ссылки
@router.delete("/delete/")
def delete_url(short_url: HttpUrl, db: Session = Depends(get_db)):
    result = delete_short_url(short_url, db)
    if not result:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ссылка {short_url} не найдена в базе данных",
        )
    else:
        return {"detail": "Ссылка из базы данных удалена успешно"}


# получение полной ссылки из существующей короткой ссылки
@router.get("/get/")
def get_url(short_url: HttpUrl, db: Session = Depends(get_db)):
    result = get_full_url(short_url, db)
    if not result:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ссылка {short_url} не найдена в базе данных",
        )
    else:
        return result
