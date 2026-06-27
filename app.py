# ================= PLANILHAS INTERATIVAS =================
elif menu == "📊 Planilhas Interativas (Excel)":

    import pandas as pd
    import streamlit as st
    from io import BytesIO

    st.title("📊 Planilhas Interativas - Excel com Abas")

    arquivos = {
        "N-Amoniacal": "N-AMONIACAL.xlsx",
        "NTK": "NTK.xlsx",
        "DQO": "DQO.xlsx"
    }

    # 🔥 TEMPLATE BASE (SEU MODELO COMPLETO)
    def criar_template():
        return pd.DataFrame({
            "CAMPO": [
                "TÍTULO: DETERMINAÇÃO DE NITROGÊNIO AMONIACAL",
                "RESPONSÁVEL",
                "PROJETO",
                "DATA DA ANÁLISE",
                "HORA DA ANÁLISE",
                "",
                "PADRONIZAÇÃO DO ÁCIDO SULFÚRICO (H2SO4) 0,02 N",
                "",
                "MASSA PESADA (g)",
                "MASSA MOLAR (g/mol)",
                "VOLUME DO BALÃO (mL)",
                "CONCENTRAÇÃO (eqg/L)",
                "",
                "1ª TITULAÇÃO",
                "VOLUME DE H2SO4 (mL)",
                "CONCENTRAÇÃO REAL",
                "",
                "2ª TITULAÇÃO",
                "VOLUME DE H2SO4 (mL)",
                "CONCENTRAÇÃO REAL",
                "",
                "3ª TITULAÇÃO",
                "VOLUME DE H2SO4 (mL)",
                "CONCENTRAÇÃO REAL",
                "",
                "RESULTADOS FINAIS",
                "CONCENTRAÇÃO REAL",
                "DESVIO PADRÃO",
                "FATOR DE CORREÇÃO"
            ],
            "VALOR": [""] * 29,
            "UNIDADE": [""] * 29
        })

    tabs = st.tabs(list(arquivos.keys()))

    for i, nome in enumerate(arquivos.keys()):

        with tabs[i]:

            st.subheader(f"📄 {nome}")

            df = criar_template()

            df_edit = st.data_editor(
                df,
                use_container_width=True,
                num_rows="fixed",
                key=f"edit_{nome}"
            )

            # 🔥 FUNÇÃO PARA GERAR EXCEL COMPLETO
            def to_excel(dataframe):
                output = BytesIO()
                with pd.ExcelWriter(output, engine="openpyxl") as writer:
                    dataframe.to_excel(writer, index=False, sheet_name=nome)
                return output.getvalue()

            st.download_button(
                f"⬇️ Baixar {nome} COMPLETO",
                data=to_excel(df_edit),
                file_name=f"{nome}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                key=f"download_{nome}"
            )
