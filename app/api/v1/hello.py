import logging

from config import settings
from fastapi import APIRouter
from lib.exceptions import Errors, APIException
from models.hello import HelloWorldResponse
from starlette import status
from starlette.responses import JSONResponse

router = APIRouter()
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

@router.get(
    "", responses=APIException.__example__(), status_code=status.HTTP_200_OK
)
def hello_world() -> HelloWorldResponse:
    
    #LOGGER.info(f"Log anything here")
    if not settings.SERVICE_VERSION:
        raise Errors.service_version_missing_error
    else:
        return JSONResponse(content=f"Hello world {settings.SERVICE_VERSION}")
