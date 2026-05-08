import streamlit as st
import numpy as np

# ================= CONFIG =================
st.set_page_config(
    page_title="Laboratório Virtual CEMMA – IFRJ",
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
st.title("🧪 Laboratório Virtual CEMMA – IFRJ")
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
    st.markdown("## 👩‍🔬 Bem-vindo (a) ao Laboratório Virtual CEMMA")

# ================= AULA TEÓRICA =================
elif menu == "Aula Teórica":

    st.header("📚 Equipamentos Utilizados")

    st.markdown("""
<div class="card">
Sólidos Totais representam todo material após evaporação da água.
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="card">
Sólidos Fixos = parte mineral (não volatiliza na mufla)
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="card">
Sólidos Voláteis = parte orgânica (queima na mufla)
</div>
""", unsafe_allow_html=True)

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
</div>
""", unsafe_allow_html=True)

    # ================= EQUIPAMENTOS =================
    st.markdown("## 🔬 Equipamentos de Laboratório")

    st.markdown("### 🔥 Forno Mufla")
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3f/Muffle_furnace.jpg", use_container_width=True)

    st.markdown("### 🌡️ Estufa Laboratorial")
    st.image("https://upload.wikimedia.org/wikipedia/commons/5/5f/Drying_oven_lab.jpg", use_container_width=True)

    st.markdown("### ⚖️ Balança de Precisão")
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/2b/Analytical_balance.jpg", use_container_width=True)

    st.markdown("### 💧 Dessecador")
    st.image("https://upload.wikimedia.org/wikipedia/commons/1/1e/Desiccator_laboratory.jpg", use_container_width=True)

    st.markdown("### 🧪 Cadinho de Porcelana")
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6b/Crucible_porcelain.jpg", use_container_width=True)

    st.markdown("### 🥣 Caçarola")
    st.image("https://upload.wikimedia.org/wikipedia/commons/9/9d/Weighing_dish_lab.jpg", use_container_width=True)

# ================= LABORATÓRIO =================
elif menu == "Laboratório":

    st.header("🧪 Inserção de Dados")

    volume = st.number_input("Alíquota (mL)", min_value=0.0, value=50.0)

    st.markdown("## 🔹 Réplica 1")
    m1 = st.number_input("m1", value=0.0, format="%.4f")
    m2 = st.number_input("m2", value=0.0, format="%.4f")
    m3 = st.number_input("m3", value=0.0, format="%.4f")

    st.markdown("## 🔹 Réplica 2")
    m1_2 = st.number_input("m1'", value=0.0, format="%.4f")
    m2_2 = st.number_input("m2'", value=0.0, format="%.4f")
    m3_2 = st.number_input("m3'", value=0.0, format="%.4f")

    if st.button("🧪 GERAR RESULTADOS"):

        if volume <= 0:
            st.error("Volume inválido.")
        else:
            fator = 1000 / (volume / 1000)

            ST1 = (m2 - m1) * fator
            ST2 = (m2_2 - m1_2) * fator

            STF1 = (m3 - m1) * fator
            STF2 = (m3_2 - m1_2) * fator

            STV1 = ST1 - STF1
            STV2 = ST2 - STF2

            if STF1 > ST1 or STF2 > ST2:
                st.warning("⚠ Atenção: STF maior que ST. Verifique os dados!")

            resultados = {
                "ST": (np.mean([ST1, ST2]), np.std([ST1, ST2], ddof=1)),
                "STF": (np.mean([STF1, STF2]), np.std([STF1, STF2], ddof=1)),
                "STV": (np.mean([STV1, STV2]), np.std([STV1, STV2], ddof=1))
            }

            st.session_state["resultado"] = resultados
            st.success("✔ Cálculos concluídos!")

# ================= LAUDO FINAL =================
elif menu == "Laudo Final":

    st.header("📄 Laudo Técnico Final")

    if "resultado" in st.session_state:

        nomes = {
            "ST": "Sólidos Totais (ST)",
            "STF": "Sólidos Fixos (STF)",
            "STV": "Sólidos Voláteis (STV)"
        }

        for chave, (media, dp) in st.session_state["resultado"].items():

            st.markdown(f"""
            <div class="card">
            <b>{nomes[chave]}</b><br>
            {media:.2f} ± {dp:.2f} mg/L
            </div>
            """, unsafe_allow_html=True)

    else:
        st.warning("⚠ Gere os resultados primeiro no laboratório.")
