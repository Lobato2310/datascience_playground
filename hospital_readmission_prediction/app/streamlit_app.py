import streamlit as st

st.title("Previsão de Readmissão Hospitalar")

st.write(
    """
    Aplicação desenvolvida para prever a probabilidade de readmissão hospitalar utilizando Machine Learning.

    Este modelo foi treinado com 16 variáveis. Para simplificar a demonstração,
    a aplicação solicita apenas as 5 variáveis mais relevantes identificadas
    durante a análise de importância das features.
    """
)

idade = st.selectbox(
    "Faixa etária",
    ['[40-50)', '[50-60)', '[60-70)', '[70-80)', '[80-90)', '[90-100)']
)

tempo_hospitalizacao = st.number_input(
    "Tempo de internação (dias)",
    min_value=0
)

n_lab_procedures = st.number_input(
    "Quantidade de exames laboratoriais",
    min_value=0
)

n_procedures = st.number_input(
    "Quantidade de procedimentos",
    min_value=0
)

n_medications = st.number_input(
    "Quantidade de medicamentos",
    min_value=0
)

previsao = st.button("Calcular Risco de Readmissão")
if previsao:
    st.write("Dados recebidos:")
    st.write({
        "idade": idade,
        "tempo_hospitalizacao": tempo_hospitalizacao,
        "n_lab_procedures": n_lab_procedures,
        "n_procedures": n_procedures,
        "n_medications": n_medications
    })