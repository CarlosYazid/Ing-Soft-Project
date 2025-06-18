from fastapi import APIRouter


router = APIRouter()

@router.get("/services")
async def get_services():
    return {"message": "List of services"}