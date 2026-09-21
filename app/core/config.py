from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # -- DB --
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="ignore"
    )


settings = Settings()
