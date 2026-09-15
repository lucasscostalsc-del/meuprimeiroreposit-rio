import streamlit as st
import pandas as pd
import numpy as np

st.title("Olá, Mundo!")


with st.sidebar:
 st.header("Sobre o App")
 st.write("Meu primeiro projeto com Streamlit")

st.write(" Se você está vendo isso, é porque deu certo!")

st.header("Isso é um divisor", divider="rainbow")

st.markdown("Isso foi criado usando st.markdown")


st.subheader("st.column")
col1, col2 = st.columns(2)

with col1:
 x = st.slider("Escolha um valor", 1, 10)
with col2:
 st.write(f"Você escolheu o valor:blue [***x***] é {x}")


st.subheader("st.line_chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)

