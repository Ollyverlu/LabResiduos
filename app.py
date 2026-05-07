import streamlit as st
import numpy as np
from datetime import datetime

# ================= CONFIG =================
st.set_page_config(
    page_title="Laboratório Virtual de Resíduos IFRJ",
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
st.title("🧪 Laboratório Virtual de Resíduos – IFRJ")
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
    - SST (Sólidos Suspensos Totais)
    - SSF (Sólidos Suspensos Fixos)
    - STV (Sólidos Totais Voláteis)
    - SSV (Sólidos Suspensos Voláteis)
    - SDT (Sólidos Dissolvidos Totais)
    - SDV (Sólidos Dissolvidos Voláteis)
    - SDF (Sólidos Dissolvidos Fixos)

    Esses dados permitem avaliar a qualidade da água e resíduos industriais.
    """)

    st.markdown("## 🧪 Recipientes e Equipamentos Utilizados nos Ensaios")
    st.image("equipamentos.png", use_container_width=True)

# ================= LABORATÓRIO =================
elif menu == "Laboratório":

    st.header("🧪 Inserção de Dados Experimentais")

    volume = st.number_input("Volume da amostra (mL)", value=500.0000, format="%.4f")

    st.markdown("### 📥 Replicatas (4 medições)")

    st.write("Cápsula / Filtro - Inserção dos valores")

    st.subheader("ST (Sólidos Totais)")
    st1 = st.number_input("ST1", key="st1", format="%.4f")
    st2 = st.number_input("ST2", key="st2", format="%.4f")
    st3 = st.number_input("ST3", key="st3", format="%.4f")
    st4 = st.number_input("ST4", key="st4", format="%.4f")

    st.subheader("STF (Sólidos Totais Fixos)")
    f1 = st.number_input("STF1", key="f1", format="%.4f")
    f2 = st.number_input("STF2", key="f2", format="%.4f")
    f3 = st.number_input("STF3", key="f3", format="%.4f")
    f4 = st.number_input("STF4", key="f4", format="%.4f")

    st.subheader("SST (Sólidos Suspensos Totais)")
    sst1 = st.number_input("SST1", key="s1", format="%.4f")
    sst2 = st.number_input("SST2", key="s2", format="%.4f")
    sst3 = st.number_input("SST3", key="s3", format="%.4f")
    sst4 = st.number_input("SST4", key="s4", format="%.4f")

    st.subheader("SSF (Sólidos Suspensos Fixos)")
    ssf1 = st.number_input("SSF1", key="x1", format="%.4f")
    ssf2 = st.number_input("SSF2", key="x2", format="%.4f")
    ssf3 = st.number_input("SSF3", key="x3", format="%.4f")
    ssf4 = st.number_input("SSF4", key="x4", format="%.4f")

    if st.button("🧪 GERAR RESULTADOS"):

        ST = np.array([st1, st2, st3, st4])
        STF = np.array([f1, f2, f3, f4])
        SST = np.array([sst1, sst2, sst3, sst4])
        SSF = np.array([ssf1, ssf2, ssf3, ssf4])

        # cálculos principais
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

# ================= LAUDO FINAL =================
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

            st.write(f"{k} | {media:.4f} ± {dp:.4f} | {classe}")
