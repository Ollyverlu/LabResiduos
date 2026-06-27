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

    st.title("🧪 DETERMINAÇÃO DE NITROGÊNIO AMONIACAL")

    st.markdown("══════════════════════════════════════")

    # ================= IDENTIFICAÇÃO =================
    st.subheader("📄 IDENTIFICAÇÃO")

    responsavel = st.text_input("Responsável")
    projeto = st.text_input("Projeto")
    data = st.date_input("Data da Análise")
    hora = st.time_input("Hora da Análise")

    st.markdown("══════════════════════════════════════")

    # ================= PADRONIZAÇÃO =================
    st.subheader("⚗️ PADRONIZAÇÃO DO ÁCIDO SULFÚRICO (H₂SO₄)")

    massa_pesada = st.number_input("Massa pesada (g)", min_value=0.0, step=0.1)
    massa_molar = st.number_input("Massa molar (g/mol)", value=381.40)
    volume_balao = st.number_input("Volume do balão (mL)", min_value=0.0, step=1.0)

    if massa_pesada > 0 and volume_balao > 0:
        concentracao = (massa_pesada / massa_molar) / (volume_balao / 1000)
        st.success(f"Concentração: {concentracao:.6f} eqg/L")
    else:
        concentracao = None
        st.warning("Preencha os dados da padronização")

    st.markdown("══════════════════════════════════════")

    # ================= TITULAÇÕES =================
    st.subheader("🧪 TITULAÇÕES")

    vol_1 = st.number_input("1ª Titulação (mL)", min_value=0.0, step=0.1)
    vol_2 = st.number_input("2ª Titulação (mL)", min_value=0.0, step=0.1)
    vol_3 = st.number_input("3ª Titulação (mL)", min_value=0.0, step=0.1)

    st.markdown("══════════════════════════════════════")

    # ================= RESULTADOS =================
    st.subheader("📊 RESULTADOS")

    media = None
    desvio = None

    if vol_1 > 0 and vol_2 > 0 and vol_3 > 0:
        media = np.mean([vol_1, vol_2, vol_3])
        desvio = np.std([vol_1, vol_2, vol_3], ddof=1)

        st.write(f"Média das titulações: {media:.2f} mL")
        st.write(f"Desvio padrão: {desvio:.2f} mL")

    st.markdown("══════════════════════════════════════")

    # ================= REAGENTES =================
    st.subheader("🧫 REAGENTES UTILIZADOS")

    st.write("""
    - Ácido sulfúrico 0,1 eqg/L  
    - Ácido sulfúrico 0,02 eqg/L  
    - Tetraborato de sódio deca hidratado  
    - Alaranjado de metila  
    - Tampão fosfato 0,5 mol/L  
    - Solução de azul de metileno 0,2%  
    - Solução de vermelho de metila 0,2%  
    - Solução indicadora de ácido bórico  
    """)

    st.markdown("══════════════════════════════════════")

    # ================= FATOR DE CORREÇÃO =================
    st.subheader("📐 FATOR DE CORREÇÃO")

    if media and media > 0:
        fator_correcao = (concentracao * media) if concentracao else None

        if fator_correcao:
            st.success(f"Fator de correção: {fator_correcao:.6f}")
        else:
            st.warning("Complete a padronização para calcular o fator")

    st.markdown("══════════════════════════════════════")

    # ================= RESULTADO FINAL =================
    st.subheader("🏁 RESULTADO FINAL")

    massa = st.number_input("Massa da amostra (m)", min_value=0.0, step=0.1)
    volume = st.number_input("Volume da amostra (L)", min_value=0.0, step=0.1)

    if media and massa > 0 and volume > 0 and concentracao:

        resultado = (massa / 381.4) / volume * media

        st.success(f"Resultado de N-Amoniacal: {resultado:.4f} mg/L")

    else:
        st.info("Preencha todos os dados para obter o resultado final")

    st.markdown("══════════════════════════════════════")

    st.success("✔ N-Amoniacal concluída com sucesso!")
