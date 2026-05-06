import streamlit as st

st.set_page_config(page_title="Laboratório Virtual de Resíduos", layout="wide")

menu = st.sidebar.selectbox(
    "📚 Menu do Laboratório",
    ["Início", "Conteúdo Teórico", "Tipos de Resíduos", "Atividade Prática", "Quiz Final"]
)m

if menu == "Início":
    st.title("📚 Laboratório Virtual de Resíduos")
    st.write("Bem-vinda ao sistema de estudo e treinamento interativo 👩‍🔬")
    st.success("Sistema pronto para estudo 🚀")
