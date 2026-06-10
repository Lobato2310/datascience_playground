import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
defaults = joblib.load(BASE_DIR / "models" / "feature_defaults.pkl")

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
        
        'n_outpatient': [defaults['n_outpatient']],
        'n_inpatient': [defaults['n_inpatient']],
        'n_emergency': [defaults['n_emergency']],

        'medical_specialty': [defaults['medical_specialty']],
        'diag_1': [defaults['diag_1']],
        'diag_2': [defaults['diag_2']],
        'diag_3': [defaults['diag_3']],

        'glucose_test': [defaults['glucose_test']],
        'A1Ctest': [defaults['A1Ctest']],
        'change': [defaults['change']],
        'diabetes_med': [defaults['diabetes_med']],
    })
        
        
    resultado = pipeline.predict(entrada)
    probabilidade = pipeline.predict_proba(entrada)
    
    
    prob_yes = probabilidade[0][1]          
    percentual = prob_yes * 100             

    if resultado[0] == 'yes':
        st.error(f"Alto risco de readmissão")
    else:
        st.success(f"Baixo risco de readmissão")

    st.metric(
        label="Probabilidade de readmissão",
        value=f"{percentual:.1f}%"
    )

    st.info(
        "As variáveis não preenchidas foram substituídas por valores de "
        "referência calculados a partir da média e moda do conjunto de treino."
    )
