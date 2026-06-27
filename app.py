import streamlit as st
import numpy as np
import pandas as pd
from io import BytesIO

# ================= CONFIG =================
st.set_page_config(page_title=" - LabResiduos -Laboratorio Virtual ", layout="wide")

# ================= CSS =================
st.markdown("""
<style>
.stApp {
    background-color: #e9f5e9;
}

h1 {
    color: #0f3d1f !important;
    font-weight: 900;
}

.card {
    background: white;
    border-left: 6px solid #1b5e20;
    padding: 15px;
    border-radius: 10px;
    margin-top: 10px;
}

.stButton>button {
    background: #1b5e20;
    color: white;
    width: 100%;
    height: 50px;
    font-weight: bold;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# ================= CABEÇALHO =================
col1, col2 = st.columns([1, 5])

with col1:
    st.image("logo.png", width=90)

with col2:
    st.title("🧪IFRJ - LABORATÓRIO VIRTUAL ")
    st.markdown("""
**Criado por:** Luciana Oliveira de Albuquerque  
**Professor responsável:** Renato Ribeiro  
**Administrador do sistema:** Aluno:Raphael Oliveira de Albuquerque  
""")

st.markdown("---")

# ================= MENU =================
menu = st.sidebar.radio("📚 Sistema Laboratorial ", [
    "🏠 Dashboard",
    "🧪 Sólidos Totais",
    "🧪 Sólidos Suspensos",
    "🧪 N-Amoniacal",
    "🧪 NTK",
    "🧪 NHX",
    "🧪 DQO",
    "📊 Planilhas Interativas (Excel)"
])

# ================= HEADER =================
def header(titulo):
    st.title(f"DETERMINAÇÃO DE {titulo}")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.text_input("Responsável", key=f"resp_{titulo}")
    with col2:
        st.text_input("Projeto", key=f"proj_{titulo}")
    with col3:
        st.date_input("Data da Análise", key=f"data_{titulo}")
    with col4:
        st.time_input("Hora da Análise", key=f"hora_{titulo}")

    st.markdown("---")

# ================= DASHBOARD =================
if menu == "🏠 Dashboard":
    st.title("Sistema Laboratorial")
    st.info("Selecione um módulo no menu lateral.")

# ================= SÓLIDOS TOTAIS =================
elif menu == "🧪 Sólidos Totais":
    header("SÓLIDOS TOTAIS")

    v = st.number_input("Volume (mL)", value=50.0)

    m1 = st.number_input("m1")
    m2 = st.number_input("m2")
    m3 = st.number_input("m3")

    m1_2 = st.number_input("m1 (rep 2)")
    m2_2 = st.number_input("m2 (rep 2)")
    m3_2 = st.number_input("m3 (rep 2)")

    if st.button("Calcular"):
        fator = 1000 / (v / 1000)

        st1 = (m2 - m1) * fator
        st2 = (m2_2 - m1_2) * fator

        stf1 = (m3 - m1) * fator
        stf2 = (m3_2 - m1_2) * fator

        stv1 = st1 - stf1
        stv2 = st2 - stf2

        st.markdown(f"""
        <div class="card">
        ST: {np.mean([st1, st2]):.2f} ± {np.std([st1, st2], ddof=1):.2f}<br>
        STF: {np.mean([stf1, stf2]):.2f} ± {np.std([stf1, stf2], ddof=1):.2f}<br>
        STV: {np.mean([stv1, stv2]):.2f} ± {np.std([stv1, stv2], ddof=1):.2f}
        </div>
        """, unsafe_allow_html=True)

# ================= SÓLIDOS SUSPENSOS =================
elif menu == "🧪 Sólidos Suspensos":
    header("SÓLIDOS SUSPENSOS")

    v = st.number_input("Volume (mL)", value=50.0)

    m1 = st.number_input("m1")
    m2 = st.number_input("m2")
    m3 = st.number_input("m3")

    m1_2 = st.number_input("m1 (rep 2)")
    m2_2 = st.number_input("m2 (rep 2)")
    m3_2 = st.number_input("m3 (rep 2)")

    if st.button("Calcular"):
        fator = 1000 / (v / 1000)

        ss1 = (m2 - m1) * fator
        ss2 = (m2_2 - m1_2) * fator

        ssf1 = (m3 - m1) * fator
        ssf2 = (m3_2 - m1_2) * fator

        ssv1 = ss1 - ssf1
        ssv2 = ss2 - ssf2

        st.markdown(f"""
        <div class="card">
        SS: {np.mean([ss1, ss2]):.2f} ± {np.std([ss1, ss2], ddof=1):.2f}<br>
        SSF: {np.mean([ssf1, ssf2]):.2f} ± {np.std([ssf1, ssf2], ddof=1):.2f}<br>
        SSV: {np.mean([ssv1, ssv2]):.2f} ± {np.std([ssv1, ssv2], ddof=1):.2f}
        </div>
        """, unsafe_allow_html=True)

# ================= N-AMONIACAL =================
elif menu == "🧪 N-Amoniacal":
    header("NITROGÊNIO AMONIACAL")

    m = st.number_input("Massa")
    v = st.number_input("Volume")

    t1 = st.number_input("Titulação 1")
    t2 = st.number_input("Titulação 2")
    t3 = st.number_input("Titulação 3")

    if st.button("Calcular N-Amoniacal"):
        media = np.mean([t1, t2, t3])
        if media != 0:
            resultado = (m / 381.4) / (v / 1000) * media
            st.success(f"Resultado: {resultado:.4f}")

# ================= NTK =================
elif menu == "🧪 NTK":
    header("NITROGÊNIO TOTAL KJELDAHL")

    m = st.number_input("Massa")
    v = st.number_input("Volume")

    t1 = st.number_input("Titulação 1")
    t2 = st.number_input("Titulação 2")
    t3 = st.number_input("Titulação 3")

    if st.button("Calcular NTK"):
        media = np.mean([t1, t2, t3])
        if media != 0:
            resultado = (m / 381.4) / (v / 1000) * media
            st.success(f"Resultado: {resultado:.4f}")

# ================= NHX =================
elif menu == "🧪 NHX":
    header("NITROGÊNIO NHX")

    m = st.number_input("Massa")
    v = st.number_input("Volume")

    t1 = st.number_input("Titulação 1")
    t2 = st.number_input("Titulação 2")
    t3 = st.number_input("Titulação 3")

    if st.button("Calcular NHX"):
        media = np.mean([t1, t2, t3])
        if media != 0:
            resultado = (m / 381.4) / (v / 1000) * media
            st.success(f"Resultado: {resultado:.4f}")

# ================= DQO =================
elif menu == "🧪 DQO":
    header("DEMANDA QUÍMICA DE OXIGÊNIO")

    m = st.number_input("Massa padrão")
    v = st.number_input("Volume amostra")

    t1 = st.number_input("Titulação 1")
    t2 = st.number_input("Titulação 2")
    t3 = st.number_input("Titulação 3")

    if st.button("Calcular DQO"):
        media = np.mean([t1, t2, t3])
        if media != 0:
            resultado = (m * 0.25) / media
            st.success(f"Resultado: {resultado:.4f}")

# ================= PLANILHAS INTERATIVAS =================
elif menu == "📊 Planilhas Interativas (Excel)":

    import streamlit as st
    import numpy as np
    
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
def gerar_pdf(titulo, dados):

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    # TÍTULO
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, 750, titulo)

    # CONTEÚDO
    pdf.setFont("Helvetica", 10)

    y = 700

    for item in dados:
        pdf.drawString(50, y, str(item))
        y -= 20

        # evita sair da página
        if y < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 10)
            y = 750

    pdf.save()
    buffer.seek(0)

    return buffer
    st.title("🧪 LABORATÓRIO VIRTUAL - PLANILHAS INTERATIVAS")

    st.markdown("══════════════════════════════════════")

    # ================= ABAS =================
    aba1, aba2, aba3 = st.tabs(["🧪 N-Amoniacal", "🧪 NTK", "🧪 DQO"])

    # =========================================================
    # 🧪 N-AMONIACAL
    # =========================================================
    with aba1:

        st.subheader("DETERMINAÇÃO DE NITROGÊNIO AMONIACAL")

        responsavel = st.text_input("Responsável", key="na_resp")
        projeto = st.text_input("Projeto", key="na_proj")
        data = st.date_input("Data", key="na_data")
        hora = st.time_input("Hora", key="na_hora")

        massa_pesada = st.number_input("Massa pesada (g)", key="na_massa", min_value=0.0)
        massa_molar = st.number_input("Massa molar", value=381.40, key="na_mm")
        volume_balao = st.number_input("Volume do balão (mL)", key="na_vol", min_value=0.0)

        t1 = st.number_input("1ª Titulação", key="na_t1")
        t2 = st.number_input("2ª Titulação", key="na_t2")
        t3 = st.number_input("3ª Titulação", key="na_t3")

        if massa_pesada > 0 and volume_balao > 0:
            conc = (massa_pesada / massa_molar) / (volume_balao / 1000)
            st.success(f"Concentração: {conc:.6f}")
        else:
            conc = None

        if t1 and t2 and t3:
            media = np.mean([t1, t2, t3])
            desvio = np.std([t1, t2, t3], ddof=1)
            st.write(f"Média: {media:.2f}")
            st.write(f"Desvio: {desvio:.2f}")

            if conc:
                resultado = (massa_pesada / 381.4) * media
                st.success(f"Resultado N-Amoniacal: {resultado:.4f} mg/L")

    # =========================================================
    # 🧪 NTK
    # =========================================================
    with aba2:

        st.subheader("NITROGÊNIO TOTAL KJELDAHL (NTK)")

        responsavel2 = st.text_input("Responsável", key="ntk_resp")
        projeto2 = st.text_input("Projeto", key="ntk_proj")

        massa = st.number_input("Massa (g)", key="ntk_massa", min_value=0.0)
        volume = st.number_input("Volume (L)", key="ntk_vol", min_value=0.0)

        t1 = st.number_input("1ª Titulação", key="ntk_t1")
        t2 = st.number_input("2ª Titulação", key="ntk_t2")
        t3 = st.number_input("3ª Titulação", key="ntk_t3")

        if t1 and t2 and t3:
            media = np.mean([t1, t2, t3])
            desvio = np.std([t1, t2, t3], ddof=1)

            st.write(f"Média: {media:.2f}")
            st.write(f"Desvio: {desvio:.2f}")

            if massa > 0 and volume > 0:
                ntk = (massa / 381.4) / volume * media
                st.success(f"NTK: {ntk:.4f} mg/L")

    # =========================================================
    # 🧪 DQO
    # =========================================================
    with aba3:

        st.subheader("DEMANDA QUÍMICA DE OXIGÊNIO (DQO)")

        responsavel3 = st.text_input("Responsável", key="dqo_resp")
        projeto3 = st.text_input("Projeto", key="dqo_proj")

        massa = st.number_input("Massa padrão (mg)", key="dqo_massa", min_value=0.0)
        volume = st.number_input("Volume (mL)", key="dqo_vol", min_value=0.0)

        t1 = st.number_input("1ª Titulação", key="dqo_t1")
        t2 = st.number_input("2ª Titulação", key="dqo_t2")
        t3 = st.number_input("3ª Titulação", key="dqo_t3")

        if t1 and t2 and t3:
            media = np.mean([t1, t2, t3])
            desvio = np.std([t1, t2, t3], ddof=1)

            st.write(f"Média: {media:.2f}")
            st.write(f"Desvio: {desvio:.2f}")

            if media > 0:
                dqo = (massa * 0.25) / media
                st.success(f"DQO: {dqo:.4f} mg/L")

    st.markdown("══════════════════════════════════════")
    st.success("✔ Todas as planilhas estão funcionando em abas!")
