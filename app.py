
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
st.title("🧪 Laboratório Virtual CEMMA – IFRJ  - Com Professor Renato Ribeiro")
st.subheader("Laudo Técnico de Ensaios Físico-Químicos")

st.markdown("""
### 👩‍🏫 Criado por  
Luciana Oliveira de Albuquerque  

### 🎓 Administrador  
Raphael Oliveira de Albuquerque
""")

st.success("Sistema ativo 🚀")

# ================= MENU =================
menu = st.sidebar.selectbox(
    "📚 Menu do Sistema",
    [
        "🏠 Início",

        "📚 Aula Teórica - Sólidos Totais",
        "📚 Aula Teórica - Sólidos Suspensos",
        "📚 Aula Teórica - N-Amoniacal",
        "📚 Aula Teórica - NTK",
        "📚 Aula Teórica - DQO",

        "🔬 Laboratório",

        "📊 Resultados"
    ]
)

# ================= INÍCIO =================
if menu == "🏠 Início":

    st.markdown(
        "<h2 style='text-align:center;'>👩‍🔬 Bem-vindo ao Laboratório Virtual CEMMA</h2>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 4, 1])

    with col2:
        st.image("logo.png", use_container_width=True)


# ================= AULAS TEÓRICAS =================
elif menu == "📚 Aula Teórica - Sólidos Totais":
    st.header("📘 Sólidos Totais (ST)")
    st.markdown("""
    Representa toda matéria sólida presente na água.
    
    📌 Fórmula:
    ST = massa total × fator
    
    📍 Importância:
    - Controle de poluição
    - Monitoramento ambiental
    """)

elif menu == "📚 Aula Teórica - Sólidos Suspensos":
    st.header("📘 Sólidos Suspensos (SS)")
    st.markdown("""
    Partículas que ficam suspensas na água.

    📍 Importância:
    - Turbidez
    - Impacto em ecossistemas aquáticos
    """)

elif menu == "📚 Aula Teórica - N-Amoniacal":
    st.header("📘 Nitrogênio Amoniacal")
    st.markdown("""
    Forma de nitrogênio presente na água como amônia/amônio.

    📍 Importância:
    - Toxicidade
    - Indicador de poluição recente
    """)

elif menu == "📚 Aula Teórica - NTK":
    st.header("📘 NTK (Nitrogênio Total Kjeldahl)")
    st.markdown("""
    Soma do nitrogênio orgânico + amoniacal.

    📍 Importância:
    - Avaliação de carga orgânica
    """)

elif menu == "📚 Aula Teórica - DQO":
    st.header("📘 DQO - Demanda Química de Oxigênio")
    st.markdown("""
    Mede o oxigênio necessário para oxidar matéria orgânica e inorgânica.

    📍 Importância:
    - Indicador de poluição industrial
    - Tratamento de efluentes
    """)


# ================= LABORATÓRIO =================
elif menu == "🔬 Laboratório":

    st.header("🧪 Inserção de Dados")

    volume = st.number_input("Alíquota (mL)", min_value=0.0, value=50.0)

    st.markdown("### 📌 Sólidos Totais")

    m1 = st.number_input("m1", value=0.0, format="%.4f")
    m2 = st.number_input("m2", value=0.0, format="%.4f")
    m3 = st.number_input("m3", value=0.0, format="%.4f")

    st.markdown("### 📌 Sólidos Suspensos")
    ss = st.number_input("Sólidos Suspensos (mg/L)", value=0.0)

    st.markdown("### 📌 Nitrogênio Amoniacal")
    na = st.number_input("N-Amoniacal (mg/L)", value=0.0)

    st.markdown("### 📌 NTK")
    ntk = st.number_input("NTK (mg/L)", value=0.0)

    st.markdown("### 📌 DQO")
    dqo = st.number_input("DQO (mg/L)", value=0.0)

    if st.button("🧪 GERAR RESULTADOS"):

        fator = 1000 / (volume / 1000)

        ST = (m2 - m1) * fator
        STF = (m3 - m1) * fator
        STV = ST - STF

        resultados = {
            "ST": ST,
            "STF": STF,
            "STV": STV,
            "SS": ss,
            "N-Amoniacal": na,
            "NTK": ntk,
            "DQO": dqo
        }

        st.session_state["resultado"] = resultados
        st.success("✔ Resultados gerados com sucesso!")


# ================= RESULTADOS =================
elif menu == "📊 Resultados":

    st.header("📊 Laudo Final")

    if "resultado" in st.session_state:

        nomes = {
            "ST": "Sólidos Totais",
            "STF": "Sólidos Fixos",
            "STV": "Sólidos Voláteis",
            "SS": "Sólidos Suspensos",
            "N-Amoniacal": "Nitrogênio Amoniacal",
            "NTK": "Nitrogênio Total Kjeldahl",
            "DQO": "Demanda Química de Oxigênio"
        }

        for k, v in st.session_state["resultado"].items():

            st.markdown(f"""
            <div class="card">
                <b>{nomes[k]}</b><br>
                {v:.2f} mg/L
            </div>
            """, unsafe_allow_html=True)

    else:
        st.warning("⚠ Nenhum resultado gerado ainda.")
