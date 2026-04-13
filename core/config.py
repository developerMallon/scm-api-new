from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    ENVIRONMENT: str = "development"
    
    # URLs para os diferentes ambientes conforme definido no seu .env
    DB_DATABASE_URL_DEVELOPMENT: str = "postgresql+asyncpg://postgres:postgres@localhost/fastapi_db_dev"
    DB_DATABASE_URL_PRODUCTION: str = "postgresql+asyncpg://postgres:postgres@localhost/fastapi_db_prod"

    @property
    def DATABASE_URL(self) -> str:
        # Pega a URL conforme o ambiente
        url = self.DB_DATABASE_URL_PRODUCTION if self.ENVIRONMENT == "production" else self.DB_DATABASE_URL_DEVELOPMENT
        # Certifica de usar o driver asyncpg se ainda não estiver na URL
        if url.startswith("postgresql://"):
            url = url.replace("postgresql://", "postgresql+asyncpg://", 1)
        return url

    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8", 
        extra="ignore"
    )

settings = Settings()
