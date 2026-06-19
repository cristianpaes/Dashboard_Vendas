from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

def get_env(key):
    # 1. tenta Streamlit Cloud (somente se existir secrets)
    try:
        import streamlit as st
        if hasattr(st, "secrets") and key in st.secrets:
            return st.secrets[key]
    except Exception:
        pass

    # 2. fallback local (.env)
    return os.getenv(key)

HOST = get_env("DB_HOST")
DATABASE = get_env("DB_NAME")
USER = get_env("DB_USER")
PASSWORD = get_env("DB_PASSWORD")
PORT = get_env("DB_PORT") or "5432"
SSL = get_env("DB_SSLMODE") or "require"

if not all([HOST, DATABASE, USER, PASSWORD]):
    raise ValueError("Credenciais do banco não encontradas (secrets ou .env)")

DATABASE_URL = (
    f"postgresql+psycopg2://{USER}:{PASSWORD}"
    f"@{HOST}:{PORT}/{DATABASE}"
    f"?sslmode={SSL}"
)

engine_postgres = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)