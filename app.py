import streamlit as st
import numpy as np

# ================= CONFIG =================
st.set_page_config(page_title="Laboratório IFRJ", layout="wide")

# ================= LOGIN =================
USUARIOS = {
    "raphael": "1234",
    "aluno1": "1111",
    "aluno2": "2222"
}

if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:

    st.title("🔐 Login - Laboratório IFRJ")

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if usuario in USUARIOS and USUARIOS[usuario] == senha:
            st.session_state["logado"] = True
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos")

    st.stop()

# ================= CABEÇALHO =================
st.title("🧪 Laboratório Virtual de Resíduos IFRJ")

st.markdown("""
### 👩‍🏫 Luciana Oliveira de Albuquerque  
### 👨‍🎓 Raphael Oliveira de Albuquerque
""")

st.success("Sistema ativo 🚀")

# ================= AMOSTRA =================
st.header("🧪 Dados da Amostra")

amostra = st.number_input("Volume da Amostra (mL)", value=500.0)

# ================= ST =================
st.subheader("ST - Sólidos Totais")
st1 = st.number_input("ST1")
st2 = st.number_input("ST2")
st3 = st.number_input("ST3")
st4 = st.number_input("ST4")

# ================= STF =================
st.subheader("STF - Sólidos Totais Fixos")
stf1 = st.number_input("STF1")
stf2 = st.number_input("STF2")
stf3 = st.number_input("STF3")
stf4 = st.number_input("STF4")

# ================= SST =================
st.subheader("SST - Sólidos Suspensos Totais")
sst1 = st.number_input("SST1")
sst2 = st.number_input("SST2")
sst3 = st.number_input("SST3")
sst4 = st.number_input("SST4")

# ================= SSF =================
st.subheader("SSF - Sólidos Suspensos Fixos")
ssf1 = st.number_input("SSF1")
ssf2 = st.number_input("SSF2")
ssf3 = st.number_input("SSF3")
ssf4 = st.number_input("SSF4")

# ================= CÁLCULO =================
if st.button("🧪 Gerar Laudo Completo"):

    ST = np.array([st1, st2, st3, st4])
    STF = np.array([stf1, stf2, stf3, stf4])
    SST = np.array([sst1, sst2, sst3, sst4])
    SSF = np.array([ssf1, ssf2, ssf3, ssf4])

    # ===== DERIVADOS =====
    STV = ST - STF
    SSV = SST - SSF
    SDT = ST - SST
    SDV = STV - SSV
    SDF = STF - SSF

    # ================= LAUDO COMPLETO =================
    resultados = {
        "AMOSTRA (mL)": amostra,

        "SL - Sólidos Totais Gerais": np.mean(ST),
        "ST - Sólidos Totais": np.mean(ST),
        "STF - Sólidos Totais Fixos": np.mean(STF),
        "SST - Sólidos Suspensos Totais": np.mean(SST),
        "SSF - Sólidos Suspensos Fixos": np.mean(SSF),

        "STV - Sólidos Totais Voláteis": np.mean(STV),
        "SSV - Sólidos Suspensos Voláteis": np.mean(SSV),
        "SDT - Sólidos Dissolvidos Totais": np.mean(SDT),
        "SDV - Sólidos Dissolvidos Voláteis": np.mean(SDV),
        "SDF - Sólidos Dissolvidos Fixos": np.mean(SDF),
    }

    st.session_state["resultados"] = resultados
    st.success("✔ Laudo completo gerado!")

# ================= LAUDO FINAL =================
st.header("📄 Laudo Técnico Final")

if "resultados" in st.session_state:

    for k, v in st.session_state["resultados"].items():
        st.write(f"**{k}** → {v:.2f}")

else:
    st.info("Execute o laboratório primeiro")
