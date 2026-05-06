import streamlit as st
import numpy as np

st.set_page_config(page_title="LabResíduos IFRJ", layout="wide")

st.title("🧪 Laboratório Virtual de Resíduos – IFRJ")

menu = st.sidebar.selectbox(
    "📚 Menu",
    ["Início", "Laboratório"]
)

if menu == "Início":
    st.write("Sistema funcionando corretamente 🚀")

elif menu == "Laboratório":
    st.header("🧪 Cálculo Simplificado")

    volume = st.number_input("Volume (mL)", value=500.0)

    m1 = st.number_input("Massa 1", value=0.0)
    m2 = st.number_input("Massa 2", value=0.0)

    if st.button("Calcular"):
        resultado = (m1 + m2) * 1000 / volume
        st.success(f"Resultado: {resultado:.2f} mg/L")
