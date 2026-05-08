import streamlit as st
import numpy as np

# ================= CONFIG =================
st.set_page_config(
    page_title="Laboratório Virtual CMMA – IFRJ",
    layout="wide"
)

# ================= ESTILO =================
st.markdown("""
<style>
.main{
    background-color:#f4f7ff;
}
h1,h2,h3{
    color:#1f4e79;
}
.block-container{
    padding-top:2rem;
}
.card {
    background-color: white;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# ================= CABEÇALHO =================
st.title("🧪 Laboratório Virtual CMMA – IFRJ")
st.subheader("Laudo Técnico de Ensaios Físico-Químicos")

st.markdown("""
### 👩‍🏫 Criador
Luciana Oliveira de Albuquerque

### 🎓 Administrador
Raphael Oliveira de Albuquerque
""")

st.success("Sistema ativo 🚀")

# ================= MENU =================
menu = st.sidebar.selectbox(
    "📚 Menu do Sistema",
    ["Início", "Aula Teórica", "Laboratório", "Laudo Final"]
)

# ================= INÍCIO =================
if menu == "Início":
    st.markdown("## 👩‍🔬 Bem-vinda ao Laboratório Virtual CMMA")

# ================= AULA TEÓRICA =================
elif menu == "Aula Teórica":

    st.header("📚 Aula Teórica – Sólidos Totais")

    st.markdown("### 📌 O que são Sólidos Totais (ST)?")
    st.markdown("""
<div class="card">
Sólidos Totais representam todo o material presente na amostra após evaporação da água.
Incluem matéria orgânica e inorgânica.
</div>
""", unsafe_allow_html=True)

    st.markdown("### 📌 Sólidos Totais Fixos (STF)")
    st.markdown("""
<div class="card">
Parte mineral dos sólidos que permanece após a queima na mufla (550°C).
</div>
""", unsafe_allow_html=True)

    st.markdown("### 📌 Sólidos Totais Voláteis (STV)")
    st.markdown("""
<div class="card">
Parte orgânica que é queimada na mufla.
</div>
""", unsafe_allow_html=True)

    st.markdown("### 🔬 Procedimento Experimental")
    st.markdown("""
<div class="card">
1. Pesar a caçarola → m1  
2. Secar em estufa (105°C) → m2  
3. Levar à mufla (550°C) → m3  
</div>
""", unsafe_allow_html=True)

    st.markdown("### 📊 Fórmulas")

    st.latex(r"ST = \frac{(m2 - m1)\times 10^6}{V}")
    st.latex(r"STF = \frac{(m3 - m1)\times 10^6}{V}")
    st.latex(r"STV = ST - STF")

    st.markdown("### 🧠 Exemplo")
    st.markdown("""
<div class="card">
m1 = 50 g  
m2 = 50.5 g  
m3 = 50.2 g  
V = 100 mL  

ST = 5000 mg/L  
STF = 2000 mg/L  
STV = 3000 mg/L  
</div>
""", unsafe_allow_html=True)

# ================= LABORATÓRIO =================
elif menu == "Laboratório":

    st.header("🧪 Dados Inseridos")

    volume = st.number_input(
        "Alíquota (mL)",
        min_value=0.0,
        value=0.0,
        step=10.0,
        format="%.2f"
    )

    st.markdown("### 📥 2 medições")
    st.write("**Caçarola**")

    st.subheader("Massas Experimentais")

    # Réplica 1
    st.markdown("## 🔹 Réplica 1")
    m1 = st.number_input("m1", value=0.0000, format="%.4f")
    m2 = st.number_input("m2", value=0.0000, format="%.4f")
    m3 = st.number_input("m3", value=0.0000, format="%.4f")

    # Réplica 2
    st.markdown("## 🔹 Réplica 2")
    m1_2 = st.number_input("m1'", value=0.0000, format="%.4f")
    m2_2 = st.number_input("m2'", value=0.0000, format="%.4f")
    m3_2 = st.number_input("m3'", value=0.0000, format="%.4f")

    if st.button("🧪 GERAR RESULTADOS"):

        if volume == 0:
            st.error("Digite a Alíquota.")
        else:
            ST1 = ((m2 - m1) * 1000000) / volume
            ST2 = ((m2_2 - m1_2) * 1000000) / volume

            STF1 = ((m3 - m1) * 1000000) / volume
            STF2 = ((m3_2 - m1_2) * 1000000) / volume

            STV1 = ST1 - STF1
            STV2 = ST2 - STF2

            resultados = {
                "ST": (np.mean([ST1, ST2]), np.std([ST1, ST2])),
                "STF": (np.mean([STF1, STF2]), np.std([STF1, STF2])),
                "STV": (np.mean([STV1, STV2]), np.std([STV1, STV2]))
            }

            st.session_state["resultado"] = resultados
            st.success("✔ Cálculos concluídos!")

# ================= LAUDO FINAL =================
elif menu == "Laudo Final":

    st.header("📄 Laudo Técnico Final")

    if "resultado" in st.session_state:

        for nome, valores in st.session_state["resultado"].items():
            media, dp = valores
            st.write(f"**{nome} = {media:.0f} ± {dp:.0f} mg/L**")

    else:
        st.warning("⚠ Gere os resultados primeiro.")
