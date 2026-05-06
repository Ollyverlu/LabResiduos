import streamlit as st
import numpy as np
from datetime import datetime
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import io

# ================= CONFIG =================
st.set_page_config(
    page_title="Laboratório Virtual IFRJ",
    layout="wide"
)

# ================= LOGIN SIMPLES =================
USUARIOS = {
    "raphael": "1234",
    "aluno2": "1234"
}

if "logado" not in st.session_state:
    st.session_state["logado"] = False
    st.session_state["usuario"] = ""

if not st.session_state["logado"]:

    st.title("🔐 Login - Laboratório IFRJ")

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):

        if usuario in USUARIOS and USUARIOS[usuario] == senha:
            st.session_state["logado"] = True
            st.session_state["usuario"] = usuario
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos")

    st.stop()

# ================= CABEÇALHO =================
st.title("🧪 Laboratório Virtual de Resíduos IFRJ")

st.markdown(f"""
👤 Aluno logado: **{st.session_state['usuario']}**  
👩‍🏫 Professora: Luciana Oliveira de Albuquerque
""")

st.success("Sistema ativo 🚀")

# ================= MENU =================
menu = st.sidebar.selectbox(
    "📚 Menu",
    ["Início", "Laboratório", "Gráficos", "Laudo PDF", "Certificado"]
)

# ================= INÍCIO =================
if menu == "Início":
    st.info("Bem-vindo ao laboratório virtual interativo.")

# ================= LABORATÓRIO =================
elif menu == "Laboratório":

    st.header("🧪 Inserção de Dados")

    st.markdown("### ST / STF / SST / SSF")

    ST = [st.number_input(f"ST{i+1}", key=f"st{i}") for i in range(4)]
    STF = [st.number_input(f"STF{i+1}", key=f"f{i}") for i in range(4)]
    SST = [st.number_input(f"SST{i+1}", key=f"s{i}") for i in range(4)]
    SSF = [st.number_input(f"SSF{i+1}", key=f"x{i}") for i in range(4)]

    if st.button("Gerar Cálculos"):

        ST = np.array(ST)
        STF = np.array(STF)
        SST = np.array(SST)
        SSF = np.array(SSF)

        st.session_state["dados"] = {
            "ST": ST,
            "STF": STF,
            "SST": SST,
            "SSF": SSF
        }

        st.success("Dados salvos!")

# ================= GRÁFICOS =================
elif menu == "Gráficos":

    st.header("📊 Gráficos Automáticos")

    if "dados" in st.session_state:

        dados = st.session_state["dados"]

        df = pd.DataFrame({
            "ST": dados["ST"],
            "STF": dados["STF"],
            "SST": dados["SST"],
            "SSF": dados["SSF"]
        })

        st.line_chart(df)

    else:
        st.warning("Gere os dados primeiro no laboratório.")

# ================= PDF LAUDO =================
elif menu == "Laudo PDF":

    st.header("📄 Laudo Técnico PDF")

    if "dados" in st.session_state:

        dados = st.session_state["dados"]

        buffer = io.BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=A4)

        pdf.drawString(50, 800, "IFRJ - Laudo Técnico de Resíduos")
        pdf.drawString(50, 780, f"Aluno: {st.session_state['usuario']}")
        pdf.drawString(50, 760, f"Data: {datetime.now()}")

        pdf.drawString(50, 720, f"ST Média: {np.mean(dados['ST']):.2f}")
        pdf.drawString(50, 700, f"STF Média: {np.mean(dados['STF']):.2f}")
        pdf.drawString(50, 680, f"SST Média: {np.mean(dados['SST']):.2f}")
        pdf.drawString(50, 660, f"SSF Média: {np.mean(dados['SSF']):.2f}")

        pdf.save()

        st.download_button(
            "📥 Baixar PDF",
            data=buffer.getvalue(),
            file_name="laudo.pdf",
            mime="application/pdf"
        )

    else:
        st.warning("Sem dados ainda.")

# ================= CERTIFICADO =================
elif menu == "Certificado":

    st.header("🏆 Certificado de Conclusão")

    st.success(f"""
    Certificamos que o aluno {st.session_state['usuario']}  
    concluiu o Laboratório Virtual de Resíduos IFRJ.
    """)

    st.download_button(
        "Baixar Certificado",
        data=f"Certificado do aluno {st.session_state['usuario']}",
        file_name="certificado.txt"
    )
