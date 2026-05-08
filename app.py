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
    ["Início", "Laboratório", "Laudo Final"]
)

# ================= INÍCIO =================
if menu == "Início":

    st.markdown("## 👩‍🔬 Bem-vinda ao Laboratório Virtual CMMA")

    st.info(
        "Sistema desenvolvido para cálculos laboratoriais "
        "de Sólidos Totais e suas frações."
    )

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

    # ===== Réplica 1 =====
    st.markdown("## 🔹 Réplica 1")

    m1 = st.number_input(
        "m1 = massa da caçarola (g)",
        value=0.0000,
        format="%.4f",
        key="m1"
    )

    m2 = st.number_input(
        "m2 = massa da caçarola + ST (g)",
        value=0.0000,
        format="%.4f",
        key="m2"
    )

    m3 = st.number_input(
        "m3 = massa da caçarola + STF (g)",
        value=0.0000,
        format="%.4f",
        key="m3"
    )

    # ===== Réplica 2 =====
    st.markdown("## 🔹 Réplica 2")

    m1_2 = st.number_input(
        "m1' = massa da caçarola (g)",
        value=0.0000,
        format="%.4f",
        key="m1_2"
    )

    m2_2 = st.number_input(
        "m2' = massa da caçarola + ST (g)",
        value=0.0000,
        format="%.4f",
        key="m2_2"
    )

    m3_2 = st.number_input(
        "m3' = massa da caçarola + STF (g)",
        value=0.0000,
        format="%.4f",
        key="m3_2"
    )

    if st.button("🧪 GERAR RESULTADOS"):

        if volume == 0:
            st.error("Digite a Alíquota (mL).")
        else:
            # ===== CÁLCULOS =====
            ST1 = ((m2 - m1) * 1000000) / volume
            ST2 = ((m2_2 - m1_2) * 1000000) / volume

            STF1 = ((m3 - m1) * 1000000) / volume
            STF2 = ((m3_2 - m1_2) * 1000000) / volume

            STV1 = ST1 - STF1
            STV2 = ST2 - STF2

            lista_ST = np.array([ST1, ST2])
            lista_STF = np.array([STF1, STF2])
            lista_STV = np.array([STV1, STV2])

            resultados = {
                "ST": (np.mean(lista_ST), np.std(lista_ST)),
                "STF": (np.mean(lista_STF), np.std(lista_STF)),
                "STV": (np.mean(lista_STV), np.std(lista_STV)),
            }

            st.session_state["resultado_cmma"] = resultados

            st.success("✔ Cálculos concluídos com sucesso!")

# ================= LAUDO FINAL =================
elif menu == "Laudo Final":

    st.header("📄 Laudo Técnico Final")

    if "resultado_cmma" in st.session_state:

        for nome, valores in st.session_state["resultado_cmma"].items():

            media = valores[0]
            dp = valores[1]

            st.write(
                f"**{nome} = {media:.4f} ± {dp:.4f} mg/L**"
            )

    else:
        st.warning("⚠ Gere os resultados primeiro.")
