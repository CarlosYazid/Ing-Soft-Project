from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import Response

from services import AuthService

router = APIRouter(prefix="/auth")

@router.post("/sign-up")
async def sign_up(form_data: OAuth2PasswordRequestForm = Depends()):
    return await AuthService.sign_up(form_data.username, form_data.password)

@router.post("/sign-in")
async def sign_in(form_data: OAuth2PasswordRequestForm = Depends(), response: Response = None):
    return await AuthService.sign_in(form_data.username, form_data.password)

@router.post("/sign-out")
async def sign_out(response: Response):
    return await AuthService.sign_out()

