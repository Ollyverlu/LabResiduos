import streamlit as st
import numpy as np
from datetime import datetime

# ================= CONFIG =================
st.set_page_config(
    page_title="Laboratório Virtual IFRJ",
    layout="wide"
)

# ================= ESTILO VISUAL =================
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
st.title("🧪 Laboratório Virtual de Resíduos – IFRJ")
st.subheader("Laudo Técnico de Ensaios Físico-Químicos")
st.write("Responsável: Luciana Oliveira de Albuquerque")

st.success("Sistema ativo 🚀")

# ================= MENU =================
menu = st.sidebar.selectbox(
    "📚 Menu do Sistema",
    ["Início", "Aula Teórica", "Laboratório", "Laudo Final", "Compartilhar"]
)

# ================= INÍCIO =================
if menu == "Início":
    st.markdown("## 👩‍🔬 Bem-vinda ao Laboratório Virtual")

    st.info("Sistema completo para ensino de análises físico-químicas de água e resíduos.")

    st.markdown("""
    ### 🎯 Você vai aprender:
    - Cálculos laboratoriais  
    - Média e desvio padrão  
    - Interpretação de resultados  
    - Construção de laudos técnicos  
    """)

# ================= AULA =================
elif menu == "Aula Teórica":
    st.header("📚 Conteúdo Teórico")

    st.write("""
    O controle de qualidade da água e resíduos envolve análises físico-químicas.

    Principais parâmetros:
    - ST (Sólidos Totais)
    - STF (Sólidos Totais Fixos)
    - SST (Sólidos Suspensos Totais)
    - SSF (Sólidos Suspensos Fixos)

    Esses dados são fundamentais para avaliação ambiental.
    """)

# ================= LABORATÓRIO =================
elif menu == "Laboratório":

    st.header("🧪 Inserção de Dados")

    volume = st.number_input("Volume da amostra (mL)", value=500.0)

    st.subheader("📥 Replicatas (ST / STF / SST / SSF)")

    st.write("Insira os valores experimentais")

    ST = [st.number_input(f"ST {i+1}", key=f"st{i}") for i in range(4)]
    STF = [st.number_input(f"STF {i+1}", key=f"stf{i}") for i in range(4)]
    SST = [st.number_input(f"SST {i+1}", key=f"sst{i}") for i in range(4)]
    SSF = [st.number_input(f"SSF {i+1}", key=f"ssf{i}") for i in range(4)]

    if st.button("🧪 GERAR RESULTADOS"):

        ST = np.array(ST)
        STF = np.array(STF)
        SST = np.array(SST)
        SSF = np.array(SSF)

        STV = ST - STF
        SSV = SST - SSF
        SDT = ST - SST
        SDF = STF - SSF
        SDV = STV - SSV

        resultados = {
            "ST": (np.mean(ST), np.std(ST)),
            "STF": (np.mean(STF), np.std(STF)),
            "SST": (np.mean(SST), np.std(SST)),
            "SSF": (np.mean(SSF), np.std(SSF)),
            "STV": (np.mean(STV), 0),
            "SSV": (np.mean(SSV), 0),
            "SDT": (np.mean(SDT), 0),
            "SDF": (np.mean(SDF), 0),
            "SDV": (np.mean(SDV), 0),
        }

        st.session_state["resultados"] = resultados

        st.success("✔ Cálculos concluídos com sucesso!")

# ================= LAUDO =================
elif menu == "Laudo Final":

    st.header("📄 Laudo Técnico Final")

    if "resultados" in st.session_state:

        st.write("**Parâmetro | Resultado (média ± desvio) | Classificação**")

        for k, v in st.session_state["resultados"].items():

            media, dp = v

            if media < 50:
                classe = "Baixo"
            elif media < 150:
                classe = "Médio"
            else:
                classe = "Alto"

            st.write(f"{k} | {media:.2f} ± {dp:.2f} | {classe}")

        st.success("📊 Laudo gerado com sucesso!")

    else:
        st.warning("⚠ Execute os cálculos primeiro no laboratório")

# ================= COMPARTILHAR =================
elif menu == "Compartilhar":

    st.header("📲 Compartilhar com Alunos")

    link = "https://SEU-LINK-AQUI.streamlit.app/"

    st.write("Envie este laboratório para seus alunos:")

    st.code(link)

    st.markdown("### 💬 WhatsApp")

    mensagem = f"📚 Laboratório Virtual IFRJ\nAcesse aqui: {link}"

    st.write("Clique e copie a mensagem abaixo:")

    st.code(mensagem)

    st.info("Depois cole no WhatsApp para seus alunos 👩‍🎓")
