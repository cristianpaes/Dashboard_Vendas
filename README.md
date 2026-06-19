---

## 🔄 Engenharia e Migração de Dados

Este projeto foi construído utilizando um ambiente completo de dados, desde a geração das informações até a disponibilização dos indicadores em ambiente cloud.

### 🏭 Geração de Dados

Foram gerados dados fictícios utilizando a biblioteca **Faker**, simulando um ambiente comercial real contendo:

- Clientes
- Produtos
- Categorias
- Vendedores
- Estados
- Vendas
- Estoque
- Devoluções

O objetivo foi criar uma base consistente para análises e desenvolvimento do Dashboard.

Biblioteca utilizada:

```python
from faker import Faker
```

---

### 🗄️ Banco de Dados SQL Server

Inicialmente os dados foram armazenados em um banco de dados SQL Server local, contendo:

#### Tabelas Dimensionais

- Dim_Cliente
- Dim_Produto
- Dim_Categoria
- Dim_Vendedor
- Dim_Data

#### Tabelas Fato

- Fato_Vendas
- Fato_Devolucao

#### Views

- VW_DASHBOARD_VENDAS
- VW_ESTOQUE

---

### ☁️ Migração para PostgreSQL (Neon)

Após a criação do Data Warehouse em SQL Server, foi realizada a migração dos dados para um ambiente PostgreSQL em nuvem utilizando o serviço Neon.

Processo realizado:

```
SQL Server Local
       ↓
Extração dos dados
       ↓
Python + Pandas
       ↓
PostgreSQL (Neon Cloud)
       ↓
Dashboard Streamlit
```

Essa arquitetura permite que o dashboard seja acessado online sem depender de banco de dados local.

---

## 🔧 Pipeline de Dados

```text
Geração dos Dados (Faker)
            ↓
SQL Server Local
            ↓
Modelagem Dimensional
            ↓
Views Analíticas
            ↓
Migração para PostgreSQL (Neon)
            ↓
Python + Pandas
            ↓
Streamlit
            ↓
Dashboard Interativo
```

---

## 🚀 Funcionalidades

✔ Dashboard responsivo

✔ KPIs comerciais

✔ Filtros dinâmicos

✔ Gráficos interativos com Plotly

✔ Integração com PostgreSQL

✔ Visual profissional inspirado no Power BI

✔ Geração de dados fictícios utilizando Faker

✔ Modelagem dimensional

✔ Data Warehouse

✔ Migração SQL Server → PostgreSQL (Neon)

✔ Análise de estoque

✔ Análise de devoluções

✔ Evolução mensal das vendas

✔ Ranking de vendedores

✔ Produtos mais vendidos

---

## 🛠️ Bibliotecas Utilizadas

```python
streamlit
pandas
plotly
sqlalchemy
psycopg2
faker
```

---

## 📚 Conceitos Aplicados

- Python
- SQL
- SQL Server
- PostgreSQL
- Neon Database
- ETL
- Data Warehouse
- Modelagem Dimensional
- Business Intelligence
- Data Visualization
- Pandas
- Streamlit
- Plotly
- Faker
- Cloud Database
