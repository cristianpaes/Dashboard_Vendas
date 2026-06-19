# 📊 Dashboard Comercial | Python + Streamlit + PostgreSQL

Dashboard interativo para análise comercial desenvolvido em **Python**, utilizando **Streamlit**, **PostgreSQL**, **Pandas** e **Plotly**, com visual inspirado no Power BI.

---

## 🚀 Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?logo=postgresql&logoColor=white)

---

## 📌 Objetivo

Disponibilizar indicadores estratégicos para acompanhamento da operação comercial, permitindo análises rápidas e suporte à tomada de decisão.

---

## 📈 Principais Indicadores (KPIs)

- 💰 Faturamento Total
- 📈 Lucro
- 📦 Quantidade Vendida
- 🎯 Ticket Médio

---

## 📊 Análises Disponíveis

### 📈 Evolução Mensal do Faturamento

Acompanhamento da evolução das vendas ao longo do tempo.

### 🏆 Top 10 Vendedores

Ranking dos vendedores com maior faturamento.

### 🌎 Faturamento por Estado

Distribuição geográfica das vendas.

### 📦 Produtos Mais Vendidos

Identificação dos produtos com maior receita.

### 🔄 Devoluções por Motivo

Análise das principais causas das devoluções.

### 📋 Controle de Estoque

Monitoramento dos produtos com maior quantidade em estoque.

---

## 🔍 Filtros Dinâmicos

O dashboard permite filtros por:

- Ano
- Mês
- Estado
- Vendedor
- Categoria
- Produto

---

## 🎨 Interface

Layout profissional inspirado em ferramentas de Business Intelligence:

✔ Tema corporativo

✔ Cards de indicadores

✔ Gráficos interativos

✔ Sidebar dinâmica

✔ Visual semelhante ao Power BI

---

## 🗄️ Banco de Dados

Fonte dos dados:

### PostgreSQL

Principais objetos utilizados:

- VW_DASHBOARD_VENDAS
- VW_ESTOQUE
- Fato_Devolucao
- Dim_Produto

---

## 📂 Estrutura do Projeto

```text
Dashboard_Comercial/
│
├── dashstreamlit.py
├── conexao_postgres.py
├── requirements.txt
├── README.md
└── imagens/
    └── dashboard.png
```

---

## ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/seuusuario/Dashboard_Comercial.git
```

Entre na pasta:

```bash
cd Dashboard_Comercial
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
streamlit run dashstreamlit.py
```

---

## 📸 Dashboard

### Visão Geral

![Dashboard Comercial](imagens/dashboard.png)

Painel desenvolvido em Streamlit para acompanhamento de indicadores comerciais, faturamento, lucro, estoque, devoluções e performance de vendedores.

---

## 🚀 Funcionalidades

✔ Dashboard responsivo

✔ KPIs comerciais

✔ Integração com PostgreSQL

✔ Visualização interativa em Plotly

✔ Filtros dinâmicos

✔ Análise de vendas

✔ Análise de estoque

✔ Análise de devoluções

✔ Layout profissional inspirado no Power BI

---

## 🛠️ Bibliotecas Utilizadas

```python
streamlit
pandas
plotly
sqlalchemy
psycopg2
```

---

## 👨‍💻 Autor

### Cristian Camargo

**DBA SQL Server | Analista de Dados | Python Developer**

💼 LinkedIn:

https://www.linkedin.com/in/cristian-camargo/

🌐 Portfólio:

https://cristiancamargo.netlify.app/

📧 Email:

cristianpcpaes@gmail.com

---

## ⭐ Sobre o Projeto

Projeto desenvolvido para demonstrar conhecimentos em:

- Python
- Streamlit
- PostgreSQL
- SQL
- Data Visualization
- Business Intelligence
- Dashboard Analytics

---

### Se este projeto foi útil, deixe uma ⭐ no repositório.
