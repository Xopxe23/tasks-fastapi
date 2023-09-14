from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET: str

    class Config:
        env_file = ".env"


settings = Settings()
