# ANÁLISE EXPLORATÓRIA DE DADOS

import pandas as pd

df = pd.read_csv('clientes-v2.csv', encoding='utf-8-sig')

'''
COLUNAS DO DATASET:
print(df.columns)

nome, cpf, idade, data, endereco, estado, pais, salario, nivel_educacao, numero_filhos, estado_civil, anos_experiencia, area_atuacao

CAMPOS SENSÍVEIS:
cpf, endereco

CAMPOS IRRELEVANTES:
pais

CAMPOS PARA SE TRABALHAR:
nome, idade, data, estado, salario, nivel_educacao, numero_filhos, estado_civil, anos_experiencia, area_atuacao
'''


print('\nHEAD Antes de alterar o formato da coluna Data:\n', df.head())
print('\nTAIL:\n', df.tail())
print('\nSHAPE:\n', df.shape)
print('\nDTypes:\n', df.dtypes)


# Convertendo os tipos de dados:
df['data'] = df['data'].str.strip()
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')
print('\nHEAD Depois de alterar o formato da coluna Data:\n', df.head())
print('\nTAIL:\n', df.tail())

print('\nVerificação inicial:\n', df.info())

print('\nAnálise de dados Nulos:\n', df.isnull().sum())

print('\n% de dados nulos:\n', df.isnull().mean() * 100)
df.dropna(inplace=True)

print('\nConfirmar a remoção de dados nulos:\n', df.isnull().sum().sum())

print('\nAnálise de dados duplicados:\n', df.duplicated().sum())

print('\nAnálise de dados únicos:\n', df.nunique())

print('\nEstatísticas dos dados:\n', df.describe())

df = df[['idade', 'data', 'estado', 'salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao']]
print('\nHEAD:\n', df.head())

df.to_csv('clientes-v2-tratados.csv', index=False, encoding='utf-8-sig')