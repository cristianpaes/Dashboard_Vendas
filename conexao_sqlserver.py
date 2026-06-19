from sqlalchemy import create_engine

SERVER = 'localhost'
DATABASE = 'BI_VENDAS'

connection_string = (
    f"mssql+pyodbc://@{SERVER}/{DATABASE}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine_sqlserver = create_engine(connection_string)
