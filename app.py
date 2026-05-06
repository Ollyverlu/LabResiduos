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

# ================= CABEÇALHO =================
st.title("🧪 Laboratório Virtual IFRJ")

st.markdown("""
### 👩‍🏫 Luciana Oliveira de Albuquerque  
### 👨‍🎓 Raphael Oliveira de Albuquerque
""")

st.success("Sistema ativo 🚀")

# ================= LABORATÓRIO =================
st.header("🧪 Inserção de Dados")

# SL (geral)
sl1 = st.number_input("SL1 - Sólidos Totais Gerais")
sl2 = st.number_input("SL2 - Sólidos Totais Gerais")
sl3 = st.number_input("SL3 - Sólidos Totais Gerais")
sl4 = st.number_input("SL4 - Sólidos Totais Gerais")

# ST
st1 = st.number_input("ST1 - Sólidos Totais")
st2 = st.number_input("ST2 - Sólidos Totais")
st3 = st.number_input("ST3 - Sólidos Totais")
st4 = st.number_input("ST4 - Sólidos Totais")

# STF
stf1 = st.number_input("STF1 - Sólidos Totais Fixos")
stf2 = st.number_input("STF2 - Sólidos Totais Fixos")
stf3 = st.number_input("STF3 - Sólidos Totais Fixos")
stf4 = st.number_input("STF4 - Sólidos Totais Fixos")

# SST
sst1 = st.number_input("SST1 - Sólidos Suspensos Totais")
sst2 = st.number_input("SST2 - Sólidos Suspensos Totais")
sst3 = st.number_input("SST3 - Sólidos Suspensos Totais")
sst4 = st.number_input("SST4 - Sólidos Suspensos Totais")

# SSF
ssf1 = st.number_input("SSF1 - Sólidos Suspensos Fixos")
ssf2 = st.number_input("SSF2 - Sólidos Suspensos Fixos")
ssf3 = st.number_input("SSF3 - Sólidos Suspensos Fixos")
ssf4 = st.number_input("SSF4 - Sólidos Suspensos Fixos")

if st.button("🧪 Gerar Resultados"):

    SL = np.array([sl1, sl2, sl3, sl4])
    ST = np.array([st1, st2, st3, st4])
    STF = np.array([stf1, stf2, stf3, stf4])
    SST = np.array([sst1, sst2, sst3, sst4])
    SSF = np.array([ssf1, ssf2, ssf3, ssf4])

    # DERIVADOS (TODOS CORRETOS)
    STV = ST - STF
    SSV = SST - SSF
    SDT = ST - SST
    SDV = STV - SSV
    SDF = STF - SSF

    resultados = {
        "SL - Sólidos Totais Gerais": np.mean(SL),
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
    st.success("✔ Todos os parâmetros calculados!")

# ================= LAUDO =================
st.header("📄 Laudo Técnico")

if "resultados" in st.session_state:

    for k, v in st.session_state["resultados"].items():
        st.write(f"**{k}** → {v:.2f}")

else:
    st.info("Execute o laboratório primeiro")
