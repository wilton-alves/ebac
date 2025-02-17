'''
Continuando o exercício anterior, seu código deve conter as ações abaixo. Todos os campos devem ser criados no mesmo DataFrame df:

Crie o campo Nota_MinMax com a transformação do campo Nota para numérico em uma escala de 0 a 1, utilizando o MinMaxScaler.
Crie o campo N_Avaliações_MinMax com a transformação do campo N_Avaliações para numérico em uma escala de 0 a 1,
utilizando o MinMaxScaler.
Crie o campo Desconto_MinMax com a transformação do campo Desconto para numérico em uma escala de 0 a 1, utilizando o MinMaxScaler.
Crie o campo Preco_MinMax com a transformação do campo Preco para numérico em uma escala de 0 a 1, utilizando o MinMaxScaler.

Crie o campo Marca_Cod utilizando o método LabelEncoder para transformar o campo Marca em numérico.
Crie o campo Material_Cod utilizando o método LabelEncoder para transformar o campo Material em numérico.
Crie o campo Temporada_Cod utilizando o método LabelEncoder para transformar o campo Temporada em numérico.
'''

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

df = pd.read_csv('/data/ecommerce_tratados_ex2.csv')

# Escreva seu código abaixo

df['Nota_MinMax'] = MinMaxScaler().fit_transform(df[['Nota']])

df['N_Avaliações_MinMax'] = MinMaxScaler().fit_transform(df[['N_Avaliacoes']])

df['Desconto_MinMax'] = MinMaxScaler().fit_transform(df[['Desconto']])

df['Preco_MinMax'] = MinMaxScaler().fit_transform(df[['Preco']])

df['Marca_Cod'] = LabelEncoder().fit_transform(df['Marca'])

df['Material_Cod'] = LabelEncoder().fit_transform(df['Material'])

df['Temporada_Cod'] = LabelEncoder().fit_transform(df['Temporada'])
