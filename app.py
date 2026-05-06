import streamlit as st

st.set_page_config(page_title="Laboratório Virtual de Resíduos", layout="wide")

menu = st.sidebar.selectbox(
    "📚 Menu do Laboratório",
    ["Início", "Conteúdo Teórico", "Tipos de Resíduos", "Atividade Prática", "Quiz Final"]
)

# INÍCIO
if menu == "Início":
    st.title("📚 Laboratório Virtual de Resíduos")
    st.write("Bem-vinda ao sistema de estudo e treinamento interativo 👩‍🔬")
    st.success("Sistema pronto para estudo 🚀")

# TEORIA
elif menu == "Conteúdo Teórico":
    st.header("📖 Conteúdo Teórico")
    st.write("O gerenciamento de resíduos envolve coleta, separação e descarte correto.")
    st.info("Objetivo: reduzir impactos ambientais.")

# TIPOS
elif menu == "Tipos de Resíduos":
    st.header("♻️ Tipos de Resíduos")

    tipo = st.selectbox("Escolha um tipo:", ["Orgânico", "Plástico", "Vidro", "Metal", "Eletrônico"])

    if tipo == "Orgânico":
        st.success("Restos de alimentos e materiais biodegradáveis.")
    elif tipo == "Plástico":
        st.warning("Demora muito para decompor.")
    elif tipo == "Vidro":
        st.info("Reciclável infinitamente.")
    elif tipo == "Metal":
        st.info("Reciclável várias vezes.")
    elif tipo == "Eletrônico":
        st.error("Descarte especial necessário.")

# ATIVIDADE
elif menu == "Atividade Prática":
    st.header("🧪 Atividade Prática")

    resposta = st.radio("Casca de banana é:", ["Plástico", "Orgânico", "Vidro"])

    if st.button("Responder"):
        if resposta == "Orgânico":
            st.success("✔ Correto!")
        else:
            st.error("❌ Resposta correta: Orgânico")

# QUIZ
elif menu == "Quiz Final":
    st.header("🏁 Quiz Final")

    q1 = st.radio("Qual é reciclável infinitamente?", ["Plástico", "Vidro", "Orgânico"])

    if st.button("Finalizar"):
        if q1 == "Vidro":
            st.success("✔ Você acertou!")
        else:
            st.error("❌ Resposta correta: Vidro")
