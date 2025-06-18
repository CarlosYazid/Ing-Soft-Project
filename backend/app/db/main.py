from supabase import create_client, Client

from core import SETTINGS


DB_CLIENT : Client = create_client(SETTINGS.db_url, SETTINGS.db_key.get_secret_value())

