import streamlit as st
import numpy as np
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
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

    # ================= ETAPA 1 =================
    with st.expander("📌 1. Identificação da Amostra"):
        responsavel = st.text_input("Responsável")
        projeto = st.text_input("Projeto")
        data = st.date_input("Data da análise")
        hora = st.time_input("Hora da análise")

    responsavel = st.text_input("Responsável")
    projeto = st.text_input("Projeto")
    data = st.date_input("Data da análise")
    hora = st.time_input("Hora da análise")
    
    st.markdown("══════════════════════════════════════")

    # ================= ETAPA 2 =================
    with st.expander("🧪 2. Cálculo N-Amoniacal"):
        m = st.number_input("Massa")
        v = st.number_input("Volume")

        t1 = st.number_input("Titulação 1")
        t2 = st.number_input("Titulação 2")
        t3 = st.number_input("Titulação 3")

        if st.button("Calcular N-Amoniacal", key="btn_na_calc"):
            media = np.mean([t1, t2, t3])
            if media != 0 and v > 0:
                resultado = (m / 381.4) / (v / 1000) * media
                st.success(f"Resultado: {resultado:.4f} mg/L")

    st.markdown("══════════════════════════════════════")

    # ================= ETAPA 3 =================
    with st.expander("📌 3. Padronização do H₂SO₄ (0,02 N)"):
        massa_pesada = st.number_input("Massa pesada (g)")
        massa_molar = st.number_input("Massa molar (g/mol)", value=381.40)
        volume_balao = st.number_input("Volume do balão (mL)")

        t1_pad = st.number_input("Titulação 1 (padronização)")
        t2_pad = st.number_input("Titulação 2 (padronização)")
        t3_pad = st.number_input("Titulação 3 (padronização)")

        if st.button("Calcular Padronização H₂SO₄", key="btn_pad_na"):
            media_pad = np.mean([t1_pad, t2_pad, t3_pad])
            st.info(f"Média da padronização: {media_pad:.4f}")


# ================= NTK =================
elif menu == "🧪 NTK":
    header("NITROGÊNIO TOTAL KJELDAHL")

    m = st.number_input("Massa")
    v = st.number_input("Volume")

    t1 = st.number_input("Titulação 1")
    t2 = st.number_input("Titulação 2")
    t3 = st.number_input("Titulação 3")

    if st.button("Calcular NTK", key="btn_ntk"):
        media = np.mean([t1, t2, t3])
        if media != 0 and v > 0:
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

    if st.button("Calcular NHX", key="btn_nhx"):
        media = np.mean([t1, t2, t3])
        if media != 0 and v > 0:
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

    if st.button("Calcular DQO", key="btn_dqo"):
        media = np.mean([t1, t2, t3])
        if media != 0:
            resultado = (m * 0.25) / media
            st.success(f"Resultado: {resultado:.4f}")


# ================= PLANILHAS INTERATIVAS (SEM EXCEL) =================
elif menu == "📊 Planilhas Interativas (Excel)":

    import pandas as pd

    st.title("🧪 LABORATÓRIO VIRTUAL - PLANILHAS INTERATIVAS")
    st.markdown("══════════════════════════════════════")

    # 🔥 dados em memória (não precisa arquivo)
    if "na_data" not in st.session_state:
        st.session_state.na_data = pd.DataFrame()

    if "ntk_data" not in st.session_state:
        st.session_state.ntk_data = pd.DataFrame()

    if "dqo_data" not in st.session_state:
        st.session_state.dqo_data = pd.DataFrame()

    aba1, aba2, aba3 = st.tabs(["N-Amoniacal", "NTK", "DQO"])

    # ================= ABA 1 =================
    with aba1:
        st.subheader("N-Amoniacal")

        df1 = st.data_editor(st.session_state.na_data, use_container_width=True, key="na")

        if st.button("💾 Salvar N-Amoniacal", key="btn_na"):
            st.session_state.na_data = df1
            st.success("Salvo na memória!")

        st.download_button(
            "⬇️ Baixar CSV",
            data=df1.to_csv(index=False).encode("utf-8"),
            file_name="N-Amoniacal.csv",
            mime="text/csv"
        )

    # ================= ABA 2 =================
    with aba2:
        st.subheader("NTK")

        df2 = st.data_editor(st.session_state.ntk_data, use_container_width=True, key="ntk")

        if st.button("💾 Salvar NTK", key="btn_ntk"):
            st.session_state.ntk_data = df2
            st.success("Salvo na memória!")

        st.download_button(
            "⬇️ Baixar CSV",
            data=df2.to_csv(index=False).encode("utf-8"),
            file_name="NTK.csv",
            mime="text/csv"
        )

    # ================= ABA 3 =================
    with aba3:
        st.subheader("DQO")

        df3 = st.data_editor(st.session_state.dqo_data, use_container_width=True, key="dqo")

        if st.button("💾 Salvar DQO", key="btn_dqo"):
            st.session_state.dqo_data = df3
            st.success("Salvo na memória!")

        st.download_button(
            "⬇️ Baixar CSV",
            data=df3.to_csv(index=False).encode("utf-8"),
            file_name="DQO.csv",
            mime="text/csv"
        )
