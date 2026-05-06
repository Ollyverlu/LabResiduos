import streamlit as st
import numpy as np
from datetime import datetime
# ================= LOGIN USUÁRIOS =================
USUARIOS = {
    "raphael": "1234",
    "aluno1": "1111",
    "aluno2": "2222"
}
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
        text-align: center;
    }

    .stButton > button {
        background-color: #1f4e79;
        color: white;
        border-radius: 10px;
        width: 100%;
    }

    section[data-testid="stSidebar"] {
        background-color: #e8eefc;
    }
    </style>
""", unsafe_allow_html=True)

# ================= CABEÇALHO =================
st.title("🧪 Laboratório Virtual de Resíduos – IFRJ")
st.subheader("Laudo Técnico de Ensaios Físico-Químicos")

st.markdown("""
### 👩‍🏫 Responsável
**Luciana Oliveira de Albuquerque**
""")
### 👨‍🎓 Aluno
**Raphael Oliveira de Albuquerque**

### 🔐 Usuário logado
**{st.session_state['usuario']}**
""")
st.success("Sistema ativo 🚀")

# ================= MENU =================
menu = st.sidebar.selectbox(
    "📚 Menu do Sistema",
    ["Início", "Aula Teórica", "Laboratório", "Laudo Final"]
)

# ================= INÍCIO =================
if menu == "Início":
    st.markdown("## 👩‍🔬 Bem-vinda ao Laboratório Virtual")

    st.info("Sistema de ensino de análises físico-químicas de água e resíduos.")

    st.markdown("""
    ### 🎯 Você irá aprender:
    - Cálculo de ST, STF, SST, SSF  
    - Média e desvio padrão  
    - Interpretação de resultados  
    - Laudos técnicos completos  
    """)

# ================= AULA TEÓRICA =================
elif menu == "Aula Teórica":

    st.header("📚 Conteúdo Teórico")

    st.write("""
    O monitoramento de água e resíduos utiliza parâmetros físico-químicos:

    ✔ ST (Sólidos Totais)  
    ✔ STF (Sólidos Totais Fixos)  
    ✔ SST (Sólidos Suspensos Totais)  
    ✔ SSF (Sólidos Suspensos Fixos)  
    ✔ STV (Sólidos Totais Voláteis)  
    ✔ SSV (Sólidos Suspensos Voláteis)  
    ✔ SDT (Sólidos Dissolvidos Totais)  
    ✔ SDF (Sólidos Dissolvidos Fixos)  
    ✔ SDV (Sólidos Dissolvidos Voláteis)  
    """)

# ================= LABORATÓRIO =================
elif menu == "Laboratório":

    st.header("🧪 Inserção de Dados Experimentais")

    volume = st.number_input("Volume da amostra (mL)", value=500.0)

    st.subheader("ST (Sólidos Totais)")
    st1 = st.number_input("ST1")
    st2 = st.number_input("ST2")
    st3 = st.number_input("ST3")
    st4 = st.number_input("ST4")

    st.subheader("STF (Sólidos Totais Fixos)")
    f1 = st.number_input("STF1")
    f2 = st.number_input("STF2")
    f3 = st.number_input("STF3")
    f4 = st.number_input("STF4")

    st.subheader("SST (Sólidos Suspensos Totais)")
    sst1 = st.number_input("SST1")
    sst2 = st.number_input("SST2")
    sst3 = st.number_input("SST3")
    sst4 = st.number_input("SST4")

    st.subheader("SSF (Sólidos Suspensos Fixos)")
    ssf1 = st.number_input("SSF1")
    ssf2 = st.number_input("SSF2")
    ssf3 = st.number_input("SSF3")
    ssf4 = st.number_input("SSF4")

    if st.button("🧪 Gerar Resultados"):

        ST = np.array([st1, st2, st3, st4])
        STF = np.array([f1, f2, f3, f4])
        SST = np.array([sst1, sst2, sst3, sst4])
        SSF = np.array([ssf1, ssf2, ssf3, ssf4])

        # ===== CÁLCULOS =====
        STV = ST - STF
        SSV = SST - SSF
        SDT = ST - SST
        SDF = STF - SSF
        SDV = STV - SSV

        resultados = {
            "ST": (np.mean(ST), np.std(ST)),
            "STF": (np.mean(STF), np.std(STF)),
            "SST": (np.mean(SST), np.std(SST)),
            "SSF": (np.mean(SSF), np.std(SSF)),
            "STV": (np.mean(STV), np.std(STV)),
            "SSV": (np.mean(SSV), np.std(SSV)),
            "SDT": (np.mean(SDT), np.std(SDT)),
            "SDF": (np.mean(SDF), np.std(SDF)),
            "SDV": (np.mean(SDV), np.std(SDV)),
        }

        st.session_state["resultados"] = resultados
        st.success("✔ Cálculos concluídos com sucesso!")

# ================= LAUDO FINAL =================
elif menu == "Laudo Final":

    st.header("📄 Laudo Técnico Completo")

    if "resultados" in st.session_state:

        st.write("### 📊 Parâmetro | Resultado (média ± desvio) | Classificação")

        for k, v in st.session_state["resultados"].items():

            media, dp = v

            if media < 50:
                classe = "Baixo"
            elif media < 150:
                classe = "Médio"
            else:
                classe = "Alto"

            st.write(f"**{k}** | {media:.2f} ± {dp:.2f} | {classe}")

        st.markdown("---")

        st.markdown("### 🧪 Fórmulas do Sistema")

        st.write("""
- ST = Sólidos Totais  
- STF = Sólidos Totais Fixos  
- SST = Sólidos Suspensos Totais  
- SSF = Sólidos Suspensos Fixos  
- STV = ST - STF  
- SSV = SST - SSF  
- SDT = ST - SST  
- SDF = STF - SSF  
- SDV = STV - SSV  
        """)

        st.success("📊 Laudo gerado com sucesso!")

    else:
        st.warning("⚠ Primeiro vá ao Laboratório e gere os cálculos")
