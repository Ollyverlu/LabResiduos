import streamlit as st
import numpy as np

# ================= CONFIG =================
st.set_page_config(page_title="LabResíduos IFRJ", layout="wide")

# ================= ESTILO =================
st.markdown("""
<style>
.stApp {
    background-color: #eaf6ea;
}

h1 {
    color: #1b5e20 !important;
    font-weight: 900;
}

h2 {
    color: #2e7d32 !important;
}

.card {
    background: white;
    padding: 15px;
    border-left: 6px solid #2e7d32;
    border-radius: 10px;
    margin-top: 10px;
}

.stButton>button {
    background: #2e7d32;
    color: white;
    width: 100%;
    height: 50px;
    border-radius: 8px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ================= CABEÇALHO =================
col1, col2 = st.columns([1, 5])

with col1:
    st.image("logo.png", width=90)

with col2:
    st.title("🧪 LABRESÍDUOS IFRJ - CEMMA")
    st.markdown("""
    **Criado por:** Luciana Oliveira de Albuquerque  
    **Professor:** Renato Ribeiro  
    **Administrador:** Raphael Oliveira de Albuquerque  
    """)

st.markdown("---")

# ================= MENU =================
menu = st.sidebar.radio("📊 MENU DO LABORATÓRIO", [
    "🏠 Início",
    "🧪 Sólidos Totais",
    "🧪 Sólidos Suspensos",
    "🧪 N-Amoniacal",
    "🧪 NTK",
    "🧪 NHX",
    "🧪 DQO"
])

# ================= FUNÇÃO PADRÃO DE CABEÇALHO DOS MÓDULOS =================
def header_modulo(titulo):
    st.title(f"DETERMINAÇÃO DE {titulo}")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.text_input("Responsável")
    with col2:
        st.text_input("Projeto")
    with col3:
        st.date_input("Data da Análise")
    with col4:
        st.time_input("Hora da Análise")

    st.markdown("---")

# ================= INÍCIO =================
if menu == "🏠 Início":
    st.title("Sistema IFRJ - Laboratório Virtual")
    st.info("Selecione um módulo no menu lateral para iniciar as análises.")

# ================= SÓLIDOS TOTAIS =================
elif menu == "🧪 Sólidos Totais":
    header_modulo("SÓLIDOS TOTAIS")

    v = st.number_input("Volume (mL)", value=50.0)

    m1 = st.number_input("m1")
    m2 = st.number_input("m2")
    m3 = st.number_input("m3")

    m1_2 = st.number_input("m1' (rep 2)")
    m2_2 = st.number_input("m2' (rep 2)")
    m3_2 = st.number_input("m3' (rep 2)")

    if st.button("Calcular ST"):

        fator = 1000 / (v / 1000)

        ST1 = (m2 - m1) * fator
        ST2 = (m2_2 - m1_2) * fator

        STF1 = (m3 - m1) * fator
        STF2 = (m3_2 - m1_2) * fator

        STV1 = ST1 - STF1
        STV2 = ST2 - STF2

        st.success("Cálculo realizado com sucesso!")

        st.markdown(f"""
        <div class="card">
        <b>ST:</b> {np.mean([ST1, ST2]):.2f} ± {np.std([ST1, ST2], ddof=1):.2f} mg/L<br>
        <b>STF:</b> {np.mean([STF1, STF2]):.2f} ± {np.std([STF1, STF2], ddof=1):.2f} mg/L<br>
        <b>STV:</b> {np.mean([STV1, STV2]):.2f} ± {np.std([STV1, STV2], ddof=1):.2f} mg/L
        </div>
        """, unsafe_allow_html=True)

# ================= SÓLIDOS SUSPENSOS =================
elif menu == "🧪 Sólidos Suspensos":
    header_modulo("SÓLIDOS SUSPENSOS")

    v = st.number_input("Volume (mL)", value=50.0)
    m1 = st.number_input("m1")
    m2 = st.number_input("m2")

    if st.button("Calcular SS"):
        fator = 1000 / (v / 1000)
        st.success((m2 - m1) * fator)

# ================= N-AMONIACAL =================
elif menu == "🧪 N-Amoniacal":
    header_modulo("NITROGÊNIO AMONIACAL")

    m = st.number_input("Massa")
    v = st.number_input("Volume")

    t1 = st.number_input("Titulação 1")
    t2 = st.number_input("Titulação 2")
    t3 = st.number_input("Titulação 3")

    if st.button("Calcular"):
        media = np.mean([t1, t2, t3])
        if media != 0:
            st.success((m/381.4)/(v/1000)*(v/media))

# ================= NTK =================
elif menu == "🧪 NTK":
    header_modulo("NITROGÊNIO TOTAL KJELDAHL")

    m = st.number_input("Massa")
    v = st.number_input("Volume")

    t1 = st.number_input("Titulação 1")
    t2 = st.number_input("Titulação 2")
    t3 = st.number_input("Titulação 3")

    if st.button("Calcular NTK"):
        media = np.mean([t1, t2, t3])
        if media != 0:
            st.success((m/381.4)/(v/1000)*(v/media))

# ================= NHX =================
elif menu == "🧪 NHX":
    header_modulo("NITROGÊNIO NHX")

    m = st.number_input("Massa")
    v = st.number_input("Volume")

    t1 = st.number_input("Titulação 1")
    t2 = st.number_input("Titulação 2")
    t3 = st.number_input("Titulação 3")

    if st.button("Calcular NHX"):
        media = np.mean([t1, t2, t3])
        if media != 0:
            st.success((m/381.4)/(v/1000)*(v/media))

# ================= DQO =================
elif menu == "🧪 DQO":
    header_modulo("DEMANDA QUÍMICA DE OXIGÊNIO")

    m = st.number_input("Massa padrão")
    v = st.number_input("Volume amostra")

    t1 = st.number_input("Titulação 1")
    t2 = st.number_input("Titulação 2")
    t3 = st.number_input("Titulação 3")

    if st.button("Calcular DQO"):
        media = np.mean([t1, t2, t3])
        if media != 0:
            st.success((m * 0.25) / (media + 0.0001))
