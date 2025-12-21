from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: str = 8000


class ApiConfig(BaseModel):
    prefix: str = "/api"
    version: str = "/v1"
    auth: str = "/auth"
    users: str = "/users"
    messages: str = "/messages"
    requires_verification: bool = True

    @property
    def bearer_token_url(self):
        parts = (self.prefix, self.version, self.auth, "/login")
        path = "".join(parts)
        return path.removeprefix("/")


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    convention: dict[str, str] = {
        # index
        "ix": "ix_%(column_0_label)s",
        # uniq
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        # constraint
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        # foreign key
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        # primary key
        "pk": "pk_%(table_name)s",
    }


class AccessTokenConfig(BaseModel):
    lifetime_seconds: int = 3600
    reset_password_token_secret: str
    verification_token_secret: str


class SuperUserConfig(BaseModel):
    email: str
    password: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # Values from the next file overwrite values from the prior.
        env_file=(".env.template", ".env"),
        env_prefix="APP_CONFIG__",
        case_sensitive=False,
        env_nested_delimiter="__",
    )

    run: RunConfig = RunConfig()
    api: ApiConfig = ApiConfig()
    db: DatabaseConfig
    access_token: AccessTokenConfig
    superuser: SuperUserConfig


settings = Settings()
