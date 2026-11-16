import pandas as pd, openpyxl

import streamlit as st

df = pd.read_excel("pib.xlsx")
df["Data"] = df["Data"].astype(str).str[:4].str.slice(0,4)
df["ano"] = df["Data"].astype(str).str[:4]
media = df.groupby("ano")["PIB real"].mean().reset_index()
print(df)


def ler_td():
    
    df = pd.read_excel("pib.xlsx")
df["Data"] = df["Data"].astype(str).str[:4].str.slice(0,4)
df["ano"] = df["Data"].astype(str).str[:4]
media = df.groupby("ano")["PIB real"].mean().reset_index()



## --------------------------------------------------------------


st.set_page_config(
    page_title="PIB do Brasil",
    layout="wide",
    initial_sidebar_state="expanded",
)


with st.sidebar:
    st.markdown('<div class="sidebar-marca">PIB Brasileiro<br>Por anos',
                unsafe_allow_html=True)

    with st.expander("📂 Carregar planilhas", expanded=False):
        upload_111 = st.file_uploader("tabela PIB", type=["xls"])

with st.sidebar:
    st.markdown("### Escolha o que ver")
    ano = st.selectbox("Ano da pesquisa", df["ano"].iloc[::-1])
    

    st.divider()
