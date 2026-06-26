import streamlit as st
import numpy as np

# ================= CONFIG =================
st.set_page_config(page_title="IFRJ - Laboratório Virtual CEMMA", layout="wide")

# ================= CSS =================
st.markdown("""
<style>
.stApp {
    background-color: #e9f5e9;
}

h1 {
    color: #0f3d1f !important;
    font-weight: 900;
}

.card {
    background: white;
    border-left: 6px solid #1b5e20;
    padding: 15px;
    border-radius: 10px;
    margin-top: 10px;
}

.stButton>button {
    background: #1b5e20;
    color: white;
    width: 100%;
    height: 50px;
    font-weight: bold;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# ================= CABEÇALHO =================
col1, col2 = st.columns([1, 5])

with col1:
    st.image("logo.png", width=90)

with col2:
    st.title("🧪 IFRJ - LABORATÓRIO VIRTUAL CEMMA")
    st.markdown("""
**Criado por:** Luciana Oliveira de Albuquerque  
**Professor responsável:** Renato Ribeiro  
**Administrador do sistema:** Raphael Oliveira de Albuquerque  
""")

st.markdown("---")

# ================= MENU =================
menu = st.sidebar.radio("📚 Sistema Laboratorial IFRJ", [
    "🏠 Dashboard",
    "🧪 Sólidos Totais",
    "🧪 Sólidos Suspensos",
    "🧪 N-Amoniacal",
    "🧪 NTK",
    "🧪 NHX",
    "🧪 DQO"
])

# ================= FUNÇÃO CABEÇALHO =================
def header(titulo):
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

# ================= DASHBOARD =================
if menu == "🏠 Dashboard":
    st.title("Sistema IFRJ")
    st.info("Selecione um módulo no menu lateral.")

# ================= SÓLIDOS TOTAIS =================
elif menu == "🧪 Sólidos Totais":
    header("SÓLIDOS TOTAIS")

    v = st.number_input("Volume (mL)", value=50.0)

    m1 = st.number_input("m1")
    m2 = st.number_input("m2")
    m3 = st.number_input("m3")

    m1_2 = st.number_input("m1 (rep 2)")
    m2_2 = st.number_input("m2 (rep 2)")
    m3_2 = st.number_input("m3 (rep 2)")

    if st.button("Calcular ST"):

        fator = 1000 / (v / 1000)

        st1 = (m2 - m1) * fator
        st2 = (m2_2 - m1_2) * fator

        stf1 = (m3 - m1) * fator
        stf2 = (m3_2 - m1_2) * fator

        stv1 = st1 - stf1
        stv2 = st2 - stf2

        st.markdown(f"""
        <div class="card">
        <b>ST:</b> {np.mean([st1, st2]):.2f} ± {np.std([st1, st2], ddof=1):.2f}<br>
        <b>STF:</b> {np.mean([stf1, stf2]):.2f} ± {np.std([stf1, stf2], ddof=1):.2f}<br>
        <b>STV:</b> {np.mean([stv1, stv2]):.2f} ± {np.std([stv1, stv2], ddof=1):.2f}
        </div>
        """, unsafe_allow_html=True)

# ================= SÓLIDOS SUSPENSOS (IGUAL ST) =================
elif menu == "🧪 Sólidos Suspensos":
    header("SÓLIDOS SUSPENSOS")

    v = st.number_input("Volume (mL)", value=50.0)

    m1 = st.number_input("m1")
    m2 = st.number_input("m2")
    m3 = st.number_input("m3")

    m1_2 = st.number_input("m1 (rep 2)")
    m2_2 = st.number_input("m2 (rep 2)")
    m3_2 = st.number_input("m3 (rep 2)")

    if st.button("Calcular SS"):

        fator = 1000 / (v / 1000)

        ss1 = (m2 - m1) * fator
        ss2 = (m2_2 - m1_2) * fator

        ssf1 = (m3 - m1) * fator
        ssf2 = (m3_2 - m1_2) * fator

        ssv1 = ss1 - ssf1
        ssv2 = ss2 - ssf2

        st.markdown(f"""
        <div class="card">
        <b>SS:</b> {np.mean([ss1, ss2]):.2f} ± {np.std([ss1, ss2], ddof=1):.2f}<br>
        <b>SSF:</b> {np.mean([ssf1, ssf2]):.2f} ± {np.std([ssf1, ssf2], ddof=1):.2f}<br>
        <b>SSV:</b> {np.mean([ssv1, ssv2]):.2f} ± {np.std([ssv1, ssv2], ddof=1):.2f}
        </div>
        """, unsafe_allow_html=True)

# ================= N-AMONIACAL =================
elif menu == "🧪 N-Amoniacal":
    header("NITROGÊNIO AMONIACAL")

    m = st.number_input("Massa")
    v = st.number_input("Volume")

    t1 = st.number_input("T1")
    t2 = st.number_input("T2")
    t3 = st.number_input("T3")

    if st.button("Calcular"):
        media = np.mean([t1, t2, t3])
        if media != 0:
            st.success((m/381.4)/(v/1000)*(v/media))

# ================= NTK =================
elif menu == "NTK":
    header("NITROGÊNIO TOTAL KJELDAHL")

    m = st.number_input("Massa")
    v = st.number_input("Volume")

    t1 = st.number_input("T1")
    t2 = st.number_input("T2")
    t3 = st.number_input("T3")

    if st.button("Calcular"):
        media = np.mean([t1, t2, t3])
        if media != 0:
            st.success((m/381.4)/(v/1000)*(v/media))

# ================= NHX =================
elif menu == "NHX":
    header("NITROGÊNIO NHX")

    m = st.number_input("Massa")
    v = st.number_input("Volume")

    t1 = st.number_input("T1")
    t2 = st.number_input("T2")
    t3 = st.number_input("T3")

    if st.button("Calcular"):
        media = np.mean([t1, t2, t3])
        if media != 0:
            st.success((m/381.4)/(v/1000)*(v/media))

# ================= DQO =================
elif menu == "DQO":
    header("DEMANDA QUÍMICA DE OXIGÊNIO")

    m = st.number_input("Massa padrão")
    v = st.number_input("Volume amostra")

    t1 = st.number_input("T1")
    t2 = st.number_input("T2")
    t3 = st.number_input("T3")

    if st.button("Calcular"):
        media = np.mean([t1, t2, t3])
        if media != 0:
            st.success((m * 0.25) / (media + 0.0001))
