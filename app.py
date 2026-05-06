import streamlit as st
import numpy as np
from datetime import datetime

# ================= USUÁRIOS =================
USUARIOS = {
    "raphael": "1234",
    "aluno1": "1111",
    "aluno2": "2222"
}

# ================= LOGIN =================
if "logado" not in st.session_state:
    st.session_state["logado"] = False
    st.session_state["usuario"] = ""

if not st.session_state["logado"]:

    st.title("🔐 Login - Laboratório IFRJ")

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):

        if usuario in USUARIOS and USUARIOS[usuario] == senha:
            st.session_state["logado"] = True
            st.session_state["usuario"] = usuario
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos")

    st.stop()

# ================= CONFIG =================
st.set_page_config(
    page_title="Laboratório Virtual IFRJ",
    layout="wide"
)

# ================= CABEÇALHO =================
st.title("🧪 Laboratório Virtual de Resíduos – IFRJ")
st.subheader("Laudo Técnico de Ensaios Físico-Químicos")

st.markdown("""
### 👩‍🏫 Luciana Oliveira de Albuquerque  
### 👨‍🎓 Raphael Oliveira de Albuquerque
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
ST, STF, SST, SSF são parâmetros usados em análises de água e resíduos.
    """)

# ================= LABORATÓRIO =================
elif menu == "Laboratório":

    st.header("🧪 Inserção de Dados")

    volume = st.number_input("Volume da amostra (mL)", value=500.0)

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

    if st.button("🧪 Gerar Resultados"):

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
            "ST": np.mean(ST),
            "STF": np.mean(STF),
            "SST": np.mean(SST),
            "SSF": np.mean(SSF),
            "STV": np.mean(STV),
            "SSV": np.mean(SSV),
            "SDT": np.mean(SDT),
            "SDF": np.mean(SDF),
            "SDV": np.mean(SDV),
        }

        st.session_state["resultados"] = resultados
        st.success("✔ Cálculos concluídos!")

# ================= LAUDO FINAL =================
elif menu == "Laudo Final":

    st.header("📄 Laudo Técnico")

    if "resultados" in st.session_state:

        for k, v in st.session_state["resultados"].items():
            st.write(f"{k} → {v:.2f}")

    else:
        st.warning("Execute o laboratório primeiro")
