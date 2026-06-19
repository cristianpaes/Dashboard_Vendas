from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("DB_HOST")
DATABASE = os.getenv("DB_NAME")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
PORT = os.getenv("DB_PORT")
SSL = os.getenv("DB_SSLMODE")

if not all([HOST, DATABASE, USER, PASSWORD]):
    raise ValueError("Variáveis do .env estão faltando")

DATABASE_URL = (
    f"postgresql+psycopg2://{USER}:{PASSWORD}"
    f"@{HOST}:{PORT}/{DATABASE}"
    f"?sslmode={SSL}"
)

engine_postgres = create_engine(DATABASE_URL)