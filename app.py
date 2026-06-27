import streamlit as st
import numpy as np
import pandas as pd

# ================= CONFIG =================
st.set_page_config(page_title="LabResiduos - Laboratório Virtual", layout="wide")

# ================= CSS =================
st.markdown("""
<style>
.stApp { background-color: #e9f5e9; }

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
    st.title("🧪 IFRJ - LABORATÓRIO VIRTUAL")

st.markdown("---")

# ================= MENU =================
menu = st.sidebar.radio("📚 Sistema Laboratorial", [
    "🏠 Dashboard",
    "🧪 Sólidos Totais",
    "🧪 Sólidos Suspensos",
    "🧪 N-Amoniacal",
    "🧪 NTK",
    "🧪 NHX",
    "🧪 DQO",
    "📊 Planilhas Interativas"
])

# ================= HEADER =================
def header(titulo):
    st.title(f"DETERMINAÇÃO DE {titulo}")
    st.markdown("---")

# ================= DASHBOARD =================
if menu == "🏠 Dashboard":
    st.info("Selecione um módulo no menu.")

# ================= SÓLIDOS TOTAIS =================
elif menu == "🧪 Sólidos Totais":
    header("SÓLIDOS TOTAIS")

    v = st.number_input("Volume", value=50.0)
    m1 = st.number_input("m1")
    m2 = st.number_input("m2")
    m3 = st.number_input("m3")

    if st.button("Calcular"):
        fator = 1000 / (v / 1000)
        st.success("Cálculo realizado")

# ================= SÓLIDOS SUSPENSOS =================
elif menu == "🧪 Sólidos Suspensos":
    header("SÓLIDOS SUSPENSOS")

    v = st.number_input("Volume", value=50.0)
    m1 = st.number_input("m1")
    m2 = st.number_input("m2")
    m3 = st.number_input("m3")

    if st.button("Calcular"):
        st.success("OK")

# ================= N-AMONIACAL =================
elif menu == "🧪 N-Amoniacal":
    header("N-AMONIACAL")

    m = st.number_input("Massa")
    v = st.number_input("Volume")

    t1 = st.number_input("Titulação 1")
    t2 = st.number_input("Titulação 2")
    t3 = st.number_input("Titulação 3")

    if st.button("Calcular"):
        if v > 0:
            media = np.mean([t1, t2, t3])
            resultado = (m / 381.4) / (v / 1000) * media
            st.success(f"Resultado: {resultado:.4f}")

# ================= NTK =================
elif menu == "🧪 NTK":
    header("NTK")

    m = st.number_input("Massa")
    v = st.number_input("Volume")

    t1 = st.number_input("Titulação 1")
    t2 = st.number_input("Titulação 2")
    t3 = st.number_input("Titulação 3")

    if st.button("Calcular"):
        if v > 0:
            media = np.mean([t1, t2, t3])
            resultado = (m / 381.4) / (v / 1000) * media
            st.success(f"Resultado: {resultado:.4f}")

# ================= NHX =================
elif menu == "🧪 NHX":
    header("NHX")

    m = st.number_input("Massa")
    v = st.number_input("Volume")

    t1 = st.number_input("Titulação 1")
    t2 = st.number_input("Titulação 2")
    t3 = st.number_input("Titulação 3")

    if st.button("Calcular"):
        if v > 0:
            media = np.mean([t1, t2, t3])
            resultado = (m / 381.4) / (v / 1000) * media
            st.success(f"Resultado: {resultado:.4f}")

# ================= DQO =================
elif menu == "🧪 DQO":
    header("DQO")

    m = st.number_input("Massa padrão")
    v = st.number_input("Volume")

    t1 = st.number_input("Titulação 1")
    t2 = st.number_input("Titulação 2")
    t3 = st.number_input("Titulação 3")

    if st.button("Calcular"):
        if v > 0:
            media = np.mean([t1, t2, t3])
            resultado = (m * 0.25) / media
            st.success(f"Resultado: {resultado:.4f}")

# ================= PLANILHAS ESTÁVEIS =================
elif menu == "📊 Planilhas Interativas":

    st.title("📊 Planilhas (Upload seguro - sem erro Excel)")

    opcao = st.selectbox("Escolha a planilha", ["N-Amoniacal", "NTK", "DQO"])

    arquivo = st.file_uploader("📂 Envie o arquivo Excel (.xlsx)", type=["xlsx"])

    if arquivo:

        df = pd.read_excel(arquivo)

        st.subheader("📊 Visualização Editável")
        df_edit = st.data_editor(df, use_container_width=True)

        st.download_button(
            "⬇️ Baixar planilha editada",
            df_edit.to_csv(index=False).encode("utf-8"),
            file_name=f"{opcao}.csv",
            mime="text/csv"
        )

    else:
        st.info("Envie um arquivo Excel (.xlsx) para começar.")
