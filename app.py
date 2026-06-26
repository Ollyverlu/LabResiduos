import streamlit as st
import numpy as np

# ================= CONFIG =================
st.set_page_config(page_title="Lab IFRJ", layout="wide")

# ================= CSS =================
st.markdown("""
<style>
.stApp { background-color: #e8f5e9; }

h1 { color: #1b5e20 !important; font-weight: 900; }

.card {
    background:white;
    padding:15px;
    border-left:6px solid #2e7d32;
    border-radius:10px;
    margin-top:10px;
}

.stButton>button {
    background:#2e7d32;
    color:white;
    width:100%;
    height:50px;
}
</style>
""", unsafe_allow_html=True)

# ================= CABEÇALHO =================
col1, col2 = st.columns([1,5])

with col1:
    st.image("logo.png", width=100)

with col2:
    st.title("LABRESÍDUOS IFRJ - CEMMA")
    st.markdown("""
    ### Criado por: Luciana Oliveira de Albuquerque  
    ### Professor: Renato Ribeiro  
    ### Admin: Raphael Oliveira de Albuquerque  
    """)

st.markdown("---")

# ================= MENU =================
menu = st.sidebar.radio("Menu", [
    "Início",
    "Sólidos Totais",
    "Sólidos Suspensos",
    "N-Amoniacal",
    "NTK",
    "NHX",
    "DQO"
])

# ================= INÍCIO =================
if menu == "Início":
    st.title("Sistema IFRJ")
    st.info("Selecione um módulo")

# ================= FUNÇÃO PADRÃO =================
def cabecalho_titulo(titulo):
    st.title(f"DETERMINAÇÃO DE {titulo}")

    col1, col2 = st.columns(4)
    with col1:
        st.text_input("Responsável")
    with col2:
        st.text_input("Projeto")
    with st.columns(4)[2]:
        st.date_input("Data da Análise")
    with st.columns(4)[3]:
        st.time_input("Hora da Análise")

    st.markdown("---")

# ================= SÓLIDOS TOTAIS =================
elif menu == "Sólidos Totais":
    cabecalho_titulo("SÓLIDOS TOTAIS")

    v = st.number_input("Volume", 0.0)

    a = st.number_input("m1")
    b = st.number_input("m2")
    c = st.number_input("m3")

    if st.button("Calcular"):
        fator = 1000 / (v / 1000)
        st.success((b-a)*fator)

# ================= SÓLIDOS SUSPENSOS =================
elif menu == "Sólidos Suspensos":
    cabecalho_titulo("SÓLIDOS SUSPENSOS")

    v = st.number_input("Volume", 0.0)

    a = st.number_input("m1")
    b = st.number_input("m2")
    c = st.number_input("m3")

    if st.button("Calcular"):
        fator = 1000 / (v / 1000)
        st.success((b-a)*fator)

# ================= N-AMONIACAL =================
elif menu == "N-Amoniacal":
    cabecalho_titulo("NITROGÊNIO AMONIACAL")

    m = st.number_input("Massa")
    v = st.number_input("Volume")

    t1 = st.number_input("T1")
    t2 = st.number_input("T2")
    t3 = st.number_input("T3")

    if st.button("Calcular"):
        media = np.mean([t1,t2,t3])
        st.success((m/381.4)/(v/1000)*(v/media))

# ================= NTK =================
elif menu == "NTK":
    cabecalho_titulo("NITROGÊNIO TOTAL KJELDAHL")

    m = st.number_input("Massa")
    v = st.number_input("Volume")

    t1 = st.number_input("T1")
    t2 = st.number_input("T2")
    t3 = st.number_input("T3")

    if st.button("Calcular"):
        media = np.mean([t1,t2,t3])
        st.success((m/381.4)/(v/1000)*(v/media))

# ================= NHX =================
elif menu == "NHX":
    cabecalho_titulo("NITROGÊNIO NHX")

    m = st.number_input("Massa")
    v = st.number_input("Volume")

    t1 = st.number_input("T1")
    t2 = st.number_input("T2")
    t3 = st.number_input("T3")

    if st.button("Calcular"):
        media = np.mean([t1,t2,t3])
        st.success((m/381.4)/(v/1000)*(v/media))

# ================= DQO =================
elif menu == "DQO":
    cabecalho_titulo("DEMANDA QUÍMICA DE OXIGÊNIO")

    m = st.number_input("Massa padrão")
    v = st.number_input("Volume amostra")

    t1 = st.number_input("T1")
    t2 = st.number_input("T2")
    t3 = st.number_input("T3")

    if st.button("Calcular"):
        media = np.mean([t1,t2,t3])
        st.success((m*0.25)/(media+0.0001))
