from api import route_urls
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(route_urls.router, prefix="/urls", tags=["urls"])
