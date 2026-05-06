mimport streamlit as st

st.set_page_config(page_title="Laboratório Virtual de Resíduos", layout="wide")

# MENU
menu = st.sidebar.selectbox(
    "📚 Menu do Laboratório",
    [
        "Início",
        "Conteúdo Teórico",
        "Tipos de Resíduos",
        "Atividade Prática",
        "Quiz Final"
    ]
)

# INÍCIO
if menu == "Início":
    st.title("📚 Laboratório Virtual de Resíduos")
    st.write("Bem-vinda ao sistema de estudo e treinamento interativo 👩‍🔬")

    st.info("Aqui você vai aprender na prática sobre resíduos e descarte correto.")
    st.success("Sistema pronto para estudo 🚀")

# CONTEÚDO TEÓRICO
elif menu == "Conteúdo Teórico":
    st.header("📖 Conteúdo Teórico")

    st.write("""
    O gerenciamento de resíduos é essencial para o meio ambiente.
    Ele envolve coleta, separação, reciclagem e descarte correto.
    """)

    st.subheader("Objetivos")
    st.write("""
    - Reduzir impactos ambientais  
    - Promover reciclagem  
    - Evitar contaminação do solo e água  
    """)

# TIPOS DE RESÍDUOS
elif menu == "Tipos de Resíduos":
    st.header("♻️ Tipos de Resíduos")

    st.write("Selecione um tipo para aprender:")

    tipo = st.selectbox(
        "Escolha:",
        ["Orgânico", "Plástico", "Vidro", "Metal", "Eletrônico"]
    )

    if tipo == "Orgânico":
        st.success("Restos de alimentos, cascas e materiais biodegradáveis.")
    elif tipo == "Plástico":
        st.warning("Demora anos para decompor. Deve ser reciclado.")
    elif tipo == "Vidro":
        st.info("100% reciclável sem perda de qualidade.")
    elif tipo == "Metal":
        st.info("Pode ser reciclado várias vezes.")
    elif tipo == "Eletrônico":
        st.error("Necessita descarte especial devido a componentes tóxicos.")

# ATIVIDADE PRÁTICA
elif menu == "Atividade Prática":
    st.header("🧪 Atividade Prática")

    st.write("Classifique corretamente o resíduo:")

    pergunta = st.radio(
        "Uma casca de banana é:",
        ["Plástico", "Orgânico", "Metal", "Vidro"]
    )

    if st.button("Responder"):
        if pergunta == "Orgânico":
            st.success("✔ Correto! Resíduo orgânico.")
        else:
            st.error("❌ Resposta incorreta. A resposta correta é Orgânico.")

# QUIZ FINAL
elif menu == "Quiz Final":
    st.header("🏁 Quiz Final")

    q1 = st.radio(
        "Qual resíduo é reciclável infinitamente?",
        ["Plástico", "Vidro", "Orgânico", "Tecido"]
    )

    if st.button("Finalizar"):
        if q1 == "Vidro":
            st.success("✔ Excelente! Você acertou.")
        else:
            st.error("❌ Resposta correta: Vidro.")
