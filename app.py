import streamlit as st
import numpy as np
from datetime import datetime

st.set_page_config(page_title="Laudo Técnico IFRJ", layout="wide")

st.title("🧪 Laudo Técnico de Ensaios Físico-Químicos")
st.write("Água e Resíduos – Laboratório Virtual IFRJ")
st.write("Responsável: Luciana Oliveira de Albuquerque")

st.sidebar.header("📊 Entrada de Dados")

n = 4  # replicatas

volume = st.sidebar.number_input("Volume da amostra (mL)", value=500.0)

# listas
massa_ST = []
massa_STF = []
massa_SST = []
massa_SSF = []

st.header("📥 Inserção de Dados")

for i in range(n):
    st.subheader(f"Replicata {i+1}")

    st.write("Cápsula")
    st1 = st.number_input(f"ST {i+1}", key=f"st{i}")
    st2 = st.number_input(f"STF {i+1}", key=f"stf{i}")

    st.write("Filtro")
    sst = st.number_input(f"SST {i+1}", key=f"sst{i}")
    ssf = st.number_input(f"SSF {i+1}", key=f"ssf{i}")

    massa_ST.append(st1)
    massa_STF.append(st2)
    massa_SST.append(sst)
    massa_SSF.append(ssf)

# ================= CÁLCULOS =================

def calc(lista):
    arr = np.array(lista)
    media = np.mean(arr)
    desvio = np.std(arr)
    return media, desvio

if st.button("🧪 GERAR LAUDO COMPLETO"):

    ST_med, ST_dp = calc(massa_ST)
    STF_med, STF_dp = calc(massa_STF)
    SST_med, SST_dp = calc(massa_SST)
    SSF_med, SSF_dp = calc(massa_SSF)

    # cálculos derivados
    STV_med = ST_med - STF_med
    SSV_med = SST_med - SSF_med
    SDT_med = ST_med - SST_med
    SDF_med = STF_med - SSF_med
    SDV_med = STV_med - SSV_med

    st.success("✔ Laudo gerado com sucesso!")

    st.subheader("📊 RESULTADOS – PARÂMETROS")

    tabela = {
        "ST": (ST_med, ST_dp),
        "STF": (STF_med, STF_dp),
        "SST": (SST_med, SST_dp),
        "SSF": (SSF_med, SSF_dp),
        "STV": (STV_med, 0),
        "SSV": (SSV_med, 0),
        "SDT": (SDT_med, 0),
        "SDF": (SDF_med, 0),
        "SDV": (SDV_med, 0),
    }

    st.markdown("### 📄 Laudo Técnico Final")

    st.write("**Parâmetro | Unidade | Resultado (média ± desvio) | Classificação**")

    for k, v in tabela.items():
        media, dp = v

        # classificação simples técnica (você pode ajustar depois)
        if media < 50:
            classe = "Baixo"
        elif media < 150:
            classe = "Médio"
        else:
            classe = "Alto"

        st.write(f"{k} | mg/L | {media:.2f} ± {dp:.2f} | {classe}")

    st.info("📌 Relatório técnico gerado conforme padrão de laboratório físico-químico")
