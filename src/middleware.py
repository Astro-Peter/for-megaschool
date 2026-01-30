from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware import ErrorMiddleware
from starlette.responses import PlainTextResponse
from starlette.requests import Request

class CustomErrorMiddleware(ErrorMiddleware):
    async def dispatch(self, request, call_next):
        try:
            response = await call_next(request)
        except Exception as e:
            # Handle exception and log it here
            return PlainTextResponse(f"An error occurred: {str(e)}", status_code=500)
        return response

from src.modules.logger import Log

logger = Log()

async def log_request(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response: {response.status_code}")
    return response
