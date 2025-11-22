import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self) -> None:
        self.database_url = os.getenv("DATABASE_URL")
        self.secret_key = os.getenv("SECRET_KEY")
        self.access_token_expire_minutes = int(
            os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60")
        )

        if not self.database_url:
            raise RuntimeError("DATABASE_URL is not set in .env")
        if not self.secret_key:
            raise RuntimeError("SECRET_KEY is not set in .env")


settings = Settings()
