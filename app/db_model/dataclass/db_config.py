from dataclasses import dataclass


@dataclass
class DBConfig:
    user: str
    password: str
    host: str
    port: str
    db: str


class MySQLClient:
    def __init__(self, db_config: DBConfig):
        self.db_config = db_config
        self.uri = f"mysql+mysqlconnector://{db_config.user}:{db_config.password}@{db_config.host}:{db_config.port}/{db_config.db}"
