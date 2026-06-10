# Hospital Readmission Prediction
Projeto end-to-end de Data-Science focado em aprendizado, analisando principais métricas contribuintes para readmissão hospitalar

----

## Objetivo
Analisar principais características e histórico do paciente e com o modelo treinado, prever a probabilidade de readmissão hospitalar do paciente, sendo importante para maiores cuidados em casos específicos

----

## Stack Técnica 

| **Etapa** | **Tecnologia** | **Uso** |
|---|---|---|
| **EDA** | Pandas | Análise exploratória |
| **Gráficos** | Matplotlib / Seaborn | Visualização das hipóteses |
| **Treinamento** | Scikit-learn | Modelagem e avaliação |
| **Interface** | Streamlit | Interação do usuário com o modelo |

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

----

## Resultados

| **Modelo** | **Accuracy** | **Precision** | **Recall** | **F1 Score** |
|---|---|---|---|---|
| **Regressão Logística** | 0.6104 | 0.6297 | 0.4160 | 0.5010 |
| **Random Forest** | 0.6074 | 0.5974 | 0.5062 | 0.5480 |
| **Random Forest Tunado** | 0.6150 | 0.6074 | 0.5125 | 0.5559 |

## Por quê escolhi Random Forest Tunado?
O melhor desempenho foi obtido pelo modelo Random Forest Tunado, que alcançou:

Accuracy: 61,50%
Precision: 60,74%
Recall: 51,25%
F1 Score: 55,59%

## Por quê escolhi a métrica F1 para decisão?
Como o objetivo é identificar pacientes com maior risco de readmissão, optou-se por utilizar F1-Score como principal métrica de otimização, pois ela equilibra Precision e Recall.

## Limitações

O modelo foi treinado com 16 variáveis, mas a interface solicita apenas as 5 mais relevantes. 
As 11 variáveis restantes são preenchidas automaticamente com valores de referência 
calculados a partir da média e moda do conjunto de treino, o que pode reduzir a 
confiabilidade da previsão em casos clínicos mais complexos.

Além disso, o F1 Score de 55,59% indica que o modelo ainda erra uma parcela relevante 
dos casos — o que é esperado dado o nível de ruído presente em datasets clínicos públicos.

**Possíveis melhorias futuras:**
- Expor as 16 variáveis na interface, preenchendo automaticamente apenas os campos 
  não informados pelo usuário
- Testar modelos baseados em gradient boosting como XGBoost ou LightGBM
- Adicionar explicabilidade com SHAP

# Conclusão de Negócio

A análise mostrou que pacientes que passaram por um maior número de procedimentos laboratoriais, utilizaram mais medicamentos e permaneceram mais tempo dentro de hospitais apresentaram maior probabilidade de readmissão hospitalar.

Esses fatores podem ser utilizados como indicadores de atenção para identificar pacientes que possivelmente necessitam de um acompanhamento mais próximo após a alta médica.

Embora o modelo não tenha como objetivo substituir a avaliação clínica, ele pode atuar como uma ferramenta de apoio para equipes médicas e gestores hospitalares, auxiliando na identificação antecipada de pacientes com maior risco de retorno ao hospital.

Na prática, soluções desse tipo podem contribuir para uma melhor gestão de recursos, redução de custos associados a readmissões e melhoria do acompanhamento dos pacientes após a internação.


## Como executar localmente

1. Clone o repositório
   git clone https://github.com/seu-usuario/hospital-readmission-prediction.git

2. Crie e ative um ambiente virtual
   python -m venv venv
   venv\Scripts\activate

3. Instale as dependências
   pip install -r requirements.txt

4. Execute a aplicação
   streamlit run app/streamlit_app.py