import streamlit as st
import numpy as np
from datetime import datetime

# ================= CONFIG =================
st.set_page_config(
    page_title="Laboratorio Vitual - CMMA IFRJ",
    layout="wide"
)

# ================= ESTILO =================
st.markdown("""
    <style>
    .main {
        background-color: #f4f7ff;
    }
    h1 {
        color: #1f4e79;
    }
    </style>
""", unsafe_allow_html=True)

# ================= CABEÇALHO =================
st.title("🧪 Laboratório Virtual CMM IFRJ")
st.subheader("Laudo Técnico de Ensaios Físico-Químicos")

st.markdown("""
### 👩‍🏫 Criador
Luciana Oliveira de Albuquerque

### 🎓 Administrador
Raphael Oliveira de Albuquerque
""")

st.success("Sistema ativo 🚀")

# ================= MENU =================
menu = st.sidebar.selectbox(
    "📚 Menu do Sistema",
    ["Início", "Aula Teórica", "Laboratório", "Laudo Final"]
)

# ================= INÍCIO =================
if menu == "Início":
    st.markdown("## 👩‍🔬 Bem-vinda ao Laboratório Virtual")

    st.info("Sistema desenvolvido para ensino de análises físico-químicas de água e resíduos.")

    st.markdown("""
    ### 🎯 Você irá aprender:
    - Cálculo de parâmetros laboratoriais
    - Média e desvio padrão
    - Interpretação de resultados
    - Construção de laudos técnicos
    """)

# ================= AULA TEÓRICA =================
elif menu == "Aula Teórica":
    st.header("📚 Conteúdo Teórico")

    st.write("""
    O monitoramento de resíduos e água envolve análise físico-química para garantir qualidade ambiental.

    Principais parâmetros:
    - ST (Sólidos Totais)
    - STF (Sólidos Totais Fixos)
    - STV (Sólidos Suspensos Totais)
    - SSF (Sólidos Suspensos Fixos)
    - STV (Sólidos Totais Voláteis)
    - SSV (Sólidos Suspensos Voláteis)
    - SDT (Sólidos Dissolvidos Totais)
    - SDV (Sólidos Dissolvidos Voláteis)
    - SDF (Sólidos Dissolvidos Fixos)
    """)

    st.markdown("## 🧪 Recipientes e Equipamentos Utilizados nos Ensaios")

    try:
        st.image("equipamentos.png", use_container_width=True)
    except:
        st.warning("Imagem 'equipamentos.png' não encontrada ou inválida.")

# ================= LABORATÓRIO =================
elif menu == "Laboratório":

    st.header("🧪 Dados Inseridos")

    volume = st.number_input("Volume da amostra (mL)", value=500.0)

    st.markdown("### 📥 Replicatas (2 medições)")
    st.write("Casalola")

    st.subheader("ST (Massas Exprerimentais)")
    m1 = st.number_input("ST1", key="st1")
    m2 = st.number_input("ST2", key="st2")
    m3 = st.number_input("ST3", key="st3")
 
            media, dp = v

            if media < 50:
                classe = "Baixo"
            elif media < 150:
                classe = "Médio"
            else:
                classe = "Alto"

            st.write(f"{k} | {media:.2f} ± {dp:.2f} | {classe}")
