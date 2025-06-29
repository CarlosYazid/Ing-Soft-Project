import smtplib
from datetime import date
from fastapi import HTTPException

from models import Email, File
from core import SETTINGS


class EmailService:
    """Service for sending emails using SMTP."""

    _session: smtplib.SMTP = None

    @classmethod
    def _ensure_session(cls):
        if cls._session is None:
            cls._session = smtplib.SMTP(SETTINGS.smtp_host, SETTINGS.smtp_port)
            cls._session.starttls()
            cls._session.login(SETTINGS.smtp_comp_email, SETTINGS.smtp_comp_password.get_secret_value())

    @staticmethod
    def _format_addresses(addresses):
        if not addresses:
            return None
        if isinstance(addresses, list):
            return ", ".join(addresses)
        return addresses

    @classmethod
    def send_email(cls, email: Email):
        """Sends an email using the SMTP session."""
        if not isinstance(email, Email):
            raise HTTPException(detail="Expected an instance of Email model", status_code=400)

        cls._ensure_session()

        mime_msg = email.to_Mime()
        cls._session.send_message(mime_msg)
    

    @classmethod
    def close_session(cls):
        """Closes the SMTP session."""
        if cls._session:
            cls._session.quit()
            cls._session = None