from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.errors import ErrorMiddleware

class CustomErrorMiddleware(ErrorMiddleware):
    async def dispatch(self, request, call_next):
        try:
            response = await call_next(request)
        except Exception as e:
            # Handle exception and log it here
            return PlainTextResponse(f"An error occurred: {str(e)}", status_code=500)
        return response
