import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

def _build_db_url() -> str:
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        return database_url

    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    name = os.getenv("DB_NAME")

    if not (user and password and name):
        raise RuntimeError(
            "Missing DB env vars. Set DATABASE_URL or DB_USER/DB_PASSWORD/DB_NAME (and optionally DB_HOST/DB_PORT)."
        )

    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}"

DB_URL = _build_db_url()
engine = create_engine(DB_URL, pool_pre_ping=True)


def get_engine():
    return engine


def test_db_connection() -> dict:
    with engine.connect() as conn:
        row = conn.execute(text("select 1 as ok, now() as now")).mappings().one()
        return dict(row)