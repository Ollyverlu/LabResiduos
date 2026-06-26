import streamlit as st
import numpy as np
from datetime import datetime

# ================= CONFIG =================
st.set_page_config(
    page_title="LabResíduos IFRJ - CEMMA",
    layout="wide"
)

# ================= ESTILO =================
st.markdown("""
<style>

.stApp {
    background-color: #e8f5e9;
}

.header {
    background-color: #1b5e20;
    padding: 15px;
    border-radius: 12px;
    color: white;
    text-align: center;
}

.card {
    background: white;
    padding: 15px;
    border-radius: 12px;
    border-left: 6px solid #2e7d32;
    margin-top: 10px;
}

.stButton>button {
    width: 100%;
    height: 55px;
    background-color: #2e7d32;
    color: white;
    font-weight: bold;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ================= CABEÇALHO =================
col1, col2 = st.columns([1, 5])

with col1:
    st.image("logo.png", width=100)

with col2:
    st.markdown("""
    <div class="header">
        <h1>🧪 LABRESÍDUOS - IFRJ / CEMMA</h1>
        <h3>Sistema Virtual de Análises Físico-Químicas</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### 👩‍🏫 Criado por: Luciana Oliveira de Albuquerque  
    ### 🎓 Professor: Renato Ribeiro  
    ### 🧑‍💻 Administrador: Raphael Oliveira de Albuquerque  
    """)

st.markdown("---")

# ================= MENU =================
menu = st.sidebar.radio(
    "📊 Menu do Laboratório",
    [
        "🏠 Início",
        "🧪 Sólidos Totais",
        "🧪 Sólidos Suspensos",
        "🧪 N-Amoniacal",
        "🧪 NTK",
        "🧪 NHX",
        "🧪 DQO"
    ]
)

# ================= BARRA EXCEL (NOVO PADRÃO) =================
def cabecalho_excel():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.text_input("RESPONSÁVEL")

    with col2:
        st.text_input("PROJETO")

    with col3:
        st.date_input("DATA DA ANÁLISE")

    with col4:
        st.time_input("HORA DA ANÁLISE")

    st.markdown("---")

# ================= INÍCIO =================
if menu == "🏠 Início":
    st.title("Bem-vindo ao Sistema IFRJ")
    st.info("Selecione um módulo no menu lateral.")

# ================= SÓLIDOS TOTAIS =================
elif menu == "🧪 Sólidos Totais":
    st.title("Sólidos Totais")

    cabecalho_excel()

    volume = st.number_input("Alíquota (mL)", value=50.0)

# ================= SÓLIDOS SUSPENSOS =================
elif menu == "🧪 Sólidos Suspensos":
    st.title("Sólidos Suspensos")
    cabecalho_excel()
    st.info("Mesmo modelo dos Sólidos Totais.")

# ================= N-AMONIACAL (COM EXCEL TOP) =================
elif menu == "🧪 N-Amoniacal":

    st.title("DETERMINAÇÃO DE NITROGÊNIO AMONIACAL")

    # 🔥 NOVA BARRA TIPO PLANILHA (SEM MEXER NO RESTO)
    cabecalho_excel()

    st.markdown("### PADRONIZAÇÃO DO H₂SO₄ 0,02N")

    massa = st.number_input("Massa (g)", value=0.0)
    volume_balao = st.number_input("Volume balão (mL)", value=100.0)

    v1 = st.number_input("1ª titulação", value=0.0)
    v2 = st.number_input("2ª titulação", value=0.0)
    v3 = st.number_input("3ª titulação", value=0.0)

    if st.button("CALCULAR"):

        media = np.mean([v1, v2, v3])
        dp = np.std([v1, v2, v3], ddof=1)

        conc = (massa / 381.40) / (volume_balao / 1000)
        real = conc * volume_balao / media if media != 0 else 0

        st.session_state["namo"] = {
            "Concentração": conc,
            "Real": real,
            "Média": media,
            "DP": dp
        }

    if "namo" in st.session_state:
        for k, v in st.session_state["namo"].items():
            st.markdown(f"<div class='card'><b>{k}</b><br>{v:.4f}</div>", unsafe_allow_html=True)

# ================= NTK =================
elif menu == "🧪 NTK":
    st.title("NTK")
    cabecalho_excel()

    massa = st.number_input("Massa (g)", value=0.0)
    volume_balao = st.number_input("Volume balão (mL)", value=100.0)

    v1 = st.number_input("1ª titulação", value=0.0)
    v2 = st.number_input("2ª titulação", value=0.0)
    v3 = st.number_input("3ª titulação", value=0.0)

    if st.button("CALCULAR NTK"):

        media = np.mean([v1, v2, v3])
        dp = np.std([v1, v2, v3], ddof=1)

        conc = (massa / 381.40) / (volume_balao / 1000)
        real = conc * volume_balao / media if media != 0 else 0

        st.session_state["ntk"] = {
            "Concentração": conc,
            "Real": real,
            "Média": media,
            "DP": dp
        }

# ================= NHX =================
elif menu == "🧪 NHX":
    st.title("NHX")
    cabecalho_excel()

# ================= DQO =================
elif menu == "🧪 DQO":
    st.title("DQO")
    cabecalho_excel()
