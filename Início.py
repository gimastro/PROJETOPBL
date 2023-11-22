import pandas as pd
import streamlit as st


# Header - titulo
st.header("PBL GRUPO 8")



# dividindo o espaçamento da tela em colunas
left_col, cent_col, last_col = st.columns(3)
with left_col:
    input = st.text_input('Pesquisa')
    st.button("Pesquisar")


# Texto introdutório
st.markdown("Digite o nome ou código da bactéria.")

