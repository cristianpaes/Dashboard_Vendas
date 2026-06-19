import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio

# ==========================================
# TEMA PROFISSIONAL
# ==========================================

pio.templates.default = "plotly_white"

COR_PRIMARIA = "#5ECDE0"      # Azul
COR_SECUNDARIA = "#10B981"    # Verde claro
COR_TERCIARIA = "#3BBB5B"      # Verde
COR_DESTAQUE = "#8B5CF6"      # Roxo
COR_ALERTA = "#F59E0B"        # Laranja
COR_ERRO = "#EF4444"          # Vermelho



from conexao_postgres import engine_postgres

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================

st.set_page_config(
    page_title='Dashboard Comercial',
    layout='wide'
)

st.markdown("""
<style>
/* =========================
   VARIÁVEIS DE TEMA
========================= */
:root {
    --bg-main: #F3F4F6;
    --bg-card: #FFFFFF;
    --bg-sidebar: #111827;

    --text-primary: #111827;
    --text-secondary: #6B7280;

    --border: #E5E7EB;

    --shadow: 0 2px 10px rgba(0,0,0,0.08);
    --radius: 12px;

    --accent: #2563EB; /* azul corporativo */
}

/* =========================
   FUNDO GERAL (APP)
========================= */
.stApp {
    background-color: var(--bg-main);
    font-family: 'Segoe UI', sans-serif;
}

/* =========================
   SIDEBAR (estilo BI)
========================= */
[data-testid="stSidebar"] {
    background-color: var(--bg-sidebar);
}

/* textos da sidebar */
[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

/* =========================
   CARDS / MÉTRICAS
========================= */
div[data-testid="metric-container"] {
    background-color: var(--bg-card);
    border: 1px solid var(--border);
    padding: 16px;
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    transition: all 0.2s ease-in-out;
}

div[data-testid="metric-container"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(0,0,0,0.12);
}

/* =========================
   TIPOGRAFIA
========================= */
html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
    color: var(--text-primary);
}

/* =========================
   TÍTULOS (BI STYLE)
========================= */
h1 {
    color: var(--text-primary) !important;
    font-weight: 700;
    letter-spacing: -0.5px;
}

h2, h3 {
    color: var(--text-primary) !important;
    font-weight: 600;
}

h4 {
    color: var(--text-secondary) !important;
    font-weight: 500;
    margin-bottom: 6px;
}

/* =========================
   TEXTOS GERAIS
========================= */
p, span, label {
    color: var(--text-primary) !important;
}

/* =========================
   BOTÕES (estilo corporativo)
========================= */
.stButton > button {
    background-color: var(--accent);
    color: white;
    border-radius: 8px;
    border: none;
    padding: 8px 16px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #1D4ED8;
}

/* =========================
   DATAFRAMES (tabelas BI)
========================= */
[data-testid="stDataFrame"] {
    border-radius: var(--radius);
    overflow: hidden;
    border: 1px solid var(--border);
}

/* =========================
   EXPANDERS
========================= */
.streamlit-expanderHeader {
    background-color: #FFFFFF;
    border-radius: var(--radius);
    border: 1px solid var(--border);
}
</style>
""", unsafe_allow_html=True)



# ==========================================
# CARREGAR DADOS
# ==========================================

query = """
SELECT *
FROM VW_DASHBOARD_VENDAS
"""

df = pd.read_sql(query, engine_postgres)

# ==========================================
# FILTROS
# ==========================================

st.sidebar.title("📊 Filtros")

st.sidebar.markdown("---")

st.sidebar.markdown(
"""
### Dashboard Comercial

Análise de vendas, estoque e devoluções.

---
"""
)

with st.sidebar.expander("📅 Período", expanded=True):

    anos = sorted(df['ano'].unique())

    anos_selecionados = st.sidebar.multiselect(
        "Ano",
        anos,
        default=anos
    )

    meses = [
        'Janeiro','Fevereiro','Março','Abril',
        'Maio','Junho','Julho','Agosto',
        'Setembro','Outubro','Novembro','Dezembro'
    ]

    meses_selecionados = st.sidebar.multiselect(
        "Mês",
        meses,
        default=meses
    )

with st.sidebar.expander("🌎 Região", expanded=False):

    estados = sorted(df['estado'].dropna().unique())

    estados_selecionados = st.sidebar.multiselect(
        "Estado",
        estados,
        default=estados
    )

with st.sidebar.expander("👔 Comercial", expanded=False):

    vendedores = sorted(df['nome_vendedor'].dropna().unique())

    vendedores_selecionados = st.sidebar.multiselect(
        "Vendedor",
        vendedores,
        default=vendedores
    )

with st.sidebar.expander("📦 Produtos", expanded=False):

    categorias = sorted(df['nome_categoria'].dropna().unique())

    categorias_selecionadas = st.sidebar.multiselect(
        "Categoria",
        categorias,
        default=categorias
    )

    produtos = sorted(df['nome_produto'].dropna().unique())

    produtos_selecionados = st.sidebar.multiselect(
        "Produto",
        produtos,
        default=produtos
    )

# ==========================================
# DATAFRAME FILTRADO
# ==========================================

df_filtrado = df[
    (df['ano'].isin(anos_selecionados))
    &
    (df['nome_mes'].isin(meses_selecionados))
    &
    (df['estado'].isin(estados_selecionados))
    &
    (df['nome_vendedor'].isin(vendedores_selecionados))
    &
    (df['nome_categoria'].isin(categorias_selecionadas))
    &
    (df['nome_produto'].isin(produtos_selecionados))
]

# ==========================================
# FUNÇÃO MOEDA BR
# ==========================================

def moeda_br(valor):

    return (
        f'R$ {valor:,.2f}'
        .replace(',', 'X')
        .replace('.', ',')
        .replace('X', '.')
    )

# ==========================================
# TÍTULO
# ==========================================

st.markdown(f"""
<h1 style="
color:{COR_PRIMARIA};
text-align:center;
font-size:42px;
font-weight:700;
margin-bottom:0px;
">
📊 Dashboard Comercial
</h1>

<p style="
text-align:center;
color:#6B7280;
font-size:12px;
margin-top:0px;
">
Criado por Cristian Camargo
</p>
""", unsafe_allow_html=True)


# ==========================================
# KPIs
# ==========================================


faturamento = df_filtrado['faturamento'].sum()

lucro = df_filtrado['lucro'].sum()

quantidade = df_filtrado['quantidade_vendida'].sum()    

ticket_medio = (
    faturamento / quantidade
)

faturamento_fmt = moeda_br(faturamento)
lucro_fmt = moeda_br(lucro)
quantidade_fmt = f'{quantidade:,.0f}'.replace(',', '.')
ticket_fmt = moeda_br(ticket_medio)

col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"""
<div style="
background:#EFF6FF;
padding:15px;
border-radius:10px;
text-align:center;
border-left:5px solid #2563EB;">
<h4 style= color:{COR_PRIMARIA};>
💰 Faturamento
</h4>
<h2 style="color:#2563EB;">
{faturamento_fmt}
</h2>
</div>
""", unsafe_allow_html=True)

col2.markdown(f"""
<div style="
background:#ECFDF5;
padding:15px;
border-radius:10px;
text-align:center;
border-left:5px solid #10B981;">
<h4 style= color:{COR_PRIMARIA};>
📈 Lucro
</h4>
<h2 style="color:#10B981;">
{lucro_fmt}
</h2>
</div>
""", unsafe_allow_html=True)

col3.markdown(f"""
<div style="
background:#FFFBEB;
padding:15px;
border-radius:10px;
text-align:center;
border-left:5px solid #F59E0B;">
<h4 style= color:{COR_PRIMARIA};>
📦 Qtd Vendida
</h4>
<h2 style="color:#F59E0B;">
{quantidade_fmt}
</h2>
</div>
""", unsafe_allow_html=True)

col4.markdown(f"""
<div style="
background:#F5F3FF;
padding:15px;
border-radius:10px;
text-align:center;
border-left:5px solid #8B5CF6;">
<h4 style= color:{COR_PRIMARIA};>
🎯 Ticket Médio
</h4>
<h2 style="color:#8B5CF6;">
{ticket_fmt}
</h2>
</div>
""", unsafe_allow_html=True)

# ==========================================
# EVOLUÇÃO MENSAL
# ==========================================

st.subheader('Evolução Mensal')

# ORDEM DOS MESES

ordem_meses = {
    'Janeiro': 1,
    'Fevereiro': 2,
    'Março': 3,
    'Abril': 4,
    'Maio': 5,
    'Junho': 6,
    'Julho': 7,
    'Agosto': 8,
    'Setembro': 9,
    'Outubro': 10,
    'Novembro': 11,
    'Dezembro': 12
}

# MAPEAR ORDEM

df_filtrado['ordem_mes'] = (
    df_filtrado['nome_mes']
    .map(ordem_meses)
)

# AGRUPAR DADOS

vendas_mes = (
    df_filtrado.groupby(
        ['ano', 'ordem_mes', 'nome_mes']
    )['faturamento']
    .sum()
    .reset_index()
)

# ORDENAR

vendas_mes = vendas_mes.sort_values(
    ['ano', 'ordem_mes']
)

# CRIAR COLUNA ANO/MÊS

vendas_mes['ano_mes'] = (
    vendas_mes['nome_mes']
    + '/'
    + vendas_mes['ano'].astype(str)
)
# ==========================================
# EVOLUÇÃO MENSAL
# ==========================================

st.subheader('📈 Evolução Mensal')

# FORMATAR VALORES

vendas_mes['faturamento_label'] = (
    vendas_mes['faturamento']
    .apply(moeda_br)
)

# CRIAR GRÁFICO

grafico_linha = px.line(
    vendas_mes,
    x='ano_mes',
    y='faturamento',
    markers=True
)

# ESTILO DA LINHA

grafico_linha.update_traces(

    line=dict(
        color=COR_PRIMARIA,
        width=4
    ),

    marker=dict(
        color=COR_PRIMARIA,
        size=8
    ),

    text=vendas_mes['faturamento_label'],

    textposition='top center',

    textfont=dict(
        color='#1F2937',
        size=11
    ),

    hovertemplate=
    '<b>%{x}</b><br>' +
    'Faturamento: %{text}<extra></extra>'
)

# LAYOUT

grafico_linha.update_layout(

    title=dict(
        text='Faturamento Mensal',
        x=0.02,
        font=dict(
            size=20,
            color='#111827'
        )
    ),

    paper_bgcolor='white',

    plot_bgcolor='white',

    font=dict(
        family='Segoe UI',
        size=12,
        color='#111827'
    ),

    xaxis=dict(
        title='Mês/Ano',

        title_font=dict(
            color='#111827'
        ),

        tickfont=dict(
            color='#111827',
            size=11
        ),

        showgrid=False,

        tickangle=-45
    ),

    yaxis=dict(
        title='Faturamento',

        title_font=dict(
            color='#111827'
        ),

        tickfont=dict(
            color='#111827',
            size=11
        ),

        showgrid=True,

        gridcolor='#E5E7EB',

        zeroline=False
    ),

    hovermode='x unified',

    hoverlabel=dict(
        bgcolor='white',
        font_color='#111827',
        font_size=12
    ),

    margin=dict(
        l=30,
        r=30,
        t=60,
        b=30
    ),

    showlegend=False
)

# EXIBIR

st.plotly_chart(
    grafico_linha,
    width='stretch',
    key='grafico_linha'
)


# FUNÇÃO POWER BI #
def aplicar_layout_powerbi(fig):

    fig.update_layout(

        paper_bgcolor='white',
        plot_bgcolor='white',

        font=dict(
            family='Segoe UI',
            size=12,
            color='#111827'
        ),

        title_font=dict(
            size=18,
            color='#111827'
        ),

        xaxis=dict(
            title_font=dict(
                color='#111827'
            ),
            tickfont=dict(
                color='#111827'
            ),
            showgrid=False
        ),

        yaxis=dict(
            title_font=dict(
                color='#111827'
            ),
            tickfont=dict(
                color='#111827'
            ),
            gridcolor='#E5E7EB',
            zeroline=False
        ),

        hoverlabel=dict(
            bgcolor='white',
            font_color='#111827'
        )
    )

    fig.update_traces(

        textfont=dict(
            color='#111827',
            size=11
        )
    )

    return fig

# ==========================================
# TOP VENDEDORES
# ==========================================

st.subheader('Top 10 Vendedores')

# AGRUPAR DADOS

top_vendedores = (
    df_filtrado.groupby('nome_vendedor')['faturamento']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

# FORMATAR MOEDA BR

top_vendedores['faturamento_formatado'] = (
    top_vendedores['faturamento']
    .apply(moeda_br)
)

# GRÁFICO

grafico_barra = px.bar(
    
    top_vendedores,

    x='nome_vendedor',

    y='faturamento',

    color_discrete_sequence=[COR_TERCIARIA],

    text='faturamento_formatado',

    title='Top 10 Vendedores',

    hover_data={
        'faturamento': False,
        'faturamento_formatado': False
    }
    
)

# HOVER CUSTOMIZADO

grafico_barra.update_traces(

    textposition='outside',

    hovertemplate=
    '<b>Vendedor</b>: %{x}<br>' +
    '<b>Faturamento</b>: %{text}<extra></extra>'
)

# LAYOUT

grafico_barra.update_layout(

    xaxis_title='Vendedor',

    yaxis_title='Faturamento'
)

# EXIBIR
grafico_barra = aplicar_layout_powerbi(
    grafico_barra
)

st.plotly_chart(
    grafico_barra,
    width='stretch',
    key='grafico_vendedores'
)
# ==========================================
# FATURAMENTO POR ESTADO
# ==========================================

st.subheader('Faturamento por Estado')

regioes = (
    df_filtrado.groupby('estado')['faturamento']
    .sum()
    .reset_index()
    .sort_values(
        by='faturamento',
        ascending=False
    )
)

# FORMATAR MOEDA BR

regioes['faturamento_formatado'] = (
    regioes['faturamento']
    .apply(moeda_br)
)

# GRÁFICO

grafico_estado = px.bar(

    regioes,

    x='estado',

    y='faturamento',

    color_discrete_sequence=[COR_SECUNDARIA],

    text='faturamento_formatado',

    title='Faturamento por Estado',

    hover_data={
        'faturamento': False,
        'faturamento_formatado': False
    }
)

# HOVER CUSTOMIZADO

grafico_estado.update_traces(

    textposition='outside',

    hovertemplate=
    '<b>Estado</b>: %{x}<br>' +
    '<b>Faturamento</b>: %{text}<extra></extra>'
)

# LAYOUT

grafico_estado.update_layout(

    xaxis_title='Estado',

    yaxis_title='Faturamento',

    uniformtext_minsize=8,

    uniformtext_mode='hide'
)

# EXIBIR
grafico_estado = aplicar_layout_powerbi(
    grafico_estado
)

st.plotly_chart(
    grafico_estado,
    width='stretch',
    key='grafico_estado'
)

# ==========================================
# PRODUTOS MAIS VENDIDOS
# ==========================================

st.subheader('Produtos Mais Vendidos')

produtos = (
    df_filtrado.groupby('nome_produto')['faturamento']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

# FORMATAR MOEDA BR

produtos['faturamento_formatado'] = (
    produtos['faturamento']
    .apply(moeda_br)
)

# GRÁFICO

grafico_produtos = px.bar(

    produtos,

    x='nome_produto',

    y='faturamento',

    color_discrete_sequence=[COR_DESTAQUE],

    text='faturamento_formatado',

    title='Top Produtos',

    hover_data={
        'faturamento': False,
        'faturamento_formatado': False
    }
)

# HOVER CUSTOMIZADO

grafico_produtos.update_traces(

    textposition='outside',

    hovertemplate=
    '<b>Produto</b>: %{x}<br>' +
    '<b>Faturamento</b>: %{text}<extra></extra>'
)

# LAYOUT

grafico_produtos.update_layout(

    xaxis_title='Produto',

    yaxis_title='Faturamento'
)

# EXIBIR
grafico_produtos = aplicar_layout_powerbi(
    grafico_produtos
)

st.plotly_chart(
    grafico_produtos,
    width='stretch',
    key='grafico_produtos'
)

# ==========================================
# DEVOLUÇÕES
# ==========================================

st.subheader('Devoluções por Motivo')

query_devolucao = """

SELECT

    d.motivo_devolucao,

    sum(d.quantidade) AS qtd_devolucoes,

	count(d.quantidade) as qtd_total_dev,

    SUM(d.valor_devolvido) AS valor_devolvido
	
FROM Fato_Devolucao d

INNER JOIN Dim_Produto p
ON d.id_produto = p.id_produto

GROUP BY
    d.motivo_devolucao

ORDER BY
    COUNT(*) DESC

"""

df_devolucao = pd.read_sql(
    query_devolucao,
    engine_postgres
)

# FORMATAR MOEDA BR

df_devolucao['valor_formatado'] = (
    df_devolucao['valor_devolvido']
    .apply(moeda_br)
)

# FORMATAR QUANTIDADE

df_devolucao['qtd_formatada'] = (
    df_devolucao['qtd_total_dev']
    .apply(
        lambda x: f'{x:,.0f}'.replace(',', '.')
    )
)

# GRÁFICO

grafico_devolucao = px.bar(

    df_devolucao,

    x='motivo_devolucao',

    y='qtd_total_dev',

    color_discrete_sequence=[COR_ERRO],

    text='qtd_formatada',

    title='Quantidade de Devoluções por Motivo',

    hover_data={
        'valor_devolvido': False,
        'valor_formatado': False,
        'qtd_formatada': False
    }
)

# HOVER CUSTOMIZADO

grafico_devolucao.update_traces(

    textposition='outside',

    hovertemplate=
    '<b>Motivo</b>: %{x}<br>' +
    '<b>Qtd Devoluções</b>: %{y}<br>' +
    '<b>Valor Devolvido</b>: %{customdata[1]}<extra></extra>'
)

# CUSTOM DATA

grafico_devolucao.update_traces(
    customdata=df_devolucao[
        ['qtd_total_dev', 'valor_formatado']
    ]
)

# LAYOUT

grafico_devolucao.update_layout(

    xaxis_title='Motivo das Devoluções',

    yaxis_title='Qtd de Devoluções'
)

# EXIBIR
grafico_devolucao = aplicar_layout_powerbi(
    grafico_devolucao
)

st.plotly_chart(
    grafico_devolucao,
    width='stretch',
    key='grafico_devolucao'
)


# ==========================================
# ESTOQUE
# ==========================================

st.subheader('Top Produtos em Estoque')

query_estoque = """
SELECT *
FROM vw_estoque
"""

df_estoque = pd.read_sql(
    query_estoque,
    engine_postgres
)

# TOP ESTOQUE

estoque_top = (
    df_estoque
    .sort_values(
        by='estoque_total',
        ascending=False
    )
    .head(10)
)

# FORMATAR ESTOQUE

estoque_top['estoque_formatado'] = (
    estoque_top['estoque_total']
    .apply(
        lambda x: f'{x:,.0f}'
        .replace(',', '.')
    )
)

# FORMATAR CUSTO

estoque_top['custo_formatado'] = (
    estoque_top['custo_estoque']
    .apply(moeda_br)
)

# GRÁFICO

grafico_estoque = px.bar(

    estoque_top,

    x='nome_produto',

    y='estoque_total',

    color_discrete_sequence=[COR_ALERTA],

    text='estoque_formatado',

    title='Top Produtos em Estoque',

    hover_data={
        'estoque_total': False,
        'custo_estoque': False,
        'estoque_formatado': False,
        'custo_formatado': False
    }
)

# HOVER CUSTOMIZADO

grafico_estoque.update_traces(

    textposition='outside',

    hovertemplate=
    '<b>Produto</b>: %{x}<br>' +
    '<b>Qtd Estoque</b>: %{text}<br>' +
    '<b>Custo Estoque</b>: %{customdata[0]}<extra></extra>'
)

# CUSTOM DATA

grafico_estoque.update_traces(
    customdata=estoque_top[
        ['custo_formatado']
    ]
)

# LAYOUT

grafico_estoque.update_layout(

    xaxis_title='Produto',

    yaxis_title='Quantidade Estoque'
)

# EXIBIR
grafico_estoque = aplicar_layout_powerbi(
    grafico_estoque
)

st.plotly_chart(
    grafico_estoque,
    width='stretch',
    key='grafico_estoque'
)