import streamlit as st
import numpy as np
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

st.set_page_config(page_title="LabResíduos IFRJ", layout="wide")

menu = st.sidebar.selectbox(
    "📚 Menu do Laboratório",
    ["Início", "Aula Teórica", "Laboratório de Cálculo", "Download PDF"]
)

# ================= INÍCIO =================
if menu == "Início":
    st.title("🧪 Laboratório Virtual de Resíduos – IFRJ")
    st.write("Bem-vinda ao sistema completo de ensino e prática 👩‍🔬")

    st.success("Sistema de aprendizagem + laboratório ativo 🚀")

# ================= AULA =================
elif menu == "Aula Teórica":
    st.header("📚 Aula Teórica")

    st.write("""
    O gerenciamento de resíduos envolve:
    - Coleta
    - Separação
    - Tratamento
    - Descarte correto

    Isso reduz impactos ambientais e protege a saúde pública.
    """)

    st.info("Objetivo: aprender teoria + prática integrada")

# ================= LABORATÓRIO =================
elif menu == "Laboratório de Cálculo":

    st.header("🧪 Cálculos de Resíduos")

    volume = st.number_input("Volume da amostra (mL)", value=500.0)

    m_vazia, m_st, m_stf = [], [], []
    f_vazio, f_sst, f_ssf = [], [], []

    st.subheader("Cápsula")
    for i in range(2):
        st.write(f"Replicata {i+1}")
        m_vazia.append(st.number_input(f"Cápsula vazia {i+1}", key=f"cv{i}"))
        m_st.append(st.number_input(f"Cápsula + ST {i+1}", key=f"cst{i}"))
        m_stf.append(st.number_input(f"Cápsula + STF {i+1}", key=f"cstf{i}"))

    st.subheader("Filtro")
    for i in range(2):
        st.write(f"Replicata {i+1}")
        f_vazio.append(st.number_input(f"Filtro vazio {i+1}", key=f"fv{i}"))
        f_sst.append(st.number_input(f"Filtro + SST {i+1}", key=f"fst{i}"))
        f_ssf.append(st.number_input(f"Filtro + SSF {i+1}", key=f"fssf{i}"))

    if st.button("CALCULAR RESULTADOS"):

        ST, STF, SST, SSF = [], [], [], []

        for i in range(2):
            ST.append((m_st[i] - m_vazia[i]) * 1000000 / volume)
            STF.append((m_stf[i] - m_vazia[i]) * 1000000 / volume)
            SST.append((f_sst[i] - f_vazio[i]) * 1000000 / volume)
            SSF.append((f_ssf[i] - f_vazio[i]) * 1000000 / volume)

        ST = np.array(ST)
        STF = np.array(STF)
        SST = np.array(SST)
        SSF = np.array(SSF)

        resultados = {
            "ST": np.mean(ST),
            "STF": np.mean(STF),
            "SST": np.mean(SST),
            "SSF": np.mean(SSF)
        }

        st.success("Cálculo concluído!")

        for k, v in resultados.items():
            st.write(f"{k}: {v:.2f} mg/L")

        # salvar para PDF
        st.session_state["resultados"] = resultados

# ================= PDF =================
elif menu == "Download PDF":

    st.header("📄 Gerar Laudo PDF")

    if "resultados" in st.session_state:

        def gerar_pdf(resultados):
            nome = "laudo_labresiduos.pdf"
            c = canvas.Canvas(nome, pagesize=A4)

            c.drawString(50, 800, "IFRJ - Laboratório Virtual de Resíduos")
            c.drawString(50, 780, f"Data: {datetime.now()}")

            y = 740
            for k, v in resultados.items():
                c.drawString(50, y, f"{k}: {v:.2f} mg/L")
                y -= 20

            c.save()
            return nome

        pdf = gerar_pdf(st.session_state["resultados"])

        st.download_button(
            "📥 Baixar PDF",
            data=open(pdf, "rb").read(),
            file_name=pdf
        )

    else:
        st.warning("Primeiro faça os cálculos no laboratório.")m
