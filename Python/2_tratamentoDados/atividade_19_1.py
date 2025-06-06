"""
Vamos continuar o nosso projeto, realizando o tratamento de dados.
Para facilitar, algumas questões, especifiquei os nomes dos campos, pois iremos usar em outros exercícios. Passo a passo:

1 - Verifique a quantidade de linhas e colunas e armazene na variável linhas_colunas.

2 - Verifique os tipos de dados de todo o dataframe e armazene na variável tipos.

3 - Verifique a quantidade de valores nulos e armazene na variável nulos.

4 - Substitua, no mesmo dataframe, os valores nulos das colunas ‘Temporada’ e ‘Marca’ por ‘Não Definido’. """

import pandas as pd

df = pd.read_csv('/data/ecommerce.csv')

# Verifique a quantidade de linhas e colunas
linhas_colunas = df.shape
print('Verificar a qtd de Linhas e colunas: ', linhas_colunas)

# Verifique os tipos de dados
tipos = df.dtypes
print('Verificar Tipagem:\n', tipos)

# Verifique a quantidade de valores nulos
nulos = df.isnull().sum()
print('Verificar valores nulos:\n', nulos)

#  Substitua os valores nulos das colunas ‘Temporada’ e ‘Marca’ por ‘Não Definido’
df['Temporada'].fillna('Não Definido', inplace=True)
df['Marca'].fillna('Não Definido', inplace=True)

