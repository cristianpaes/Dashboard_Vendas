from sqlalchemy import inspect
import pandas as pd

from conexao_sqlserver import engine_sqlserver
from conexao_postgres import engine_postgres

insp = inspect(engine_sqlserver)

tabelas = insp.get_table_names()

print(f"Tabelas encontradas: {tabelas}")

for tabela in tabelas:

    print(f"\nMigrando tabela: {tabela}...")

    # leitura SQL Server
    query = f"SELECT * FROM [{tabela}]"
    df = pd.read_sql(query, engine_sqlserver)

    # nome seguro para Postgres
    tabela_pg = tabela.lower().replace(" ", "_")

    # escrita no Postgres
    df.to_sql(
        name=tabela_pg,
        con=engine_postgres,
        if_exists='replace',   # depois posso te ensinar 'append seguro'
        index=False,
        method='multi'         # melhora performance
    )

    print(f"Tabela {tabela} migrada com sucesso!")

print("\nMigração concluída!")