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

# ================= N-AMONIACAL =================
if menu == "🧪 N-Amoniacal":

    # ================= TÍTULO ORIGINAL (RESTAURADO) =================
    st.title("DETERMINAÇÃO DE NITROGÊNIO AMONIACAL")

    # ================= CABEÇALHO CLICÁVEL =================
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

    # ================= PLANILHA (EXCEL VISUAL) =================
    st.markdown("""
    <div style="background-color:white; padding:15px; border-radius:10px;">

    <h4>PADRONIZAÇÃO DO ÁCIDO SULFÚRICO (H₂SO₄) 0,02 N</h4>

    <b>PADRÃO PRIMÁRIO:</b> TETRABORATO DE SÓDIO DECA HIDRATADO (Na₂B₄O₇·10H₂O)<br><br>

    <b>MASSA PESADA:</b> ______ g <br>
    <b>MASSA MOLAR:</b> 381,40 g/mol <br>
    <b>VOLUME DO BALÃO VOLUMÉTRICO:</b> ______ mL <br>
    <b>CONCENTRAÇÃO:</b> #DIV/0! eqg/L <br>
    <b>VOLUME DA ALÍQUOTA:</b> 10,00 mL <br><br>

    <b>1ª TITULAÇÃO</b><br>
    VOLUME DE H₂SO₄ GASTO: ______ mL <br>
    CONCENTRAÇÃO TEÓRICA: 0,02 eqg/L <br>
    CONCENTRAÇÃO REAL: #DIV/0! eqg/L <br><br>

    <b>2ª TITULAÇÃO</b><br>
    VOLUME DE H₂SO₄ GASTO: ______ mL <br>
    CONCENTRAÇÃO TEÓRICA: 0,02 eqg/L <br>
    CONCENTRAÇÃO REAL: #DIV/0! eqg/L <br><br>

    <b>3ª TITULAÇÃO</b><br>
    VOLUME DE H₂SO₄ GASTO: ______ mL <br>
    CONCENTRAÇÃO TEÓRICA: 0,02 eqg/L <br>
    CONCENTRAÇÃO REAL: #DIV/0! eqg/L <br><br>

    <b>REAGENTES UTILIZADOS</b><br>
    ÁCIDO SULFÚRICO 0,1 eqg/L<br>
    ÁCIDO SULFÚRICO 0,02 eqg/L<br>
    TETRABORATO DE SÓDIO DECA HIDRATADO<br>
    ALARANJADO DE METILA<br>
    TAMPÃO FOSFATO 0,5 mol/L<br>
    SOLUÇÃO DE AZUL DE METILENO 0,2%<br>
    SOLUÇÃO DE VERMELHO DE METILA 0,2%<br>
    SOLUÇÃO INDICADORA DE ÁCIDO BÓRICO<br>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ================= CÁLCULO =================
    st.subheader("🧪 CÁLCULO DO N-AMONIACAL")

    massa = st.number_input("Massa (g)", value=0.0)
    volume_balao = st.number_input("Volume do balão (mL)", value=100.0)

    t1 = st.number_input("1ª Titulação", value=0.0)
    t2 = st.number_input("2ª Titulação", value=0.0)
    t3 = st.number_input("3ª Titulação", value=0.0)

    if st.button("CALCULAR"):

        media = np.mean([t1, t2, t3])
        dp = np.std([t1, t2, t3], ddof=1) if len([t1, t2, t3]) > 1 else 0

        if media != 0:
            conc = (massa / 381.40) / (volume_balao / 1000)
            resultado_final = conc * (volume_balao / media)

            st.session_state["n_amoniacal"] = {
                "Concentração": conc,
                "Resultado Final": resultado_final,
                "Média": media,
                "Desvio Padrão": dp
            }

    if "n_amoniacal" in st.session_state:

        st.markdown("### 📄 RESULTADO FINAL")

        for k, v in st.session_state["n_amoniacal"].items():
            st.markdown(f"""
            <div class="card">
            <b>{k}</b><br>
            {v:.4f}
            </div>
            """, unsafe_allow_html=True)
