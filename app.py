import streamlit as st
import numpy as np

# ================= CONFIG =================
st.set_page_config(
    page_title="Laboratório Virtual IFRJ",
    layout="wide"
)

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

# ================= CABEÇALHO =================
st.title("🧪 Laboratório Virtual de Resíduos – IFRJ")

st.markdown("""
### 👩‍🏫 Responsável
Luciana Oliveira de Albuquerque  

### 👨‍🎓 Aluno
Raphael Oliveira de Albuquerque
""")

st.success("Sistema ativo 🚀")

# ================= MENU =================
menu = st.sidebar.selectbox(
    "📚 Menu",
    ["Início", "Aula Teórica", "Laboratório", "Laudo Final"]
)

# ================= INÍCIO =================
if menu == "Início":
    st.info("Sistema de análise físico-química de água e resíduos.")

# ================= AULA TEÓRICA =================
elif menu == "Aula Teórica":

    st.write("""
✔ ST - Sólidos Totais  
✔ STF - Sólidos Totais Fixos  
✔ SST - Sólidos Suspensos Totais  
✔ SSF - Sólidos Suspensos Fixos  
✔ STV - Sólidos Totais Voláteis  
✔ SSV - Sólidos Suspensos Voláteis  
✔ SDT - Sólidos Dissolvidos Totais  
✔ SDV - Sólidos Dissolvidos Voláteis  
✔ SDF - Sólidos Dissolvidos Fixos  
    """)

# ================= LABORATÓRIO =================
elif menu == "Laboratório":

    st.header("🧪 Inserção de Dados Experimentais")

    volume = st.number_input("Volume da amostra (mL)", value=500.0)

    # ================= ST =================
    st.subheader("ST - Sólidos Totais")
    st1 = st.number_input("ST1")
    st2 = st.number_input("ST2")
    st3 = st.number_input("ST3")
    st4 = st.number_input("ST4")

    # ================= STF =================
    st.subheader("STF - Sólidos Totais Fixos")
    f1 = st.number_input("STF1")
    f2 = st.number_input("STF2")
    f3 = st.number_input("STF3")
    f4 = st.number_input("STF4")

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

    if st.button("🧪 Gerar Resultados"):

        ST = np.array([st1, st2, st3, st4])
        STF = np.array([f1, f2, f3, f4])
        SST = np.array([sst1, sst2, sst3, sst4])
        SSF = np.array([ssf1, ssf2, ssf3, ssf4])

        # ================= CÁLCULOS =================
        STV = ST - STF
        SSV = SST - SSF
        SDT = ST - SST
        SDV = STV - SSV
        SDF = STF - SSF

        resultados = {
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
        st.success("✔ Todos os cálculos concluídos!")

# ================= LAUDO FINAL =================
elif menu == "Laudo Final":

    st.header("📄 Laudo Técnico Completo")

    if "resultados" in st.session_state:

        st.write("### 📊 Parâmetro | Resultado")

        for k, v in st.session_state["resultados"].items():
            st.write(f"**{k}** → {v:.2f}")

        st.success("📊 Laudo completo com TODOS os sólidos!")

    else:
        st.warning("Execute o laboratório primeiro")
