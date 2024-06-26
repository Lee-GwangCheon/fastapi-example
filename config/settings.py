from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mongodb_url: str
    model_config = SettingsConfigDict(env_file=".env")


setting = Settings()
