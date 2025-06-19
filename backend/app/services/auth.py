from fastapi import Request, Depends, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import jwt

from db import get_db_client
from core import SETTINGS


class AuthService:
    """Service for handling authentication operations."""
    SECURITY_SCHEME = OAuth2PasswordBearer(tokenUrl=SETTINGS.sign_in_redirect_url)
    CRYPT_CONTEXT = CryptContext(schemes=['bcrypt'])

    @classmethod
    async def current_user(cls, token: str = Depends(SECURITY_SCHEME)):
        """Get the current authenticated user from the request state."""
        try:
            payload = jwt.decode(token, SETTINGS.jwt_secret.get_secret_value(), algorithms=[SETTINGS.algorithm])
            user_id = payload.get("sub")
            
            if not user_id:
                raise HTTPException(detail="User ID not found in token", status_code=401)

            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(detail="Token has expired", status_code=401) from jwt.ExpiredSignatureError
        except jwt.InvalidTokenError:
            raise HTTPException(detail="Invalid token", status_code=401) from jwt.InvalidTokenError

    @classmethod
    async def sign_up(cls, email: str, password: str):
        """Sign up a new user."""
        
        client = await get_db_client()
        
        try:
            response = await client.auth.sign_up({
                "email": email,
                "password": password,
            })
        
            if response.user is None:
                raise HTTPException(detail="Sign up failed", status_code=400)
            return RedirectResponse(
                url=SETTINGS.sign_in_redirect_url,
                status_code=303
            )
        except Exception as e:
            raise HTTPException(detail=f"Sign up failed: {str(e)}", status_code=400) from e

    @classmethod
    async def sign_in(cls, email: str, password: str):
        """Sign in an existing user."""
        
        client = await get_db_client()
        
        try:
        
            response = await client.auth.sign_in_with_password(
                {
                    "email": email,
                    "password": password,
                })
        
            if response.user is None:
                raise HTTPException(detail="Sign in failed", status_code=401)

            access_token = response.session.access_token
            refresh_token = response.session.refresh_token
            
            if not access_token:
                raise HTTPException(detail="Access token not found in response", status_code=401)
            response = RedirectResponse(
                url=SETTINGS.home_url,
                status_code=303
            )
            response.set_cookie(
                key="access_token",
                value=access_token,
                httponly=True,
                samesite="Lax"
            )
            response.set_cookie(
                key="refresh_token",
                value=refresh_token,
                httponly=True,
                samesite="Lax"
            )
            
            return response
            
        except Exception as e:
            raise HTTPException(detail=f"Sign in failed: {str(e)}", status_code=401) from e

    @classmethod
    async def sign_out(self):
        
        client = await get_db_client()
        
        await client.auth.sign_out()
        
        response = RedirectResponse(
            url=SETTINGS.sign_in_redirect_url,
            status_code=303
        )
        
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")

        if response is None:
            raise HTTPException(detail="Sign out failed", status_code=400)
        return response

    @classmethod
    async def reset_password(cls, email: str):
        """Reset password for a user."""
        
        client = await get_db_client()
        
        await client.auth.reset_password_for_email(
            email,
            {
                "redirect_to": SETTINGS.reset_password_url
            }
        )
    
    @classmethod
    async def update_password(self, new_password: str):
        """Update password for the authenticated user."""
        
        client = await get_db_client()
        
        response = client.auth.update_user(
            {
                "password": new_password
            }
        )
        if response.user is None:
            raise HTTPException(detail="Password update failed", status_code=400)

        return RedirectResponse(
            url=SETTINGS.sign_in_redirect_url,
            status_code=303
        )