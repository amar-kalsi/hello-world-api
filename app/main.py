from api.routing import api_router
from config import settings
from fastapi import FastAPI
from lib.exceptions import APIException
from starlette.requests import Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
    version=settings.SERVICE_VERSION,
    docs_url=settings.PREFIX + "/docs",
    openapi_url=settings.PREFIX,
)
# Configure CORS
origins = ["*"]  # Adjust this to the IP/hostname of the production Kubernetes service]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_router)


@app.exception_handler(APIException)
async def exception_handler(_: Request, exc: APIException) -> JSONResponse:
    return exc.__response__()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
