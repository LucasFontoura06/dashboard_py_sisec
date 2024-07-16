import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Configurando a largura da página
st.set_page_config(layout="wide")

# Definindo os dados
data = {
    "Mês": ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"],
    "2023_PI_Empresas": [0, 0, 0, 0, 0, 3, 6, 0, 2, 1, 0, 0],
    "2023_PI_Entes": [0, 0, 0, 0, 1, 6, 2, 0, 2, 5, 1, 0],
    "2023_PI_Est_Munic": [0, 0, 0, 0, 4, 3, 3, 2, 4, 4, 3, 1],
    "2023_ACT": [0, 0, 0, 0, 2, 2, 0, 1, 0, 2, 0, 0],
    "2024_PI_Empresas": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "2024_PI_Entes": [0, 2, 2, 2, 0, 2, 1, 0, 0, 0, 0, 0],
    "2024_PI_Est_Munic": [0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    "2024_ACT": [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "2025_PI_Empresas": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "2025_PI_Entes": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "2025_PI_Est_Munic": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "2025_ACT": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "2026_PI_Empresas": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "2026_PI_Entes": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "2026_PI_Est_Munic": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "2026_ACT": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

# Criando o DataFrame
df = pd.DataFrame(data)

# Criando a interface do Streamlit
st.markdown("<h1 style='text-align: center;'>Dashboard Controle De Instrumentos Jurídicos - ACT e PI - DAIT</h1>", unsafe_allow_html=True)

# Opções de filtro
anos = ["2023", "2024", "2025", "2026"]
categorias = ["PI_Empresas", "PI_Entes", "PI_Est_Munic", "ACT"]
meses = df["Mês"].tolist()

# Selecionar anos, meses e categorias
with st.sidebar:
    st.header("Filtros")
    anos_selecionados = st.multiselect("Selecione os anos", anos, default=anos)
    meses_selecionados = st.multiselect("Selecione os meses", meses, default=meses)
    categorias_selecionadas = st.multiselect("Selecione as categorias", categorias, default=categorias)

# Filtrando os dados
colunas_selecionadas = ["Mês"] + [f"{ano}_{categoria}" for ano in anos_selecionados for categoria in categorias_selecionadas]
df_filtrado = df[df["Mês"].isin(meses_selecionados)][colunas_selecionadas]

# Criando os gráficos
fig1, ax1 = plt.subplots(figsize=(18, 10))
for coluna in colunas_selecionadas[1:]:
    ax1.plot(df_filtrado["Mês"], df_filtrado[coluna], marker='o', label=coluna)
ax1.set_title("Número de Instrumentos por Mês")
ax1.set_xlabel("Mês")
ax1.set_ylabel("Quantidade")
ax1.legend()
ax1.set_facecolor('white')

fig2, ax2 = plt.subplots(figsize=(18, 10))
bar_width = 0.2
index = range(len(df_filtrado["Mês"]))
for i, coluna in enumerate(colunas_selecionadas[1:]):
    ax2.bar([p + bar_width * i for p in index], df_filtrado[coluna], bar_width, label=coluna)
ax2.set_title("Número de Instrumentos por Mês (Gráfico de Barras)")
ax2.set_xlabel("Mês")
ax2.set_ylabel("Quantidade")
ax2.set_xticks([p + bar_width * (len(colunas_selecionadas[1:]) - 1) / 2 for p in index])
ax2.set_xticklabels(df_filtrado["Mês"])
ax2.legend()
ax2.set_facecolor('white')

fig3, ax3 = plt.subplots(figsize=(18, 10))
df_sum = df_filtrado[colunas_selecionadas[1:]].sum()
ax3.pie(df_sum, labels=colunas_selecionadas[1:], autopct='%1.1f%%', startangle=90)
ax3.set_title("Distribuição de Instrumentos por Categoria")

fig4, ax4 = plt.subplots(figsize=(18, 10))
for coluna in colunas_selecionadas[1:]:
    ax4.fill_between(df_filtrado["Mês"], df_filtrado[coluna], alpha=0.5, label=coluna)
ax4.set_title("Número de Instrumentos por Mês (Gráfico de Área)")
ax4.set_xlabel("Mês")
ax4.set_ylabel("Quantidade")
ax4.legend()
ax4.set_facecolor('white')

# Exibindo os gráficos
st.write("### Gráficos")

# Dividindo a tela para os gráficos
col1, col2 = st.columns(2)

with col1:
    st.pyplot(fig1)
    st.pyplot(fig3)

with col2:
    st.pyplot(fig2)
    st.pyplot(fig4)
