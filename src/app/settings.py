from pydantic import BaseSettings


class Settings(BaseSettings):
    environment: str = "LOCAL"
    log_level: str = "INFO"
    db_host: str = "localhost"
    db_port: int = 3306
    db_user: str = "user"
    db_password: str = "secret"
    db_name: str = "social-network"
    db_pool_min_size: int = 1
    db_pool_max_size: int = 3

    secret_key: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

    @property
    def db_dsn(self):
        return (
            f"mysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}?"
            f"min_size={self.db_pool_min_size}&max_size={self.db_pool_max_size}"
        )

    @property
    def db_dsn_alembic(self):
        return f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


settings = Settings()
