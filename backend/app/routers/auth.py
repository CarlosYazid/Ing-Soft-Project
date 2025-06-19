from fastapi import APIRouter

from controllers import AuthController

router = APIRouter()

auth_controller = AuthController()

@router.post("/auth/sign-up")
async def sign_up(email: str, password: str):
    return auth_controller.sign_up(email, password)

@router.post("/auth/sign-in")
async def sign_in(email: str, password: str):
    return auth_controller.sign_in(email, password)

@router.post("/auth/sign-out")
async def sign_out():
    return auth_controller.sign_out()

