import streamlit as st
import numpy as np
# ================= CONFIG =================
st.set_page_config(
    page_title="LabResiduos - Laboratório Virtual",
    layout="wide"
)

# ================= CSS =================
st.markdown("""
<style>
.stApp{
    background-color:#e9f5e9;
}

h1{
    color:#0f3d1f !important;
    font-weight:900;
}

.card{
    background:white;
    border-left:6px solid #1b5e20;
    padding:15px;
    border-radius:10px;
    margin-top:10px;
}

.stButton>button{
    background:#1b5e20;
    color:white;
    width:100%;
    height:50px;
    font-weight:bold;
    border-radius:8px;
}
</style>
""", unsafe_allow_html=True)

# ================= CABEÇALHO =================
col1, col2 = st.columns([1, 5])

with col1:
    st.image("logo.png", width=90)

with col2:
    st.title("🧪 IFRJ - LABORATÓRIO VIRTUAL")

    st.markdown("""
**Criado por:** Luciana Oliveira de Albuquerque  
**Professor responsável:** Renato Ribeiro  
**Administrador do sistema:** Raphael Oliveira de Albuquerque  
""")

st.markdown("---")

# ================= MENU =================
menu = st.sidebar.radio(
    "📚 Sistema Laboratorial",
    [
        "🏠 Dashboard",
        "🧪 Sólidos Totais",
        "🧪 Sólidos Suspensos",
        "🧪 N-Amoniacal",
        "🧪 NTK",
        "🧪 NHX",
        "🧪 DQO",
        "📊 Planilhas Interativas (Excel)"
    ]
)

# ================= HEADER =================
def header(titulo):
    st.title(f"DETERMINAÇÃO DE {titulo}")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.text_input("Responsável", key=f"resp_{titulo}")
    with col2:
        st.text_input("Projeto", key=f"proj_{titulo}")
    with col3:
        st.date_input("Data da Análise", key=f"data_{titulo}")
    with col4:
        st.time_input("Hora da Análise", key=f"hora_{titulo}")

    st.markdown("---")

# ================= DASHBOARD =================
if menu == "🏠 Dashboard":
    st.title("Sistema Laboratorial")
    st.info("Selecione um módulo no menu lateral.")
