import streamlit as st
import numpy as np
from datetime import datetime

st.set_page_config(
    page_title="Laudo IFRJ - Laboratório Virtual",
    layout="wide"
)

# ===== ESTILO VISUAL =====
st.markdown("""
    <style>
    .main {
        background-color: #f5f7ff;
    }
    .stTitle {
        color: #1f4e79;
    }
    </style>
""", unsafe_allow_html=True)

# ===== CABEÇALHO =====
st.title("🧪 Laboratório Virtual de Resíduos – IFRJ")
st.subheader("📊 Laudo Técnico de Ensaios Físico-Químicos")

st.success("Sistema interativo ativo 🚀")

# ===== MENU LATERAL =====
menu = st.sidebar.selectbox(
    "📚 Navegação",
    ["Início", "Inserção de Dados", "Resultados"]
)

# ===== INÍCIO =====
if menu == "Início":
    st.markdown("## 👩‍🔬 Bem-vinda ao Laboratório Virtual")
    st.info("Aqui você realiza análises físico-químicas com base em dados reais de laboratório.")

    st.markdown("### 🎯 O que você vai aprender:")
    st.write("""
    - Cálculo de parâmetros laboratoriais  
    - Interpretação de resultados  
    - Construção de laudos técnicos  
    """)

# ===== ENTRADA DE DADOS =====
elif menu == "Inserção de Dados":

    st.markdown("## 📥 Entrada de Dados")

    volume = st.number_input("Volume da amostra (mL)", value=500.0)

    st.markdown("### 🧪 Replicatas")

    st.write("Insira os valores com atenção")

    m1 = st.number_input("ST 1", key="1")
    m2 = st.number_input("ST 2", key="2")
    m3 = st.number_input("ST 3", key="3")
    m4 = st.number_input("ST 4", key="4")

    if st.button("💾 Salvar Dados"):
        st.session_state["dados"] = [m1, m2, m3, m4, volume]
        st.success("Dados salvos com sucesso!")

# ===== RESULTADOS =====
elif menu == "Resultados":

    st.markdown("## 📊 Resultados do Laudo")

    if "dados" in st.session_state:

        dados = st.session_state["dados"]

        valores = np.array(dados[:4])

        media = np.mean(valores)
        desvio = np.std(valores)

        st.metric("📌 Média", f"{media:.2f} mg/L")
        st.metric("📌 Desvio padrão", f"{desvio:.2f} mg/L")

        st.success("✔ Laudo gerado com sucesso")

    else:
        st.warning("⚠ Insira os dados primeiro no menu anterior")
