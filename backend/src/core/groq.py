from groq import AsyncGroq
from core import SETTINGS

GROQ_CLIENT = AsyncGroq(
    api_key=SETTINGS.groq_api_key.get_secret_value()
)