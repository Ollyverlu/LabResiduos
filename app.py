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

.stApp {
    background-color: #e8f5e9;
}

h1 {
    color: #1b5e20 !important;
    font-weight: 900;
}

h2, h3 {
    color: #2e7d32 !important;
}

.card {
    background: white;
    padding: 15px;
    border-radius: 12px;
    border-left: 6px solid #2e7d32;
    margin-top: 10px;
}

input {
    background-color: white !important;
    color: black !important;
    font-size: 16px !important;
}

.stButton>button {
    background-color: #2e7d32;
    color: white;
    font-weight: bold;
    width: 100%;
    height: 55px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ================= CABEÇALHO =================
col1, col2 = st.columns([1, 5])

with col1:
    st.image("logo.png", width=100)

with col2:
    st.title("🧪 LABRESÍDUOS - IFRJ / CEMMA")
    st.subheader("Sistema Virtual de Análises Físico-Químicas")

    st.markdown("""
    ### 👩‍🏫 Criado por: Luciana Oliveira de Albuquerque  
    ### 🎓 Professor responsável: Renato Ribeiro  
    ### 🧑‍💻 Administrador: Raphael Oliveira de Albuquerque  
    """)

st.markdown("---")

# ================= MENU =================
menu = st.sidebar.radio(
    "📊 Menu do Sistema",
    [
        "🏠 Início",
        "🧪 Sólidos Totais",
        "🧪 Sólidos Suspensos",
        "🧪 N-Amoniacal",
        "🧪 NTK",
        "🧪 NHX",
        "🧪 DQO"
    ]
)

# ================= INÍCIO =================
if menu == "🏠 Início":
    st.title("Sistema IFRJ - Laboratório Virtual")
    st.info("Selecione um módulo no menu lateral.")

# ================= SÓLIDOS TOTAIS =================
elif menu == "🧪 Sólidos Totais":
    st.title("🧪 Sólidos Totais")

    volume = st.number_input("Alíquota (mL)", value=50.0)

    m1 = st.number_input("m1", value=0.0)
    m2 = st.number_input("m2", value=0.0)
    m3 = st.number_input("m3", value=0.0)

    m1_2 = st.number_input("m1'", value=0.0)
    m2_2 = st.number_input("m2'", value=0.0)
    m3_2 = st.number_input("m3'", value=0.0)

    if st.button("Calcular ST"):

        fator = 1000 / (volume / 1000)

        ST1 = (m2 - m1) * fator
        ST2 = (m2_2 - m1_2) * fator

        STF1 = (m3 - m1) * fator
        STF2 = (m3_2 - m1_2) * fator

        STV1 = ST1 - STF1
        STV2 = ST2 - STF2

        st.session_state["ST"] = (np.mean([ST1, ST2]), np.std([ST1, ST2], ddof=1))
        st.session_state["STF"] = (np.mean([STF1, STF2]), np.std([STF1, STF2], ddof=1))
        st.session_state["STV"] = (np.mean([STV1, STV2]), np.std([STV1, STV2], ddof=1))

    if "ST" in st.session_state:
        st.markdown("### 📄 Resultados")

        st.markdown(f"""
        <div class="card">
        <b>ST:</b> {st.session_state["ST"][0]:.2f} ± {st.session_state["ST"][1]:.2f}
        </div>
        """, unsafe_allow_html=True)

    st.button("⬅ Voltar")

# ================= SÓLIDOS SUSPENSOS =================
elif menu == "🧪 Sólidos Suspensos":
    st.title("🧪 Sólidos Suspensos")
    st.info("Estrutura igual ao Sólidos Totais (em implementação).")

    st.button("⬅ Voltar")

# ================= N-AMONIACAL =================
elif menu == "🧪 N-Amoniacal":

    st.title("DETERMINAÇÃO DE NITROGÊNIO AMONIACAL")

    responsavel = st.text_input("Responsável")
    projeto = st.text_input("Projeto")
    data = st.date_input("Data da Análise")
    hora = st.time_input("Hora da Análise")

    st.markdown("---")

    massa = st.number_input("Massa (g)", value=0.0)
    volume = st.number_input("Volume (mL)", value=100.0)

    t1 = st.number_input("1ª Titulação", value=0.0)
    t2 = st.number_input("2ª Titulação", value=0.0)
    t3 = st.number_input("3ª Titulação", value=0.0)

    if st.button("Calcular N-Amoniacal"):

        media = np.mean([t1, t2, t3])

        if media > 0:
            resultado = (massa / 381.4) / (volume / 1000) * (volume / media)
            st.session_state["N_AMONIACAL"] = resultado

    if "N_AMONIACAL" in st.session_state:
        st.success(f"Resultado: {st.session_state['N_AMONIACAL']:.4f}")

    st.button("⬅ Voltar")

# ================= NTK =================
elif menu == "🧪 NTK":
    st.title("🧪 NTK")
    st.info("Estrutura de planilha IFRJ será aplicada aqui.")

    st.button("⬅ Voltar")

# ================= NHX =================
elif menu == "🧪 NHX":
    st.title("🧪 NHX")
    st.info("Estrutura de planilha IFRJ será aplicada aqui.")

    st.button("⬅ Voltar")

# ================= DQO =================
elif menu == "🧪 DQO":
    st.title("🧪 DQO")
    st.info("Estrutura de planilha IFRJ será aplicada aqui.")

    st.button("⬅ Voltar")
