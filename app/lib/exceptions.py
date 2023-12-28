from starlette.responses import JSONResponse


class APIException(Exception):
    def __init__(
        self, status_code: int, error_code: int, error_type: str, description: str
    ):
        """
        @param status_code: the error status code
        @param error_code: unique error code
        @param error_type: generic external code (non unique)
        @param description: message for integrator to understand
        """
        self.status_code = status_code
        self.error_code = error_code
        self.error_type = error_type
        self.description = description

    def __response__(self):
        return JSONResponse(status_code=self.status_code, content=self.content())

    def content(self) -> dict:
        return {
            "error_code": self.error_code,
            "error_type": self.error_type,
            "description": self.description,
        }

    @staticmethod
    def __example__():
        """produces an openapi spec compatible example for endpoint documentation"""
        return {
            200: {
                "description": "example description",
                "content": {
                    "application/json": {
                        "example": {
                            "error_code": 9999,
                            "error_type": "example_error_type",
                            "description": "an example error",
                        }
                    }
                },
            },
        }


class Errors:
    internal_server_error = APIException(
        error_code=1000,
        error_type="internal_server_error",
        description="internal_server_error",
        status_code=500,
    )
    service_version_missing_error = APIException(
        error_code=1001,
        error_type="internal_server_error",
        description="service_version_missing_error",
        status_code=500,
    )
