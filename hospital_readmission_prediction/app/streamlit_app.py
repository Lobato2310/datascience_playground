import streamlit as st

st.title("Previsão de Readmissão Hospitalar")
st.write("Configurando o ambiente de forma simples!")

nome = st.text_input("Digite seu nome:")
idade = st.number_input("Informe sua idade:")
tempo_hospitalizacao = st.number_input("Por quantos dias voce já esteve hospitalizado?")
medicamentos = st.number_input("Quantos medicamentos foram receitados?")
risco_de_readmissao = st.button("Veja a previsão de ser novamente hospitalizado")
if nome:
    st.write(f"")
