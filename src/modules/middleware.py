from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse

class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            return JSONResponse(content={"detail": str(e)}, status_code=500)
