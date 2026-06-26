import streamlit as st
import numpy as np

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
    background-color: #2e7d32;
    padding: 15px;
    border-radius: 10px;
    color: white;
    margin-bottom: 15px;
}

.header h1 {
    text-align: center;
    color: white !important;
    font-size: 32px;
}

.header h3 {
    text-align: center;
    color: #f1f8e9 !important;
}

.card {
    background: white;
    padding: 15px;
    border-radius: 10px;
    border-left: 6px solid #2e7d32;
    margin-top: 10px;
}

.stButton>button {
    width: 100%;
    height: 60px;
    background-color: #2e7d32;
    color: white;
    font-weight: bold;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ================= NAVEGAÇÃO =================
if "page" not in st.session_state:
    st.session_state.page = "dashboard"

def go(page):
    st.session_state.page = page

# ================= CABEÇALHO =================
col1, col2 = st.columns([1, 4])

with col1:
    st.image("logo.png", width=110)

with col2:
    st.markdown("""
    <div class="header">
        <h1>🧪 LABRESÍDUOS - IFRJ / CEMMA</h1>
        <h3>Sistema Virtual de Análises Físico-Químicas</h3>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ================= DASHBOARD =================
if st.session_state.page == "dashboard":

    st.title("📊 Dashboard do Laboratório")

    col1, col2 = st.columns(2)

    with col1:
        st.button("Sólidos Totais", on_click=go, args=("st",))
        st.button("Sólidos Suspensos", on_click=go, args=("ss",))
        st.button("N-Amoniacal", on_click=go, args=("namo",))

    with col2:
        st.button("NTK", on_click=go, args=("ntk",))
        st.button("DQO", on_click=go, args=("dqo",))

# ================= SÓLIDOS TOTAIS =================
elif st.session_state.page == "st":

    st.title("🧪 Sólidos Totais")

    volume = st.number_input("Alíquota (mL)", value=50.0)

    m1 = st.number_input("m1", value=0.0)
    m2 = st.number_input("m2", value=0.0)
    m3 = st.number_input("m3", value=0.0)

    m1_2 = st.number_input("m1'", value=0.0)
    m2_2 = st.number_input("m2'", value=0.0)
    m3_2 = st.number_input("m3'", value=0.0)

    if st.button("GERAR ST"):

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

        st.success("✔ ST calculado!")

    if "st" in st.session_state:
        for k, (m, d) in st.session_state["st"].items():
            st.markdown(f"<div class='card'><b>{k}</b><br>{m:.2f} ± {d:.2f}</div>", unsafe_allow_html=True)

# ================= SÓLIDOS SUSPENSOS =================
elif st.session_state.page == "ss":

    st.title("🧪 Sólidos Suspensos")

    volume = st.number_input("Alíquota (mL)", value=50.0, key="ss")

    m1 = st.number_input("m1", value=0.0, key="ss1")
    m2 = st.number_input("m2", value=0.0, key="ss2")
    m3 = st.number_input("m3", value=0.0, key="ss3")

    m1_2 = st.number_input("m1'", value=0.0, key="ss4")
    m2_2 = st.number_input("m2'", value=0.0, key="ss5")
    m3_2 = st.number_input("m3'", value=0.0, key="ss6")

    if st.button("GERAR SS"):

        fator = 1000 / (volume / 1000)

        SS1 = (m2 - m1) * fator
        SS2 = (m2_2 - m1_2) * fator

        SSF1 = (m3 - m1) * fator
        SSF2 = (m3_2 - m1_2) * fator

        SSV1 = SS1 - SSF1
        SSV2 = SS2 - SSF2

        st.session_state["ss"] = {
            "SS": (np.mean([SS1, SS2]), np.std([SS1, SS2], ddof=1)),
            "SSF": (np.mean([SSF1, SSF2]), np.std([SSF1, SSF2], ddof=1)),
            "SSV": (np.mean([SSV1, SSV2]), np.std([SSV1, SSV2], ddof=1))
        }

        st.success("✔ SS calculado!")

    if "ss" in st.session_state:
        for k, (m, d) in st.session_state["ss"].items():
            st.markdown(f"<div class='card'><b>{k}</b><br>{m:.2f} ± {d:.2f}</div>", unsafe_allow_html=True)

# ================= N-AMONIACAL (EXCEL) =================
elif st.session_state.page == "namo":

    st.title("🧪 Nitrogênio Amoniacal")

    massa = st.number_input("Massa Na2B4O7·10H2O (g)", value=0.0)
    massa_molar = 381.40
    volume_balao = st.number_input("Volume do Balão (mL)", value=100.0)

    v1 = st.number_input("Titulação 1 (mL)", value=0.0)
    v2 = st.number_input("Titulação 2 (mL)", value=0.0)
    v3 = st.number_input("Titulação 3 (mL)", value=0.0)

    if st.button("CALCULAR N-AMONIACAL"):

        tit = [v1, v2, v3]

        media = np.mean(tit)
        dp = np.std(tit, ddof=1)

        mol = massa / massa_molar
        conc_padrao = mol / (volume_balao / 1000)

        conc_real = (conc_padrao * volume_balao) / media if media != 0 else 0

        rsd = (dp / media) * 100 if media != 0 else 0

        fator = conc_real / 0.02 if 0.02 != 0 else 0

        st.session_state["namo"] = {
            "Concentração Padrão": conc_padrao,
            "Concentração Real": conc_real,
            "Média Titulação": media,
            "Desvio Padrão": dp,
            "RSD (%)": rsd,
            "Fator de Correção": fator
        }

        st.success("✔ N-Amoniacal calculado!")

    if "namo" in st.session_state:
        for k, v in st.session_state["namo"].items():
            st.markdown(f"<div class='card'><b>{k}</b><br>{v:.4f}</div>", unsafe_allow_html=True)

# ================= NTK (EXCEL) =================
elif st.session_state.page == "ntk":

    st.title("🧪 Nitrogênio Total Kjeldahl (NTK)")

    massa = st.number_input("Massa Na2B4O7·10H2O (g)", value=0.0)
    volume_balao = st.number_input("Volume do Balão (mL)", value=100.0)

    v1 = st.number_input("Titulação 1 (mL)", value=0.0)
    v2 = st.number_input("Titulação 2 (mL)", value=0.0)
    v3 = st.number_input("Titulação 3 (mL)", value=0.0)

    if st.button("CALCULAR NTK"):

        tit = [v1, v2, v3]

        media = np.mean(tit)
        dp = np.std(tit, ddof=1)

        mol = massa / 381.40
        conc_padrao = mol / (volume_balao / 1000)

        conc_real = (conc_padrao * volume_balao) / media if media != 0 else 0

        rsd = (dp / media) * 100 if media != 0 else 0

        fator = conc_real / 0.02 if 0.02 != 0 else 0

        st.session_state["ntk"] = {
            "Concentração Padrão": conc_padrao,
            "Concentração Real": conc_real,
            "Média Titulação": media,
            "Desvio Padrão": dp,
            "RSD (%)": rsd,
            "Fator de Correção": fator
        }

        st.success("✔ NTK calculado!")

    if "ntk" in st.session_state:
        for k, v in st.session_state["ntk"].items():
            st.markdown(f"<div class='card'><b>{k}</b><br>{v:.4f}</div>", unsafe_allow_html=True)

# ================= DQO =================
elif st.session_state.page == "dqo":
    st.title("🧪 DQO")
    st.info("Em desenvolvimento")
