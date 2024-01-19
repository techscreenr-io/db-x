"""
/healthz endpoint.
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/api/healthz", tags=["service-health"])
async def health_check():
    return {"status": "healthy"}
