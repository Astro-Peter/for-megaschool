from fastapi import APIRouter, Response

router = APIRouter()

@router.get("/healthcheck")
async def healthcheck():
    # TODO: Add logic to check database connectivity and other critical services
    return Response(content="OK", status_code=200)
