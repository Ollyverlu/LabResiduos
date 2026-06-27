import streamlit as st
import numpy as np

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
    "🧪 DQO"
])

# ================= HEADER CORRIGIDO (ANTI ERRO STREAMLIT) =================
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

    import pandas as pd

    st.title("📊 Planilhas Interativas - Estilo Excel")

    st.info("Módulo independente. Não altera nenhum cálculo do sistema principal.")

    opcao = st.selectbox("Escolha a planilha:", [
        "🧪 Sólidos Totais (ST)",
        "🔥 Sólidos Fixos (STF)",
        "💨 Sólidos Voláteis (STV)"
    ])

    if opcao == "🧪 Sólidos Totais (ST)":

        df = pd.DataFrame({
            "Amostra": ["A1", "A2", "A3"],
            "Massa (m2-m1)": [0, 0, 0],
            "Volume (mL)": [50, 50, 50]
        })

        df_edit = st.data_editor(df, num_rows="dynamic", use_container_width=True)

        if st.button("📌 Calcular ST"):
            df_edit["ST (mg/L)"] = df_edit["Massa (m2-m1)"] / (df_edit["Volume (mL)"] / 1000)

            st.success("ST calculado com sucesso!")
            st.dataframe(df_edit, use_container_width=True)

    elif opcao == "🔥 Sólidos Fixos (STF)":

        df = pd.DataFrame({
            "Amostra": ["A1", "A2", "A3"],
            "Massa Cinzas": [0, 0, 0],
            "Volume (mL)": [50, 50, 50]
        })

        df_edit = st.data_editor(df, num_rows="dynamic", use_container_width=True)

        if st.button("📌 Calcular STF"):
            df_edit["STF (mg/L)"] = df_edit["Massa Cinzas"] / (df_edit["Volume (mL)"] / 1000)

            st.success("STF calculado com sucesso!")
            st.dataframe(df_edit, use_container_width=True)

    elif opcao == "💨 Sólidos Voláteis (STV)":

        df = pd.DataFrame({
            "Amostra": ["A1", "A2", "A3"],
            "ST": [0, 0, 0],
            "STF": [0, 0, 0]
        })

        df_edit = st.data_editor(df, num_rows="dynamic", use_container_width=True)

        if st.button("📌 Calcular STV"):
            df_edit["STV"] = df_edit["ST"] - df_edit["STF"]

            st.success("STV calculado com sucesso!")
            st.dataframe(df_edit, use_container_width=True)  
     
