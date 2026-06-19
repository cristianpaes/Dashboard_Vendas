from sqlalchemy import create_engine

DATABASE_URL = (
   "postgresql://neondb_owner:npg_QU0SGrAOLt8C@ep-lively-star-ajae4xdw-pooler.c-3.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
)

engine_postgres = create_engine(DATABASE_URL)