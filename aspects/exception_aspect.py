
from functools import wraps
from fastapi.responses import JSONResponse
from custom_exceptions.custom_exceptions import SecurityException, UnauthorizedAccessException, ValidationException
from logger.logger import *


def exception_aspect(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except ValidationException as e:
            return JSONResponse(e.message, status_code=400)

        except UnauthorizedAccessException as e:
            return JSONResponse(e.message, status_code=401)

        except SecurityException as e:
            return JSONResponse(e.message, status_code=403)

        except Exception as e:
            logger.error(str(e), exc_info=True)
            return JSONResponse(
                {"message": str(e),
                 "status": False,
                 "data": None}, status_code=500)

    return wrapper
