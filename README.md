# 📊 Dashboard_Vendas

## 🚀 Sobre o Projeto

O Dashboard_Vendas é uma aplicação desenvolvida em Python utilizando Streamlit, Plotly e SQL Server para análise comercial e monitoramento de indicadores estratégicos.

O projeto consome dados diretamente de um Data Warehouse modelado em Star Schema, permitindo a visualização de métricas de vendas, lucro, estoque, devoluções e desempenho comercial em tempo real.

O objetivo é demonstrar conhecimentos em:

- Business Intelligence
- Data Analytics
- SQL Server
- Python
- Streamlit
- Plotly
- Data Warehouse
- ETL
- Dashboards Executivos

---

## 🛠 Tecnologias Utilizadas

- Python
- Streamlit
- Pandas
- Plotly
- SQL Server
- SQLAlchemy
- PyODBC

---

## 📂 Estrutura do Projeto

```text
Dashboard_Vendas/
│
├── dashboard.py
├── conexao.py
├── requirements.txt
├── README.md
│
└── imagens/
    └── dashboard.png
```

---

## 🔌 Fonte dos Dados

O dashboard consome informações diretamente do banco SQL Server através do SQLAlchemy.

```python
from conexao import engine

query = """
SELECT *
FROM VW_DASHBOARD_VENDAS
"""

df = pd.read_sql(query, engine)
```

---

## 📈 Indicadores Principais (KPIs)

O painel apresenta os seguintes indicadores:

### 💰 Faturamento Total

Valor total vendido pela empresa.

### 📈 Lucro Total

Lucro consolidado obtido nas vendas.

### 📦 Quantidade Vendida

Total de produtos comercializados.

### 🎯 Ticket Médio

Valor médio por item vendido.

---

## 📊 Análises Disponíveis

### Evolução Mensal

Acompanhamento do faturamento ao longo dos meses.

Recursos:

- Linha temporal
- Marcadores
- Valores formatados
- Hover personalizado

---

### Top 10 Vendedores

Ranking dos vendedores com maior faturamento.

Permite identificar:

- Melhores desempenhos
- Produtividade comercial
- Distribuição das vendas

---

### Faturamento por Estado

Análise geográfica das vendas.

Indicadores:

- Estados com maior faturamento
- Distribuição regional
- Participação de mercado

---

### Produtos Mais Vendidos

Ranking dos produtos com maior faturamento.

Auxilia na identificação de:

- Produtos estratégicos
- Curva ABC
- Oportunidades comerciais

---

### Devoluções por Motivo

Monitoramento das devoluções realizadas.

Principais métricas:

- Quantidade de devoluções
- Valor devolvido
- Motivos mais frequentes

---

### Estoque

Análise dos produtos com maior volume em estoque.

Indicadores:

- Quantidade disponível
- Custo financeiro do estoque
- Produtos com maior investimento

---

## 🎨 Interface

O dashboard foi desenvolvido utilizando uma identidade visual moderna inspirada em ferramentas corporativas como:

- Power BI
- Tableau
- Looker Studio

Características:

- Layout responsivo
- Cards KPI personalizados
- Gráficos interativos
- Paleta de cores profissional
- Experiência otimizada para análise de dados

---

## 🏗 Arquitetura da Solução

```text
SQL Server
      │
      ▼
Views Analíticas
      │
      ▼
SQLAlchemy
      │
      ▼
Pandas
      │
      ▼
Streamlit
      │
      ▼
Dashboard Executivo
```

---

## 📋 Views Utilizadas

### VW_DASHBOARD_VENDAS

Responsável pelos indicadores gerais de vendas.

### VW_DEVOLUCOES

Responsável pelas análises de devoluções.

### VW_ESTOQUE

Responsável pelos indicadores de estoque.

---

## ▶️ Como Executar

### Instalar dependências

```bash
pip install -r requirements.txt
```

Ou:

```bash
pip install streamlit pandas plotly sqlalchemy pyodbc
```

---

### Configurar SQL Server

Editar o arquivo:

```python
conexao.py
```

Exemplo:

```python
SERVER = 'localhost'
DATABASE = 'BI_VENDAS'
```

---

### Executar Dashboard

```bash
streamlit run dashboard.py
```

---

## 📸 Dashboard

Adicione uma captura de tela nesta pasta:

```text
imagens/dashboard.png
```

E exiba no README:

```markdown
![Dashboard](imagens/dashboard.png)
```

---

## 🎯 Competências Demonstradas

Este projeto demonstra experiência em:

- Desenvolvimento de Dashboards
- Business Intelligence
- Data Warehouse
- SQL Server
- Python
- Streamlit
- Plotly
- SQL Analytics
- KPIs Gerenciais
- Visualização de Dados
- ETL
- Modelagem Dimensional

---

## 👨‍💻 Autor

### Cristian Camargo

Profissional de Tecnologia com mais de 28 anos de experiência atuando em:

- Administração de Banco de Dados
- SQL Server
- ERP Sankhya
- Business Intelligence
- Data Warehouse
- Python
- Análise de Dados
- Infraestrutura e Segurança

### LinkedIn

www.linkedin.com/in/cristiancamargo

---

⭐ Caso tenha gostado do projeto, deixe uma estrela no repositório.
