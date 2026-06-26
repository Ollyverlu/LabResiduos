import streamlit as st
import numpy as np

# ================= CONFIG =================
st.set_page_config(
    page_title="LabResíduos IFRJ - CEMMA",
    layout="wide"
)

# ================= ESTILO (VERDE MAIS CLARO + LEITURA) =================
st.markdown("""
<style>

/* FUNDO */
.stApp {
    background-color: #e8f5e9;
}

/* CABEÇALHO */
.header {
    background-color: #2e7d32;  /* verde mais claro */
    padding: 15px;
    border-radius: 10px;
    color: white;
    margin-bottom: 15px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.15);
}

.header h1 {
    margin: 0;
    font-size: 34px;
    text-align: center;
    color: white !important;
}

.header h3 {
    margin: 0;
    font-size: 18px;
    text-align: center;
    font-weight: normal;
    color: #f1f8e9 !important;
}

/* TEXTOS GERAIS */
p, label, span {
    color: #1a1a1a !important;
    font-size: 16px;
}

/* INPUTS */
input, textarea {
    background-color: white !important;
    color: black !important;
    font-size: 16px !important;
}

/* BOTÕES */
.stButton>button {
    width: 100%;
    height: 65px;
    font-size: 16px;
    font-weight: bold;
    background-color: #2e7d32;
    color: white;
    border-radius: 12px;
}

/* CARDS RESULTADO */
.card {
    background-color: white;
    padding: 18px;
    border-radius: 12px;
    border-left: 6px solid #2e7d32;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.10);
    font-size: 18px;
    color: black !important;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background-color: #1b5e20;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ================= NAVEGAÇÃO =================
if "page" not in st.session_state:
    st.session_state.page = "dashboard"

def go(page):
    st.session_state.page = page

# ================= CABEÇALHO PROFISSIONAL =================
col1, col2 = st.columns([1, 4])

with col1:
    st.image("logo.png", width=120)

with col2:
    st.markdown("""
    <div class="header">
        <h1>🧪 LABRESÍDUOS - IFRJ / CEMMA</h1>
        <h3>Sistema Virtual de Análises Físico-Químicas</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### 👩‍🏫 Criado por  
    Luciana Oliveira de Albuquerque  

    ### 🎓 Professor responsável  
    Renato Ribeiro  

    ### 🧑‍💻 Administrador do sistema  
    Raphael Oliveira de Albuquerque  
    """)

st.markdown("---")

# ================= DASHBOARD =================
if st.session_state.page == "dashboard":

    st.title("📊 Dashboard do Laboratório")

    col1, col2 = st.columns(2)

    with col1:
        st.button("🏠 Início", on_click=go, args=("inicio",))
        st.button("🧪 Sólidos Totais", on_click=go, args=("st",))
        st.button("🧪 Sólidos Suspensos", on_click=go, args=("ss",))

    with col2:
        st.button("🧪 N-Amoniacal", on_click=go, args=("namo",))
        st.button("🧪 NTK", on_click=go, args=("ntk",))
        st.button("🧪 DQO", on_click=go, args=("dqo",))

# ================= INÍCIO =================
elif st.session_state.page == "inicio":

    st.title("🏠 Início do Sistema")
    st.info("Bem-vindo ao LabResíduos IFRJ")

    st.button("⬅ Voltar", on_click=go, args=("dashboard",))

# ================= SÓLIDOS TOTAIS =================
elif st.session_state.page == "st":

    st.title("🧪 Sólidos Totais")

    volume = st.number_input("Alíquota (mL)", min_value=0.0, value=50.0)

    st.markdown("### Réplica 1")
    m1 = st.number_input("m1", value=0.0, format="%.4f")
    m2 = st.number_input("m2", value=0.0, format="%.4f")
    m3 = st.number_input("m3", value=0.0, format="%.4f")

    st.markdown("### Réplica 2")
    m1_2 = st.number_input("m1'", value=0.0, format="%.4f")
    m2_2 = st.number_input("m2'", value=0.0, format="%.4f")
    m3_2 = st.number_input("m3'", value=0.0, format="%.4f")

    if st.button("🧪 GERAR RESULTADO"):

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

    # ================= RESULTADO =================
    if "resultado" in st.session_state:

        st.markdown("## 📄 Resultado Final")

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

    st.button("⬅ Voltar", on_click=go, args=("dashboard",))

# ================= OUTROS =================
elif st.session_state.page == "ss":
    st.title("🧪 Sólidos Suspensos")
    st.info("Módulo em desenvolvimento.")
    st.button("⬅ Voltar", on_click=go, args=("dashboard",))

elif st.session_state.page == "namo":
    st.title("🧪 N-Amoniacal")
    st.info("Módulo em desenvolvimento.")
    st.button("⬅ Voltar", on_click=go, args=("dashboard",))

elif st.session_state.page == "ntk":
    st.title("🧪 NTK")
    st.info("Módulo em desenvolvimento.")
    st.button("⬅ Voltar", on_click=go, args=("dashboard",))

elif st.session_state.page == "dqo":
    st.title("🧪 DQO")
    st.info("Módulo em desenvolvimento.")
    st.button("⬅ Voltar", on_click=go, args=("dashboard",))
