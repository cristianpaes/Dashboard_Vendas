# 🔌 Módulo de Conexão SQL Server com SQLAlchemy

## 📋 Sobre

Este módulo é responsável por criar a conexão entre a aplicação Python e o banco de dados SQL Server utilizando SQLAlchemy e PyODBC.

A conexão é utilizada pelos scripts de ETL, geração de dados e dashboards desenvolvidos no projeto BI Vendas.

---

## 🚀 Tecnologias Utilizadas

- Python
- SQLAlchemy
- PyODBC
- SQL Server
- ODBC Driver 17 for SQL Server

---

## 📂 Arquivo

```text
conexao.py
```

---

## 💻 Código

```python
from sqlalchemy import create_engine

SERVER = 'localhost'
DATABASE = 'BI_VENDAS'

connection_string = (
    f"mssql+pyodbc://@{SERVER}/{DATABASE}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(connection_string)
```

---

## ⚙️ Como Funciona

### Definição do Servidor

```python
SERVER = 'localhost'
```

Define o servidor SQL Server que receberá as conexões.

---

### Definição do Banco

```python
DATABASE = 'BI_VENDAS'
```

Especifica o banco de dados utilizado pela aplicação.

---

### String de Conexão

```python
connection_string = (
    f"mssql+pyodbc://@{SERVER}/{DATABASE}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)
```

Parâmetros utilizados:

| Parâmetro | Descrição |
|------------|------------|
| mssql+pyodbc | Dialeto SQL Server |
| SERVER | Nome do servidor |
| DATABASE | Banco de dados |
| ODBC Driver 17 | Driver oficial Microsoft |
| trusted_connection=yes | Autenticação Windows |

---

### Criação do Engine

```python
engine = create_engine(connection_string)
```

O objeto `engine` será utilizado para:

- Executar consultas SQL
- Ler dados com Pandas
- Inserir registros
- Atualizar tabelas
- Alimentar dashboards Streamlit

---

## 📊 Exemplo de Uso

### Consulta SQL com Pandas

```python
import pandas as pd
from conexao import engine

df = pd.read_sql(
    "SELECT * FROM Fato_Vendas",
    engine
)
```

---

### Inserção de Dados

```python
df.to_sql(
    'Nova_Tabela',
    engine,
    if_exists='append',
    index=False
)
```

---

## 🔐 Segurança

Para ambientes produtivos recomenda-se:

- Utilizar variáveis de ambiente
- Armazenar credenciais em arquivos `.env`
- Evitar usuários com privilégios administrativos
- Utilizar autenticação integrada quando possível

Exemplo:

```python
import os

SERVER = os.getenv("DB_SERVER")
DATABASE = os.getenv("DB_DATABASE")
```

---

## 🎯 Objetivos Demonstrados

Este módulo demonstra conhecimento em:

- Conexão Python ↔ SQL Server
- SQLAlchemy
- Banco de Dados Relacional
- Integração com Pandas
- ETL e Data Engineering
- Desenvolvimento de Dashboards
- Arquitetura de Projetos de Dados

---

## 👨‍💻 Autor

Cristian Camargo

Especialista em:

- SQL Server
- Business Intelligence
- Data Warehouse
- Python
- ERP Sankhya
- Análise de Dados
- Infraestrutura e Segurança

LinkedIn:
https://www.linkedin.com/in/cristiancamargo
