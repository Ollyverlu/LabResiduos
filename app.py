import streamlit as st
import numpy as np

# ================= CONFIG =================
st.set_page_config(
    page_title="LabResíduos IFRJ - CEMMA",
    layout="wide"
)

# ================= ESTILO PROFISSIONAL =================
st.markdown("""
<style>

.stApp {
    background-color: #e8f5e9;
}

/* CABEÇALHO */
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

# ================= INÍCIO =================
if menu == "🏠 Início":
    st.title("Bem-vindo ao Sistema IFRJ")
    st.info("Selecione um módulo no menu lateral.")

# ================= SÓLIDOS TOTAIS =================
elif menu == "🧪 Sólidos Totais":

    st.title("Sólidos Totais")

    volume = st.number_input("Alíquota (mL)", value=50.0)

    m1 = st.number_input("m1", value=0.0)
    m2 = st.number_input("m2", value=0.0)
    m3 = st.number_input("m3", value=0.0)

    m1_2 = st.number_input("m1'", value=0.0)
    m2_2 = st.number_input("m2'", value=0.0)
    m3_2 = st.number_input("m3'", value=0.0)

    if st.button("GERAR RESULTADO"):

        fator = 1000 / (volume / 1000)

        ST1 = (m2 - m1) * fator
        ST2 = (m2_2 - m1_2) * fator

        STF1 = (m3 - m1) * fator
        STF2 = (m3_2 - m1_2) * fator

        STV1 = ST1 - STF1
        STV2 = ST2 - STF2

        st.session_state["st"] = {
            "ST": (np.mean([ST1, ST2]), np.std([ST1, ST2], ddof=1)),
            "STF": (np.mean([STF1, STF2]), np.std([STF1, STF2], ddof=1)),
            "STV": (np.mean([STV1, STV2]), np.std([STV1, STV2], ddof=1))
        }

    if "st" in st.session_state:
        for k, (m, d) in st.session_state["st"].items():
            st.markdown(f"<div class='card'><b>{k}</b><br>{m:.2f} ± {d:.2f}</div>", unsafe_allow_html=True)

# ================= SÓLIDOS SUSPENSOS =================
elif menu == "🧪 Sólidos Suspensos":
    st.title("Sólidos Suspensos")
    st.info("Mesmo modelo dos Sólidos Totais.")

# ================= N-AMONIACAL =================
elif menu == "🧪 N-Amoniacal":
    st.title("N-Amoniacal")
    st.info("Módulo em desenvolvimento.")

# ================= NTK =================
elif menu == "🧪 NTK":

    st.title("DETERMINAÇÃO DE NTK")

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

    if "ntk" in st.session_state:
        for k, v in st.session_state["ntk"].items():
            st.markdown(f"<div class='card'><b>{k}</b><br>{v:.4f}</div>", unsafe_allow_html=True)

# ================= NHX =================
elif menu == "🧪 NHX":

    st.title("DETERMINAÇÃO DE NHX")

    massa = st.number_input("Massa (g)", value=0.0, key="nhx_massa")
    volume_balao = st.number_input("Volume balão (mL)", value=100.0, key="nhx_vol")

    v1 = st.number_input("1ª titulação", value=0.0, key="nhx_v1")
    v2 = st.number_input("2ª titulação", value=0.0, key="nhx_v2")
    v3 = st.number_input("3ª titulação", value=0.0, key="nhx_v3")

    if st.button("CALCULAR NHX"):

        media = np.mean([v1, v2, v3])
        dp = np.std([v1, v2, v3], ddof=1)

        conc = (massa / 381.40) / (volume_balao / 1000)
        real = conc * volume_balao / media if media != 0 else 0

        st.session_state["nhx"] = {
            "Concentração": conc,
            "Real": real,
            "Média": media,
            "DP": dp
        }

    if "nhx" in st.session_state:
        for k, v in st.session_state["nhx"].items():
            st.markdown(f"<div class='card'><b>{k}</b><br>{v:.4f}</div>", unsafe_allow_html=True)

# ================= DQO (NOVO - IGUAL EXCEL QUE VOCÊ MANDOU) =================
elif menu == "🧪 DQO":

    st.title("DETERMINAÇÃO DE DEMANDA QUÍMICA DE OXIGÊNIO")

    st.markdown("### PADRONIZAÇÃO DO SFA 0,25N")

    massa = st.number_input("Massa (g) K2Cr2O7", value=12.4556)
    massa_molar = 294.18
    volume_balao = st.number_input("Volume balão (mL)", value=1000.0)

    aliquota = st.number_input("Volume da alíquota (mL)", value=0.0)

    v1 = st.number_input("1ª titulação (mL)", value=0.0)
    v2 = st.number_input("2ª titulação (mL)", value=0.0)
    v3 = st.number_input("3ª titulação (mL)", value=0.0)

    if st.button("CALCULAR DQO"):

        media = np.mean([v1, v2, v3])
        dp = np.std([v1, v2, v3], ddof=1)

        conc_padrao = (massa / massa_molar) / (volume_balao / 1000)

        real = conc_padrao * volume_balao / media if media != 0 else 0

        st.session_state["dqo"] = {
            "Concentração padrão": conc_padrao,
            "Concentração real": real,
            "Média": media,
            "DP": dp
        }

    if "dqo" in st.session_state:
        for k, v in st.session_state["dqo"].items():
            st.markdown(f"<div class='card'><b>{k}</b><br>{v:.4f}</div>", unsafe_allow_html=True)
