import streamlit as st
import pandas as pd

df = pd.read_csv("dataset_sinalizacao_ferroviaria.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Filtros na Barra Lateral
st.sidebar.header("Filtros de Sinalização")

linhas_selecionadas = st.sidebar.multiselect(
    "Linha / Sinalização:",
    options=df["linha"].unique(),
    default=df["linha"].unique()
)

aspectos_selecionados = st.sidebar.multiselect(
    "Aspecto do Sinal:",
    options=df["aspecto_sinal"].unique(),
    default=df["aspecto_sinal"].unique()
)

# DataFrame Filtrado
df_filtrado = df[
    (df["linha"].isin(linhas_selecionadas)) & 
    (df["aspecto_sinal"].isin(aspectos_selecionados))
]

st.dataframe(df_filtrado)

tab1, tab2, tab3 = st.tabs(["Comparativo de Tecnologias", "Análise por Bloco", "Eventos de Parada"])

with tab1:
    st.write("**Desempenho Médio: Bloco Fixo vs CBTC**")
    media_linhas = df.groupby("linha")[["headway_seg", "velocidade_permitida_kmh"]].mean()
    st.dataframe(media_linhas)

with tab2:
    st.write("**Ocupação de Via por Bloco**")
    bloco = st.selectbox("Selecione o Bloco:", df["id_bloco"].unique())
    df_bloco = df[df["id_bloco"] == bloco]
    st.line_chart(df_bloco.set_index("timestamp")["tempo_ocupacao_circuito_seg"])

with tab3:
    st.write("**Sinais Vermelhos Registrados**")
    st.dataframe(df[df["aspecto_sinal"] == "Vermelho"])