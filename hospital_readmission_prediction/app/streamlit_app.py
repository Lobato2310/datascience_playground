import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "hospital_readmission_pipeline.pkl"

pipeline = joblib.load(MODEL_PATH)
st.title("Previsão de Readmissão Hospitalar")

st.write( """ Aplicação desenvolvida para prever a probabilidade de readmissão hospitalar utilizando Machine Learning. Este modelo foi treinado com 16 variáveis. 
         Para simplificar a demonstração, a aplicação solicita apenas as 5 variáveis mais relevantes identificadas durante a análise de importância das features. """ )

idade = st.selectbox(
    "Faixa etária",
    ['[40-50)', '[50-60)', '[60-70)', '[70-80)', '[80-90)', '[90-100)']
)

tempo_hospitalizacao = st.number_input("Tempo de hospitalização (dias)", min_value=0)

n_lab_procedures = st.number_input( "Quantidade de procedimentos laboratoriais", min_value=0 )

n_procedures = st.number_input( "Quantidade de procedimentos", min_value=0 )

n_medications = st.number_input( "Quantidade de medicamentos", min_value=0 )

previsao = st.button("Calcular Risco de Readmissão")
if previsao:
    entrada = pd.DataFrame({
        'age' : [idade],
        'time_in_hospital': [tempo_hospitalizacao],
        'n_lab_procedures': [n_lab_procedures],
        'n_procedures': [n_procedures],
        'n_medications': [n_medications],
        
        'n_outpatient': [0],
        'n_inpatient': [0],
        'n_emergency': [0],

        'medical_specialty': ['Missing'],
        'diag_1': ['Other'],
        'diag_2': ['Other'],
        'diag_3': ['Other'],

        'glucose_test': ['no'],
        'A1Ctest': ['no'],
        'change': ['no'],
        'diabetes_med': ['no']
    })
        
    st.write(entrada)

    resultado = pipeline.predict(entrada)
    if resultado[0] == 'yes':
        st.error(" Alto risco de readmissão hospitalar")
    else:
        st.success("Baixo risco de readmissão hospitalar")
        
    probabilidade = pipeline.predict_proba(entrada)
        
    risco = probabilidade[0][1]

    st.metric(
        label="Probabilidade de Readmissão",
        value=f"{risco:.1%}"
    )