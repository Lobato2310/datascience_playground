# Modelo treinado para prever readmissão Hospitalar
Projeto end-to-end de Data-Science focado em aprendizado, analisando principais métricas contribuintes para readmissão hospitalar

----

## Objetivo
Analisar principais características e histórico do paciente e com o modelo treinado, prever a probabilidade de readmissão hospitalar do paciente, sendo importante para maiores cuidados em casos específicos

----

## Stack Técnica 

| Etapa | Tecnologia | Uso |
|**EDA** | Pandas | Análise exploratória 
|**Gráficos** | Matplotlib & Seaborn | Criação de gráficos para visualização das hipóteses
|**Treinamento** | Scikit-Learn | Desenvolvimento de modelos de treino e de teste, descobrindo o melhor modelo
|**Interação com usuário** | Streamlit | Interação do usuário com o modelo, analisando variáveis preenchidas pelo próprio usuário, calculando a probabilidade de readmissão

----

## Etapa 1: Adquirir o Dataset. 
**Dataset** adquirido da plataforma Kaggle
**Processo:** Adquirir o dataset hospital_readmission.csv na plataforma kaggle


## Etapa 2: EDA 
**Ferramentas:** Python + Pandas + matplotlib
**Processo:** Realizar a Análise Exploratória do dataset, visualizando as principais métricas que contribuem para a readmissão hospitalar e definir intervalos confiáveis de dados
**Código:** 01_eda.ipynb

## Etapa 3: Treinar modelos e salvar melhor modelo
**Ferramentas:** Scikit-learn + Seaborn + joblib
**Processo:** Treinar e Testar modelos, salvando o melhor modelo para a produção
**Código:** 02_data_preparation.ipynb

## Etapa 4: Configurar Streamlit
**Ferramentas:** Streamlit + CSS
**Processo:** Configurar Streamlit para usuário interagir com o melhor modelo salvo, conseguindo preencher suas informações e obter um retorno automático da previsão do modelo e estilizar os visuais com CSS
**Código:** streamlit_app.py + config.toml

---

## Ranking das principais métricas que contribuem para a readmissão hospitalar
1º colocado: Número de procedimentos laboratoriais
2º colocado: Número de medicações
3º colocado: Número de dias em hospitais
4º colocado: Idade
5º colocado: Número de procedimentos
6º colocado: Número de internações

