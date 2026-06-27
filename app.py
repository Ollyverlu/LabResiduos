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

    st.markdown("═══════════════════════════════════════")

    # ================= ETAPA 2 - PADRONIZAÇÃO =================
    with st.expander("📌 Padronização do H₂SO₄ (0,02 N)"):

        massa_pesada = st.number_input("Massa pesada (g)")
        massa_molar = st.number_input("Massa molar (g/mol)", value=381.40)
        volume_balao = st.number_input("Volume do balão (mL)")

        t1_pad = st.number_input("Volume de H₂SO₄ gasto 1")
        t2_pad = st.number_input("Volume de H₂SO₄ gasto 2")
        t3_pad = st.number_input("Volume de H₂SO₄ gasto 3")

        if st.button("Calcular Padronização H₂SO₄", key="btn_padronizacao"):
            media_pad = np.mean([t1_pad, t2_pad, t3_pad])
            desvio_pad = np.std([t1_pad, t2_pad, t3_pad], ddof=1)

            st.success(f"Média: {media_pad:.4f}")
            st.info(f"Desvio padrão: {desvio_pad:.4f}")

    st.markdown("═══════════════════════════════════════")

    # ================= ETAPA 3 - CÁLCULO =================
    with st.expander("🧪 Cálculo do N-Amoniacal"):

        m = st.number_input("Massa (g)", key="nh3_m")
        v = st.number_input("Volume (mL)", key="nh3_v")

        t1 = st.number_input("Titulação 1", key="nh3_t1")
        t2 = st.number_input("Titulação 2", key="nh3_t2")
        t3 = st.number_input("Titulação 3", key="nh3_t3")

        if st.button("Calcular N-Amoniacal", key="btn_nh3"):

            if v > 0:
                media = np.mean([t1, t2, t3])
                desvio = np.std([t1, t2, t3], ddof=1)

                resultado = (m / 381.4) / (v / 1000) * media

                st.success(f"Resultado: {resultado:.4f} mg/L")
                st.info(f"Média: {media:.4f}")
                st.info(f"Desvio padrão: {desvio:.4f}")
        
# ================= ETAPA 4 - RELATÓRIO FINAL =================
st.markdown("═══════════════════════════════════════")
st.subheader("📌 Relatório Final da Análise")

if st.button("📄 Gerar Relatório Final", key="btn_relatorio"):

    if v > 0:

        media = np.mean([t1, t2, t3])
        desvio = np.std([t1, t2, t3], ddof=1)
        resultado = (m / 381.4) / (v / 1000) * media

        st.markdown(f"""
        <div class="card">

        <b>🧪 NITROGÊNIO AMONIACAL - RELATÓRIO FINAL</b><br><br>

        📌 Responsável: {responsavel}<br>
        📌 Projeto: {projeto}<br>
        📌 Data: {data}<br>
        📌 Hora: {hora}<br><br>

        ⚗ Massa: {m} g<br>
        ⚗ Volume: {v} mL<br><br>

        📊 Média das titulações: {media:.4f}<br>
        📉 Desvio padrão: {desvio:.4f}<br>
        🧪 Resultado final: {resultado:.4f} mg/L<br><br>

        ✔ Análise concluída com sucesso
        </div>
        """, unsafe_allow_html=True)
        
# ================= NTK =================
elif menu == "🧪 NTK":
    header("NITROGÊNIO TOTAL KJELDAHL")

    # ================= ETAPA 1 =================
    with st.expander("📌 1. Identificação da Amostra"):
        responsavel = st.text_input("Responsável", key="ntk_resp")
        projeto = st.text_input("Projeto", key="ntk_proj")
        data = st.date_input("Data da análise", key="ntk_data")
        hora = st.time_input("Hora da análise", key="ntk_hora")

    st.markdown("═══════════════════════════════════════")

    # ================= ETAPA 2 =================
    st.subheader("🧪 Cálculo do NTK")

    m = st.number_input("Massa (g)", key="ntk_m")
    v = st.number_input("Volume (mL)", key="ntk_v")

    t1 = st.number_input("Titulação 1", key="ntk_t1")
    t2 = st.number_input("Titulação 2", key="ntk_t2")
    t3 = st.number_input("Titulação 3", key="ntk_t3")

    if st.button("Calcular NTK", key="btn_ntk_calc"):

        if v > 0:

            media = np.mean([t1, t2, t3])
            desvio = np.std([t1, t2, t3], ddof=1)

            resultado = (m / 381.4) / (v / 1000) * media

            st.success(f"NTK: {resultado:.4f} mg/L")
            st.info(f"Média: {media:.4f}")
            st.info(f"Desvio padrão: {desvio:.4f}")

    st.markdown("═══════════════════════════════════════")

    # ================= ETAPA 3 =================
    st.subheader("📌 Relatório Final")

    if st.button("📄 Gerar Relatório NTK", key="btn_ntk_rel"):

        if v > 0:

            media = np.mean([t1, t2, t3])
            desvio = np.std([t1, t2, t3], ddof=1)
            resultado = (m / 381.4) / (v / 1000) * media

            st.markdown(f"""
            <div class="card">

            <b>🧪 RELATÓRIO NTK</b><br><br>

            Responsável: {responsavel}<br>
            Projeto: {projeto}<br>
            Data: {data}<br>
            Hora: {hora}<br><br>

            Massa: {m} g<br>
            Volume: {v} mL<br><br>

            Média: {media:.4f}<br>
            Desvio padrão: {desvio:.4f}<br>
            Resultado: {resultado:.4f} mg/L
            </div>
            """, unsafe_allow_html=True)

# ================= DQO =================
elif menu == "🧪 DQO":
    header("DEMANDA QUÍMICA DE OXIGÊNIO")

    # ================= ETAPA 1 =================
    with st.expander("📌 1. Identificação da Amostra"):
        responsavel = st.text_input("Responsável", key="dqo_resp")
        projeto = st.text_input("Projeto", key="dqo_proj")
        data = st.date_input("Data da análise", key="dqo_data")
        hora = st.time_input("Hora da análise", key="dqo_hora")

    st.markdown("═══════════════════════════════════════")

    # ================= ETAPA 2 =================
    st.subheader("🧪 Cálculo da DQO")

    m = st.number_input("Massa padrão", key="dqo_m")
    v = st.number_input("Volume da amostra", key="dqo_v")

    t1 = st.number_input("Titulação 1", key="dqo_t1")
    t2 = st.number_input("Titulação 2", key="dqo_t2")
    t3 = st.number_input("Titulação 3", key="dqo_t3")

    if st.button("Calcular DQO", key="btn_dqo_calc"):

        if v > 0:

            media = np.mean([t1, t2, t3])
            desvio = np.std([t1, t2, t3], ddof=1)

            resultado = (m * 0.25) / media

            st.success(f"DQO: {resultado:.4f} mg/L")
            st.info(f"Média: {media:.4f}")
            st.info(f"Desvio padrão: {desvio:.4f}")

    st.markdown("═══════════════════════════════════════")

    # ================= ETAPA 3 =================
    st.subheader("📌 Relatório Final")

    if st.button("📄 Gerar Relatório DQO", key="btn_dqo_rel"):

        if media > 0:

            st.markdown(f"""
            <div class="card">

            <b>🧪 RELATÓRIO DQO</b><br><br>

            Responsável: {responsavel}<br>
            Projeto: {projeto}<br>
            Data: {data}<br>
            Hora: {hora}<br><br>

            Massa: {m}<br>
            Volume: {v}<br><br>

            Média: {media:.4f}<br>
            Desvio padrão: {desvio:.4f}<br>
            Resultado: {resultado:.4f} mg/L
            </div>
            """, unsafe_allow_html=True)
   # ================= PLANILHAS INTERATIVAS (SEM EXCEL - ESTÁVEL) =================
elif menu == "📊 Planilhas Interativas (Excel)":

    import pandas as pd

    st.title("🧪 LABORATÓRIO VIRTUAL - REGISTRO DE DADOS")
    st.markdown("══════════════════════════════════════")

    # ================= MEMÓRIA =================
    if "na_data" not in st.session_state:
        st.session_state.na_data = []

    if "ntk_data" not in st.session_state:
        st.session_state.ntk_data = []

    if "dqo_data" not in st.session_state:
        st.session_state.dqo_data = []

    aba1, aba2, aba3 = st.tabs(["N-Amoniacal", "NTK", "DQO"])

    # ================= ABA 1 =================
    with aba1:
        st.subheader("N-Amoniacal")

        responsavel = st.text_input("Responsável", key="na_resp")
        projeto = st.text_input("Projeto", key="na_proj")
        resultado = st.number_input("Resultado (mg/L)", key="na_resultado")

        if st.button("➕ Adicionar N-Amoniacal"):
            st.session_state.na_data.append({
                "Responsável": responsavel,
                "Projeto": projeto,
                "Resultado": resultado
            })

        st.dataframe(pd.DataFrame(st.session_state.na_data))

    # ================= ABA 2 =================
    with aba2:
        st.subheader("NTK")

        responsavel_ntk = st.text_input("Responsável", key="ntk_resp")
        projeto_ntk = st.text_input("Projeto", key="ntk_proj")
        resultado_ntk = st.number_input("Resultado (mg/L)", key="ntk_res")

        if st.button("➕ Adicionar NTK"):
            st.session_state.ntk_data.append({
                "Responsável": responsavel_ntk,
                "Projeto": projeto_ntk,
                "Resultado": resultado_ntk
            })

        st.dataframe(pd.DataFrame(st.session_state.ntk_data))

    # ================= ABA 3 =================
    with aba3:
        st.subheader("DQO")

        responsavel_dqo = st.text_input("Responsável", key="dqo_resp2")
        projeto_dqo = st.text_input("Projeto", key="dqo_proj2")
        resultado_dqo = st.number_input("Resultado (mg/L)", key="dqo_res")

        if st.button("➕ Adicionar DQO"):
            st.session_state.dqo_data.append({
                "Responsável": responsavel_dqo,
                "Projeto": projeto_dqo,
                "Resultado": resultado_dqo
            })

        st.dataframe(pd.DataFrame(st.session_state.dqo_data))
