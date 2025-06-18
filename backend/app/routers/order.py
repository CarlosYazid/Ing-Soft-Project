from fastapi import APIRouter


router = APIRouter()

@router.get("/orders")
async def get_orders():
    return {"message": "List of orders"}