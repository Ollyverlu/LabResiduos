import streamlit as st
import numpy as np

# ================= CONFIG =================
st.set_page_config(
    page_title="LabResíduos IFRJ - CEMMA",
    layout="wide"
)

# ================= ESTILO =================
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
    st.title("Sistema IFRJ")
    st.info("Selecione um módulo no menu lateral.")

# ================= SÓLIDOS TOTAIS =================
elif menu == "🧪 Sólidos Totais":
    st.title("Sólidos Totais")
    st.info("Módulo original mantido.")

    st.button("⬅ Voltar", on_click=lambda: st.experimental_rerun())

# ================= SÓLIDOS SUSPENSOS =================
elif menu == "🧪 Sólidos Suspensos":
    st.title("Sólidos Suspensos")
    st.info("Mesmo modelo do Sólidos Totais.")

    st.button("⬅ Voltar", on_click=lambda: st.experimental_rerun())

# ================= N-AMONIACAL (COMPLETO) =================
elif menu == "🧪 N-Amoniacal":

    st.title("DETERMINAÇÃO DE NITROGÊNIO AMONIACAL")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.text_input("RESPONSÁVEL")

    with col2:
        st.text_input("PROJETO")

    with col3:
        st.date_input("DATA DA ANÁLISE")

    with col4:
        st.time_input("HORA DA ANÁLISE")

    st.markdown("---")

    st.markdown("""
    <div class="card">
    <b>PADRONIZAÇÃO DO ÁCIDO SULFÚRICO (H2SO4) 0,02 N</b><br><br>

    PADRÃO PRIMÁRIO: TETRABORATO DE SÓDIO DECA HIDRATADO<br>
    MASSA PESADA: ____ g<br>
    MASSA MOLAR: 381,40 g/mol<br>
    VOLUME DO BALÃO: ____ mL<br>
    CONCENTRAÇÃO: #DIV/0!<br>
    </div>
    """, unsafe_allow_html=True)

    massa = st.number_input("Massa (g)", value=0.0)
    vol = st.number_input("Volume do balão (mL)", value=100.0)

    t1 = st.number_input("1ª Titulação", value=0.0)
    t2 = st.number_input("2ª Titulação", value=0.0)
    t3 = st.number_input("3ª Titulação", value=0.0)

    if st.button("CALCULAR N-AMONIACAL"):

        media = np.mean([t1, t2, t3])

        if media > 0:
            resultado = (massa / 381.4) / (vol / 1000) * (vol / media)

            st.session_state["n_amoniacal"] = resultado

    if "n_amoniacal" in st.session_state:
        st.success(f"Resultado: {st.session_state['n_amoniacal']:.4f}")

    st.button("⬅ Voltar", on_click=lambda: st.experimental_rerun())

# ================= NTK =================
elif menu == "🧪 NTK":
    st.title("NTK")
    st.info("Módulo preservado para implementação futura.")
    st.button("⬅ Voltar", on_click=lambda: st.experimental_rerun())

# ================= NHX =================
elif menu == "🧪 NHX":
    st.title("NHX")
    st.info("Módulo preservado para implementação futura.")
    st.button("⬅ Voltar", on_click=lambda: st.experimental_rerun())

# ================= DQO =================
elif menu == "🧪 DQO":
    st.title("DQO")
    st.info("Módulo preservado para implementação futura.")
    st.button("⬅ Voltar", on_click=lambda: st.experimental_rerun())
