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

/* Cards dashboard */
.card {
    background-color: white;
    padding: 20px;
    border-radius: 14px;
    border-left: 6px solid #2e7d32;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
}

/* Botões */
.stButton>button {
    width: 100%;
    height: 70px;
    font-size: 16px;
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

# ================= CABEÇALHO =================
st.title("🧪 LABRESÍDUOS - IFRJ / CEMMA")
st.subheader("Sistema de Laboratório Virtual Físico-Químico")

# ================= INFORMAÇÕES =================
st.markdown("""
### 👩‍🏫 Criado por  
Luciana Oliveira de Albuquerque  

### 🎓 Professor responsável  
Renato Ribeiro  

### 🧑‍💻 Administrador do sistema  
Raphael Oliveira de Albuquerque  
""")

# ================= ALUNO =================
aluno = st.text_input("🧑‍🎓 Nome do Aluno")

if aluno:
    st.success(f"Bem-vindo(a), {aluno}! Sistema pronto para uso 🚀")

st.markdown("---")

# ================= DASHBOARD =================
st.title("📊 Dashboard do Laboratório")

col1, col2 = st.columns(2)

with col1:
    st.button("🏠 Início")
    st.button("🧪 Sólidos Totais")
    st.button("🧪 Sólidos Suspensos")

with col2:
    st.button("🧪 N-Amoniacal")
    st.button("🧪 NTK")
    st.button("🧪 DQO")

st.markdown("---")

# ================= SÓLIDOS TOTAIS =================
st.header("🧪 Sólidos Totais")

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

    if volume <= 0:
        st.error("Volume inválido.")
    else:
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

# ================= RESULTADOS =================
if "resultado" in st.session_state:

    st.markdown("## 📄 Resultados do Laudo")

    nomes = {
        "ST": "Sólidos Totais (ST)",
        "STF": "Sólidos Fixos (STF)",
        "STV": "Sólidos Voláteis (STV)"
    }

    for chave, (media, dp) in st.session_state["resultado"].items():

        st.markdown(f"""
        <div class="card">
        <b>{nomes[chave]}</b><br>
        {media:.2f} ± {dp:.2f} mg/L
        </div>
        """, unsafe_allow_html=True)
