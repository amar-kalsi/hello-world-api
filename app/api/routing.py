from api.v1 import hello
from config import settings
from fastapi import APIRouter

# fmt: off
api_router = APIRouter(prefix=settings.PREFIX)
api_router.include_router(hello.router, prefix="/hello", tags=["Hello"])



