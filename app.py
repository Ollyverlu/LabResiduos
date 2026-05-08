import streamlit as st
import numpy as np

# ================= CONFIG =================
st.set_page_config(
    page_title="Laboratório Virtual CMMA IFRJ",
    layout="wide"
)

# ================= CABEÇALHO =================
st.title("🧪 Laboratório Virtual CMMA – IFRJ")
st.subheader("Laudo Técnico de Ensaios Físico-Químicos")

st.markdown("""
### 👩‍🏫 Criador
Luciana Oliveira de Albuquerque

### 🎓 Administrador
Raphael Oliveira de Albuquerque
""")

st.success("Sistema ativo 🚀")

# ================= MENU =================
menu = st.sidebar.selectbox(
    "📚 Menu do Sistema",
    ["Início", "Laboratório", "Laudo Final"]
)

# ================= INÍCIO =================
if menu == "Início":
    st.markdown("## 👩‍🔬 Bem-vinda ao Laboratório Virtual CMMA")

# ================= LABORATÓRIO =================
elif menu == "Laboratório":

    st.header("🧪 Dados Inseridos")

    volume = st.number_input("Alíquota (mL)", value=500.0)

    st.markdown("### 📥 2 medições")
    st.write("Casarola")

    st.subheader("Massas Experimentais")

    # ===== REPLICA 1 =====
    st.markdown("### 🔹 1ª medição")

    m1 = st.number_input("m1 (massa da caçarola)", key="m1")
    m2 = st.number_input("m2 (caçarola + ST)", key="m2")
    m3 = st.number_input("m3 (caçarola + STF)", key="m3")

    # ===== REPLICA 2 =====
    st.markdown("### 🔹 2ª medição")

    m1_l = st.number_input("m1'", key="m1l")
    m2_l = st.number_input("m2'", key="m2l")
    m3_l = st.number_input("m3'", key="m3l")

    if st.button("🧪 GERAR RESULTADOS"):

        # ================= FÓRMULAS (IGUAL DA FOLHA) =================

        # ST
        ST1 = (m2 - m1) * 1e6 / volume
        ST2 = (m2_l - m1_l) * 1e6 / volume
        ST = (ST1 + ST2) / 2

        # STF
        STF1 = (m3 - m1) * 1e6 / volume
        STF2 = (m3_l - m1_l) * 1e6 / volume
        STF = (STF1 + STF2) / 2

        # STV
        STV1 = ST1 - STF1
        STV2 = ST2 - STF2
        STV = (STV1 + STV2) / 2

        resultados = {
            "ST": ST,
            "STF": STF,
            "STV": STV
        }

        st.session_state["resultados"] = resultados

        st.success("✔ Cálculos concluídos!")

# ================= LAUDO =================
elif menu == "Laudo Final":

    st.header("📄 Laudo Final")

    if "resultados" in st.session_state:

        for k, v in st.session_state["resultados"].items():
            st.write(f"{k} = {v:.2f} mg/L")

    else:
        st.warning("⚠ Gere os dados primeiro")
