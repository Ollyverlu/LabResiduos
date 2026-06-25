import streamlit as st
import numpy as np
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

st.set_page_config(page_title="LabResiduos IFRJ", layout="wide")

st.title("🧪 Laboratório Virtual de Resíduos – IFRJ Nilópolis")
st.subheader("Luciana Oliveira de Albuquerque")

st.markdown("## Entrada de Dados")

volume = st.number_input("Volume da amostra (mL)", value=500.0)

m_vazia, m_st, m_stf = [], [], []
f_vazio, f_sst, f_ssf = [], [], []

st.markdown("### Cápsula")
for i in range(4):
    st.write(f"Replicata {i+1}")
    m_vazia.append(st.number_input(f"Cápsula vazia {i+1}", key=f"v{i}"))
    m_st.append(st.number_input(f"Cápsula + ST {i+1}", key=f"st{i}"))
    m_stf.append(st.number_input(f"Cápsula + STF {i+1}", key=f"stf{i}"))

st.markdown("### Filtro")
for i in range(4):
    st.write(f"Replicata {i+1}")
    f_vazio.append(st.number_input(f"Filtro vazio {i+1}", key=f"fv{i}"))
    f_sst.append(st.number_input(f"Filtro + SST {i+1}", key=f"sst{i}"))
    f_ssf.append(st.number_input(f"Filtro + SSF {i+1}", key=f"ssf{i}"))

def gerar_pdf(resultados):
    nome_arquivo = "laudo_labresiduos.pdf"
    c = canvas.Canvas(nome_arquivo, pagesize=A4)
    largura, altura = A4

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, altura - 50, "IFRJ - Laboratorio Virtual de Residuos")
    c.setFont("Helvetica", 11)
    c.drawString(50, altura - 70, "Responsavel: Luciana Oliveira de Albuquerque")

    c.drawString(50, altura - 100, f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}")

    y = altura - 140
    c.setFont("Helvetica", 10)

    for k, v in resultados.items():
        c.drawString(50, y, f"{k}: {v:.2f} mg/L")
        y -= 20

    c.save()
    return nome_arquivo

if st.button("CALCULAR E GERAR LAUDO"):

    ST, STF, SST, SSF = [], [], [], []

    for i in range(4):
        st_val = ((m_st[i] - m_vazia[i]) * 1000000) / volume
        stf_val = ((m_stf[i] - m_vazia[i]) * 1000000) / volume
        sst_val = ((f_sst[i] - f_vazio[i]) * 1000000) / volume
        ssf_val = ((f_ssf[i] - f_vazio[i]) * 1000000) / volume

        ST.append(st_val)
        STF.append(stf_val)
        SST.append(sst_val)
        SSF.append(ssf_val)

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
        "ST": np.mean(ST),
        "STF": np.mean(STF),
        "STV": np.mean(STV),
        "SST": np.mean(SST),
        "SSF": np.mean(SSF),
        "SSV": np.mean(SSV),
        "SDT": np.mean(SDT),
        "SDF": np.mean(SDF),
        "SDV": np.mean(SDV)
    }

    st.success("Cálculo concluído!")

    for k, v in resultados.items():
        st.write(f"{k}: {v:.2f} mg/L")

    pdf = gerar_pdf(resultados)

    st.download_button(
        label="📄 Baixar Laudo em PDF",
        file_name=pdf,
        data=open(pdf, "rb").read()
    )
