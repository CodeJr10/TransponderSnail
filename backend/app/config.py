from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env")

    tesseract_cmd: str | None = None

    max_upload_mb: int = 8

    cors_origins: list[str] = ["http://localhost:5173"]


settings = Settings()