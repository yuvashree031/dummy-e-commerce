import os

API_KEY = os.getenv("API_KEY")
DB_PASSWORD = os.getenv("DB_PASSWORD")


DATABASE_URL = (
    f"mysql://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@localhost/store"
)