
import streamlit as st
import numpy as np

# ================= CONFIG =================
st.set_page_config(
    page_title="Laboratório Virtual CEMMA – IFRJ",
    layout="wide"
)

# ================= ESTILO (VISUAL LABORATÓRIO) =================
st.markdown("""
<style>

/* Fundo geral estilo laboratório */
.stApp {
    background-color: #e8f5e9;
}

/* Título */
h1 {
    color: #1b5e20;
    font-weight: 700;
}

h2, h3 {
    color: #2e7d32;
}

/* Área principal */
.block-container {
    padding-top: 2rem;
    padding-left: 2.5rem;
    padding-right: 2.5rem;
}

/* Cards estilo laboratório */
.card {
    background-color: #ffffff;
    padding: 18px;
    border-radius: 12px;
    border-left: 6px solid #2e7d32;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 12px;
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.01);
    box-shadow: 0px 6px 18px rgba(0,0,0,0.12);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #1b5e20;
}

/* Texto da sidebar */
[data-testid="stSidebar"] * {
    color: white;
}

/* Botões */
.stButton>button {
    background-color: #2e7d32;
    color: white;
    border-radius: 8px;
    font-weight: bold;
}

.stButton>button:hover {
    background-color: #1b5e20;
}

</style>
""", unsafe_allow_html=True)

# ================= CABEÇALHO =================
st.title("🧪 Laboratório Virtual CEMMA – IFRJ  - Com Professor Renato Ribeiro")
st.subheader("Laudo Técnico de Ensaios Físico-Químicos")

st.markdown("""
### 👩‍🏫 Criado por  
Luciana Oliveira de Albuquerque  

### 🎓 Administrador  
Raphael Oliveira de Albuquerque
""")

st.success("Sistema ativo 🚀")

# ================= MENU =================
menu = st.sidebar.selectbox(
    "📚 Menu do Sistema",
    [
        "🏠 Início",
        "📖 Aula Teórica",
        "Laboratório",
        "🧪 Sólidos Totais",
        "🧪 Sólidos Suspensos",
        "🧪 N-Amoniacal",
        "🧪 NTK",
        "🧪 DQO",
        "📄 Laudo Final"
    ]
)

# ================= 🔬 MENU EXTRA =================
st.sidebar.markdown("---")
st.sidebar.markdown("## 🔬 Estrutura do Laboratório")

st.sidebar.markdown("""
- Sólidos Totais  
- Sólidos Suspensos  
- N-Amoniacal  
- NTK  
- DQO  
""")

# ================= INÍCIO =================
if menu == "🏠 Início":

    st.markdown(
        "<h2 style='text-align:center;'>👩‍🔬 Bem-vindo (a) ao Laboratório Virtual CEMMA</h2>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 4, 1])

    with col2:
        st.image("logo.png", use_container_width=True)

# ================= AULA TEÓRICA =================
elif menu == "📖 Aula Teórica":

    st.header("📖 Aula Teórica")
    st.info("Conteúdo teórico será inserido aqui futuramente.")

# ================= SÓLIDOS TOTAIS =================
elif menu == "🧪 Sólidos Totais":

    st.markdown("""
    ## 🔬 LABORATÓRIO

    Neste ambiente o aluno encontra os principais ensaios físico-químicos do LabResíduos:

    🧪 Sólidos Totais (ST)  
    🧪 Sólidos Suspensos (SST)  
    🧪 Nitrogênio Amoniacal (N-Amoniacal)  
    🧪 NTK (Nitrogênio Kjeldahl Total)  
    🧪 DQO (Demanda Química de Oxigênio)  

    👉 Selecione o ensaio desejado no menu lateral para iniciar.

    ---
    """)

    st.header("🧪 Solídos Totais")

    volume = st.number_input("Alíquota (mL)", min_value=0.0, value=50.0)

    st.markdown("## 🔹 Réplica 1")
    m1 = st.number_input("m1", value=0.0, format="%.4f")
    m2 = st.number_input("m2", value=0.0, format="%.4f")
    m3 = st.number_input("m3", value=0.0, format="%.4f")

    st.markdown("## 🔹 Réplica 2")
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

            if STF1 > ST1 or STF2 > ST2:
                st.warning("⚠ Atenção: STF maior que ST. Verifique os dados!")

            resultados = {
                "ST": (np.mean([ST1, ST2]), np.std([ST1, ST2], ddof=1)),
                "STF": (np.mean([STF1, STF2]), np.std([STF1, STF2], ddof=1)),
                "STV": (np.mean([STV1, STV2]), np.std([STV1, STV2], ddof=1))
            }

            st.session_state["resultado"] = resultados
            st.success("✔ Cálculos concluídos!")

# ================= SÓLIDOS SUSPENSOS =================
elif menu == "🧪 Sólidos Suspensos":

    st.header("🧪 Sólidos Suspensos")
    st.info("Módulo em desenvolvimento.")

# ================= N-AMONIACAL =================
elif menu == "🧪 N-Amoniacal":

    st.header("🧪 Nitrogênio Amoniacal")
    st.info("Módulo em desenvolvimento.")

# ================= NTK =================
elif menu == "🧪 NTK":

    st.header("🧪 Nitrogênio Kjeldahl Total")
    st.info("Módulo em desenvolvimento.")

# ================= DQO =================
elif menu == "🧪 DQO":

    st.header("🧪 Demanda Química de Oxigênio")
    st.info("Módulo em desenvolvimento.")

# ================= LAUDO FINAL =================
elif menu == "📄 Laudo Final":

    st.header("📄 Laudo Técnico Final")

    if "resultado" in st.session_state:

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

    else:
        st.warning("⚠ Gere os resultados primeiro no laboratório.")
