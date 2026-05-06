import streamlit as st
import numpy as np
from datetime import datetime

# ================= CONFIG =================
st.set_page_config(
    page_title="Laboratório Virtual de Resíduos IFRJ",
    layout="wide"
)

# ================= ESTILO =================
st.markdown("""
    <style>
    .main {
        background-color: #f4f7ff;
    }

    h1 {
        color: #1f4e79;
    }

    .stButton > button {
        background-color: #1f4e79;
        color: white;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ================= CABEÇALHO =================
st.title("🧪 Laboratório Virtual de Resíduos – IFRJ")
st.subheader("Laudo Técnico de Ensaios Físico-Químicos")

# 👉 AJUSTE FEITO AQUI (somente nome da dona)
st.markdown("""
### 👩‍🏫 Responsável e Proprietária do Sistema
**Luciana Oliveira de Albuquerque**
""")

st.success("Sistema ativo 🚀")

# ================= MENU =================
menu = st.sidebar.selectbox(
    "📚 Menu",
    ["Início", "Aula Teórica", "Laboratório", "Laudo Final"]
)

# ================= INÍCIO =================
if menu == "Início":
    st.info("Sistema de estudo de análises físico-químicas.")

# ================= AULA TEÓRICA =================
elif menu == "Aula Teórica":
    st.write("""
    Parâmetros:
    - ST
    - STF
    - SST
    - SSF
    """)

# ================= LABORATÓRIO =================
elif menu == "Laboratório":

    st.header("🧪 Inserção de Dados")

    volume = st.number_input("Volume (mL)", value=500.0)

    st.subheader("ST")
    st1 = st.number_input("ST1")
    st2 = st.number_input("ST2")
    st3 = st.number_input("ST3")
    st4 = st.number_input("ST4")

    st.subheader("STF")
    f1 = st.number_input("STF1")
    f2 = st.number_input("STF2")
    f3 = st.number_input("STF3")
    f4 = st.number_input("STF4")

    st.subheader("SST")
    sst1 = st.number_input("SST1")
    sst2 = st.number_input("SST2")
    sst3 = st.number_input("SST3")
    sst4 = st.number_input("SST4")

    st.subheader("SSF")
    ssf1 = st.number_input("SSF1")
    ssf2 = st.number_input("SSF2")
    ssf3 = st.number_input("SSF3")
    ssf4 = st.number_input("SSF4")

    if st.button("Gerar Resultados"):

        ST = np.array([st1, st2, st3, st4])
        STF = np.array([f1, f2, f3, f4])
        SST = np.array([sst1, sst2, sst3, sst4])
        SSF = np.array([ssf1, ssf2, ssf3, ssf4])

        STV = ST - STF
        SSV = SST - SSF
        SDT = ST - SST
        SDF = STF - SSF
        SDV = STV - SSV

        resultados = {
            "ST": (np.mean(ST), np.std(ST)),
            "STF": (np.mean(STF), np.std(STF)),
            "SST": (np.mean(SST), np.std(SST)),
            "SSF": (np.mean(SSF), np.std(SSF))
        }

        st.session_state["resultados"] = resultados
        st.success("Cálculos concluídos!")

# ================= LAUDO =================
elif menu == "Laudo Final":

    st.header("📄 Laudo Técnico")

    if "resultados" in st.session_state:

        for k, v in st.session_state["resultados"].items():
            media, dp = v
            st.write(f"{k} → {media:.2f} ± {dp:.2f}")

    else:
        st.warning("Primeiro faça os cálculos no laboratório")
