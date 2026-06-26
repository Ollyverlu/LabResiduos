import streamlit as st
import numpy as np

# ================= CONFIG =================
""", unsafe_allow_html=True)

# ================= CABEÇALHO =================
st.title("🧪 Laboratório Virtual CEMMA – IFRJ  - Com Professor Renato Ribeiro")
st.subheader("Laudo Técnico de Ensaios Físico-Químicos")

st.markdown("""
### 👩‍🏫 Criado por  
Luciana Oliveira de Albuquerque  

### 🎓 Professor responsável  
Renato Ribeiro  

### 🧑‍💻 Administrador do sistema  
Raphael Oliveira de Albuquerque
""")

st.success("Sistema ativo 🚀")
# ================= ESTILO PROFISSIONAL =================
st.markdown("""
<style>

/* Fundo geral */
.stApp {
    background-color: #e8f5e9;
}

/* Títulos */
h1 {
    color: #1b5e20 !important;
    font-weight: 800;
}

h2 {
    color: #2e7d32 !important;
}

/* Cards estilo dashboard */
.card {
    background-color: white;
    padding: 20px;
    border-radius: 14px;
    border-left: 6px solid #2e7d32;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.02);
}

/* Botões estilo sistema */
.stButton>button {
    width: 100%;
    height: 70px;
    font-size: 18px;
    font-weight: bold;
    background-color: #2e7d32;
    color: white;
    border-radius: 12px;
}

.stButton>button:hover {
    background-color: #1b5e20;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #1b5e20;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ================= ESTADO DE NAVEGAÇÃO =================
if "page" not in st.session_state:
    st.session_state.page = "dashboard"

def go(page):
    st.session_state.page = page

# ================= DASHBOARD =================
if st.session_state.page == "dashboard":

    st.title("🧪 LABRESÍDUOS - IFRJ / CEMMA")
    st.subheader("Sistema de Laboratório Virtual Físico-Químico")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.button("🏠 Início", on_click=go, args=("inicio",))
        st.button("🧪 Sólidos Totais", on_click=go, args=("st",))
        st.button("🧪 Sólidos Suspensos", on_click=go, args=("ss",))

    with col2:
        st.button("🧪 N-Amoniacal", on_click=go, args=("namo",))
        st.button("🧪 NTK", on_click=go, args=("ntk",))
        st.button("🧪 DQO", on_click=go, args=("dqo",))

    st.markdown("---")

    st.info("Selecione um módulo para iniciar o laboratório.")

# ================= INÍCIO =================
elif st.session_state.page == "inicio":

    st.title("🏠 Início do Sistema")

    st.markdown("""
    ### Bem-vindo ao LabResíduos IFRJ

    Sistema virtual para análise de parâmetros físico-químicos:

    - Sólidos Totais  
    - Sólidos Suspensos  
    - N-Amoniacal  
    - NTK  
    - DQO  
    """)

    st.button("⬅ Voltar", on_click=go, args=("dashboard",))

# ================= SÓLIDOS TOTAIS (SEU CÓDIGO ORIGINAL) =================
elif st.session_state.page == "st":

    st.title("🧪 Sólidos Totais")

    volume = st.number_input("Alíquota (mL)", min_value=0.0, value=50.0)

    st.markdown("## Réplica 1")
    m1 = st.number_input("m1", value=0.0, format="%.4f")
    m2 = st.number_input("m2", value=0.0, format="%.4f")
    m3 = st.number_input("m3", value=0.0, format="%.4f")

    st.markdown("## Réplica 2")
    m1_2 = st.number_input("m1'", value=0.0, format="%.4f")
    m2_2 = st.number_input("m2'", value=0.0, format="%.4f")
    m3_2 = st.number_input("m3'", value=0.0, format="%.4f")

    if st.button("🧪 GERAR RESULTADOS"):

        fator = 1000 / (volume / 1000)

        ST1 = (m2 - m1) * fator
        ST2 = (m2_2 - m1_2) * fator

        STF1 = (m3 - m1) * fator
        STF2 = (m3_2 - m1_2) * fator

        STV1 = ST1 - STF1
        STV2 = ST2 - STF2

        resultados = {
            "ST": (np.mean([ST1, ST2]), np.std([ST1, ST2], ddof=1)),
            "STF": (np.mean([STF1, STF2]), np.std([STF1, STF2], ddof=1)),
            "STV": (np.mean([STV1, STV2]), np.std([STV1, STV2], ddof=1))
        }

        st.session_state["resultado"] = resultados
        st.success("✔ Cálculos concluídos!")

    st.button("⬅ Voltar ao Dashboard", on_click=go, args=("dashboard",))

# ================= OUTROS MÓDULOS =================
else:
    st.title("🧪 Módulo em Desenvolvimento")
    st.info("Este laboratório será implementado em breve.")

    st.button("⬅ Voltar ao Dashboard", on_click=go, args=("dashboard",))
