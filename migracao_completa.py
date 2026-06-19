from sqlalchemy import inspect
import pandas as pd

from conexao_sqlserver import engine_sqlserver
from conexao_postgres import engine_postgres

insp = inspect(engine_sqlserver)

tabelas = insp.get_table_names()

print(tabelas)

for tabela in tabelas:

    print(f"Migrando {tabela}...")

    df = pd.read_sql(
        f"SELECT * FROM [{tabela}]",
        engine_sqlserver
    )

    df.to_sql(
        tabela.lower(),
        engine_postgres,
        if_exists='replace',
        index=False
    )

    print(f"{tabela} migrada com sucesso!")

print("Migracao concluida!")