import pandas as pd

"""
O método shape é utilizado para obter as dimensões de um DataFrame, ou seja, o número de linhas e colunas presentes nele. Ele retorna uma tupla contendo esses valores.
df = pd.read_csv(r'hospital_readmissions.csv')
print(df.shape)

linhas = df.shape[0]
colunas = df.shape[1]
print(f'Número de linhas: {linhas}')
print(f'Número de colunas: {colunas}')
"""

"""
Informações sobre o DataFrame, incluindo o número de entradas, colunas, tipos de dados e uso de memória. Ele é útil para obter uma visão geral rápida do conteúdo do DataFrame.

df = pd.read_csv(r'hospital_readmissions.csv')
df.info()
"""

"""
df = pd.read_csv(r'hospital_readmissions.csv')
contagem = df['readmitted'].value_counts()
percentual = df['readmitted'].value_counts(normalize=True) * 100
resultado = pd.DataFrame({'Contagem': contagem, 'Percentual': percentual})
print(resultado)
"""

"""
Hipótese 1: O tempo de internação influencia a probabilidade de readmissão.
Resultados observados:
- A taxa de readmissão apresentou tendência de crescimento conforme o tempo de internação aumentou.
- Os maiores percentuais de readmissão foram observados entre 7 e 10 dias de hospitalização.
- Após esse período, a taxa de readmissão apresentou oscilações, sem manter um crescimento consistente.
Limitações da análise:
- O número de pacientes diminui significativamente para tempos de internação mais elevados (11 a 14 dias).
- Dessa forma, as estimativas para esses grupos possuem menor robustez estatística.
- São necessárias análises complementares para confirmar a força dessa relação.
Conclusão preliminar:
Existe evidência inicial de que pacientes com maior tempo de internação apresentam maior probabilidade de readmissão hospitalar, com um pico observado entre 7 e 10 dias. No entanto, a relação não é linear e requer investigação adicional para entender os fatores subjacentes.
"""

"""
df = pd.read_csv(r'hospital_readmissions.csv')
dias = df.groupby('time_in_hospital')['readmitted'].value_counts().unstack().fillna(0)
percentual = dias.div(dias.sum(axis=1), axis=0) * 100
print(dias)
print(percentual)
"""

"""hipótese 2: Pacientes com histórico de internação anteriores possuem maior probabilidade de readmissão.
Resultado observado: - Foi identificada uma forte relação positiva entre o número de internações prévias e a taxa de readmissão.
- Pacientes sem histórico de internação apresentaram taxa de readmissão de aproximadamente 40%.
- A taxa de readmissão aumentou progressivamente à medida que o número de internações anteriores cresceu.
- Pacientes com cinco internações prévias apresentaram taxa superior a 80%.
Limitações:
- Grupos com valores muito altos de n_inpatient possuem poucas observações e devem ser interpretados com cautela.
Conclusão preliminar:
O histórico de internações anteriores demonstra forte potencial preditivo e pode ser uma das variáveis mais relevantes para o modelo de classificação.
"""

"""
df = pd.read_csv(r'hospital_readmissions.csv')
internados = df.groupby('n_inpatient')['readmitted'].value_counts().unstack().fillna(0)
percentual = internados.div(internados.sum(axis=1), axis=0) * 100
print(internados)
print(percentual)
"""

"""Hipótese 3: Existe associação entre a quantidade de medicamentos administrados e a probabilidade de readmissão hospitalar.
Resultados observados:
- Foi identificada uma tendência de aumento da taxa de readmissão conforme cresce a quantidade de medicamentos administrados.
- Pacientes que receberam até aproximadamente 10 medicamentos apresentaram taxas de readmissão inferiores a 45%.
- A partir de aproximadamente 18 a 25 medicamentos, a taxa de readmissão ultrapassou 50% em diversos grupos.
Limitações:
- Os grupos com grande quantidade de medicamentos possuem poucos pacientes.
- Isso gera maior variabilidade nas estimativas observadas.
Conclusão preliminar:
A quantidade de medicamentos demonstra potencial relação com a readmissão hospitalar, embora o efeito observado seja menos pronunciado do que o identificado para o histórico de internações anteriores.
"""

"""
df = pd.read_csv(r'hospital_readmissions.csv')
medicamentos = df.groupby('n_medications',)['readmitted'].value_counts().unstack().fillna(0)
medicamentos = medicamentos.reindex(columns=sorted(medicamentos.columns), fill_value=0)
pd.set_option('display.max_rows', None)
percentual = medicamentos.div(medicamentos.sum(axis=1), axis=0) * 100
print(f'Medicamentos:\n{medicamentos}')
print(f'Percentual:\n{percentual}')
"""

"""Hipótese 4: Indicadores relacionados ao diabetes estão associados a uma maior probabilidade de readmissão hospitalar.
Variáveis investigadas:
A1Ctest
glucose_test
diabetes_med
change
Resultados observados:
A1Ctest
Pacientes com A1C elevado apresentaram taxa de readmissão um pouco superior aos pacientes com A1C normal.
A associação observada foi fraca:
glucose_test
Pacientes com glicose elevada apresentaram maior taxa de readmissão.
A associação observada foi moderada:
diabetes_med
Pacientes que utilizavam medicação para diabetes apresentaram taxa de readmissão superior aos pacientes sem medicação.
A associação observada foi moderada:
change
Pacientes que tiveram alteração no tratamento apresentaram taxa de readmissão um pouco superior.
A associação observada foi fraca a moderada.
"""

"""
df = pd.read_csv(r'hospital_readmissions.csv')
teste = df.groupby(['A1Ctest'])['readmitted'].value_counts().unstack().fillna(0)
percentual = teste.div(teste.sum(axis=1), axis=0) * 100
print(f'Teste:\n{teste}')
print(f'Percentual:\n{percentual}')
"""

"""
df = pd.read_csv(r'hospital_readmissions.csv')
teste = df.groupby(['glucose_test'])['readmitted'].value_counts().unstack().fillna(0)
percentual = teste.div(teste.sum(axis=1), axis=0) * 100
print(f'Teste:\n{teste}')
print(f'Percentual:\n{percentual}')
"""

"""
df = pd.read_csv(r'hospital_readmissions.csv')
teste = df.groupby(['diabetes_med'])['readmitted'].value_counts().unstack().fillna(0)
percentual = teste.div(teste.sum(axis=1), axis=0) * 100
print(f'Teste:\n{teste}')
print(f'Percentual:\n{percentual}')
"""

"""
df = pd.read_csv(r'hospital_readmissions.csv')
teste = df.groupby(['change'])['readmitted'].value_counts().unstack().fillna(0)
percentual = teste.div(teste.sum(axis=1), axis=0) * 100
print(f'Teste:\n{teste}')
print(f'Percentual:\n{percentual}')
"""

"""Hipótese 5: O diagnóstico principal do paciente está associado à probabilidade de readmissão hospitalar
Resultados observados:
- Pacientes com diagnóstico principal relacionado a Diabetes apresentaram a maior taxa de readmissão (53,6%).
- Doenças Respiratórias apresentaram a segunda maior taxa de readmissão (49,1%).
- Diagnósticos Musculoesqueléticos apresentaram a menor taxa observada (39,5%).
Conclusão preliminar:
Os resultados sugerem que o tipo de doença principal está associado à probabilidade de readmissão hospitalar. Entre os diagnósticos analisados, Diabetes apresentou a associação mais forte com a ocorrência de novas internações.
"""

"""
df = pd.read_csv(r'hospital_readmissions.csv')
diagnosticos = df.groupby(['diag_1'])['readmitted'].value_counts().unstack().fillna(0)
percentual = diagnosticos.div(diagnosticos.sum(axis=1), axis=0) * 100
print(f'Quais os diagnósticos em diag_1: {diagnosticos}')
print(f'Numero total de pacientes: {diagnosticos.sum()}')
print(f'Percentual:\n{percentual}')
"""

"""Hipótese 6: Pacientes com maior utilização prévia do sistema de saúde apresentam maior probabilidade de readmissão.

"""
df = pd.read_csv(r'hospital_readmissions.csv')
utilizacao_ambulatorial = df.groupby('n_outpatient')['readmitted'].value_counts().unstack().fillna(0)
percentual = utilizacao_ambulatorial.div(utilizacao_ambulatorial.sum(axis=1), axis=0) * 100
print(utilizacao_ambulatorial)
print(percentual)


"""
df = pd.read_csv(r'hospital_readmissions.csv')
utilizacao_emergencial = df.groupby('n_emergency')['readmitted'].value_counts().unstack().fillna(0)
percentual = utilizacao_emergencial.div(utilizacao_emergencial.sum(axis=1), axis=0) * 100
print(utilizacao_emergencial)
print(percentual)
"""


"""
Principais descobertas da análise exploratória:

1. O histórico de internações anteriores (n_inpatient) apresentou a associação mais forte com a readmissão hospitalar.

2. Pacientes com diagnóstico principal relacionado a Diabetes apresentaram a maior taxa de readmissão entre os grupos diagnósticos analisados.

3. O tempo de internação apresentou associação positiva com a readmissão, especialmente entre 7 e 10 dias.

4. Pacientes submetidos a maior quantidade de medicamentos apresentaram tendência de maior readmissão.

5. Indicadores relacionados ao diabetes demonstraram associação positiva, porém mais fraca do que variáveis relacionadas ao histórico hospitalar.
"""



