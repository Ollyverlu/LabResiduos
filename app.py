elif menu == "Laboratório":

    st.header("🔬 Laboratório Virtual")

    opcao = st.radio(
        "📌 Escolha o parâmetro para análise:",
        [
            "Sólidos Totais",
            "Sólidos Suspensos",
            "N-Amoniacal",
            "NTK",
            "DQO"
        ]
    )

    # ================= SÓLIDOS TOTAIS =================
    if opcao == "Sólidos Totais":

        st.subheader("🧪 Sólidos Totais")

        volume = st.number_input("Alíquota (mL)", min_value=0.0, value=50.0)

        st.markdown("## 🔹 Réplica 1")
        m1 = st.number_input("m1", value=0.0, format="%.4f")
        m2 = st.number_input("m2", value=0.0, format="%.4f")
        m3 = st.number_input("m3", value=0.0, format="%.4f")

        st.markdown("## 🔹 Réplica 2")
        m1_2 = st.number_input("m1'", value=0.0, format="%.4f")
        m2_2 = st.number_input("m2'", value=0.0, format="%.4f")
        m3_2 = st.number_input("m3'", value=0.0, format="%.4f")

        if st.button("🧪 GERAR RESULTADO ST"):

            fator = 1000 / (volume / 1000)

            ST1 = (m2 - m1) * fator
            ST2 = (m2_2 - m1_2) * fator

            STF1 = (m3 - m1) * fator
            STF2 = (m3_2 - m1_2) * fator

            STV1 = ST1 - STF1
            STV2 = ST2 - STF2

            st.session_state["ST"] = (ST1, ST2, STF1, STF2, STV1, STV2)
            st.success("✔ Sólidos Totais calculado!")

    # ================= SÓLIDOS SUSPENSOS =================
    elif opcao == "Sólidos Suspensos":
        st.subheader("🧪 Sólidos Suspensos")
        ss = st.number_input("Sólidos Suspensos (mg/L)", value=0.0)
        st.session_state["SS"] = ss
        st.success("✔ SS registrado!")

    # ================= N-AMONIACAL =================
    elif opcao == "N-Amoniacal":
        st.subheader("🧪 N-Amoniacal")
        na = st.number_input("N-Amoniacal (mg/L)", value=0.0)
        st.session_state["NA"] = na
        st.success("✔ N-Amoniacal registrado!")

    # ================= NTK =================
    elif opcao == "NTK":
        st.subheader("🧪 NTK")
        ntk = st.number_input("NTK (mg/L)", value=0.0)
        st.session_state["NTK"] = ntk
        st.success("✔ NTK registrado!")

    # ================= DQO =================
    elif opcao == "DQO":
        st.subheader("🧪 DQO")
        dqo = st.number_input("DQO (mg/L)", value=0.0)
        st.session_state["DQO"] = dqo
        st.success("✔ DQO registrado!")
