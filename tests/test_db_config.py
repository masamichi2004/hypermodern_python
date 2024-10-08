from app.db_model.dataclass.db_config import MySQLClient, DBConfig
import app.config.env as env
from sqlalchemy import create_engine
import pytest


@pytest.fixture
def db_config():
    return DBConfig(
        user=env.DB_USER,
        password=env.DB_PASSWORD,
        host=env.DB_HOST,
        port=env.DB_PORT,
        db=env.DB_NAME,
    )


@pytest.fixture
def engine(db_config):
    client = MySQLClient(db_config)
    return create_engine(client.uri)


def test_db_config(db_config):
    client = MySQLClient(db_config)
    uri = env.DB_URL
    assert client.uri == uri


# def test_select_query(engine):
#     query = engine("SELECT * FROM todo")
#     assert query == "SELECT * FROM todo"
