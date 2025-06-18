from db import client
from core import SETTINGS
from infra import  UserNotSignUpError, UserNotSignInError, UserNotSignOutError, PasswordResetError, PasswordUpdateError

class AuthService:
    def __init__(self):
        self.db_client = client

    def sign_up(self, email: str, password: str):
        """Sign up a new user."""
        response = self.db_client.auth.sign_up({
            "email": email,
            "password": password,
        })
        
        if response.error:
            raise UserNotSignUpError(f"Sign up failed: {response.error.message}")
        return response.data
    
    def sign_in(self, email: str, password: str):
        """Sign in an existing user."""
        response = self.db_client.auth.sign_in_with_password(
            {
                "email": email,
                "password": password,
            })
        
        if response.error:
            raise UserNotSignInError(f"Sign in failed: {response.error}")
        return response.data
    
    def sign_out(self):
        response = self.db_client.auth.sign_out()
        if response.error:
            raise UserNotSignOutError(f"Sign out failed: {response.error}")
        return response.data
    
    def reset_password(self, email: str):
        """Reset password for a user."""
        response = self.db_client.auth.reset_password_for_email(
            email,
            {
                "redirect_to": SETTINGS.reset_password_url
            }
        )

        if response.error:
            raise PasswordResetError(f"Password reset failed: {response.error}")
        return response.data
    
    def update_password(self, new_password: str):
        """Update password for the authenticated user."""
        response = self.db_client.auth.update_user(
            {
                "password": new_password
            }
        )
        if response.error:
            raise PasswordUpdateError(f"Password update failed: {response.error}")
        return response.data