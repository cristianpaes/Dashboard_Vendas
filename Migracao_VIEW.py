from sqlalchemy import inspect
import pandas as pd

from conexao_sqlserver import engine_sqlserver
from conexao_postgres import engine_postgres


df = pd.read_sql(
    "SELECT * FROM VW_ESTOQUE",
    engine_sqlserver
)

df.to_sql(
    "vw_estoque",
    engine_postgres,
    if_exists='replace',
    index=False
)

df = pd.read_sql(
    "SELECT * FROM VW_DASHBOARD_VENDAS",
    engine_sqlserver
)

df.to_sql(
    "vw_dashboard_vendas",
    engine_postgres,
    if_exists='replace',
    index=False
)


df = pd.read_sql(
    "SELECT * FROM VW_DEVOLUCOES",
    engine_sqlserver
)

df.to_sql(
    "VW_DEVOLUCOES",
    engine_postgres,
    if_exists='replace',
    index=False
)



df = pd.read_sql(
    "SELECT * FROM VW_FATURAMENTO_GERAL",
    engine_sqlserver
)

df.to_sql(
    "VW_FATURAMENTO_GERAL",
    engine_postgres,
    if_exists='replace',
    index=False
)

df = pd.read_sql(
    "SELECT * FROM VW_META_REALIZADO",
    engine_sqlserver
)

df.to_sql(
    "VW_META_REALIZADO",
    engine_postgres,
    if_exists='replace',
    index=False
)

df = pd.read_sql(
    "SELECT * FROM VW_VENDAS_ANALITICAS",
    engine_sqlserver
)

df.to_sql(
    "VW_VENDAS_ANALITICAS",
    engine_postgres,
    if_exists='replace',
    index=False
)


