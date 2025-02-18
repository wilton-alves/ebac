import pandas as pd
import numpy as np


pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('clientes-v3-preparado.csv')

print(df)

print('Estatística com Pandas')
print('Média: ', df['salario'].mean())
print('Mediana: ', df['salario'].median())
print('Variância: ', df['salario'].var())
print('Desvio Padrão: ', df['salario'].std())
print('Moda: ', df['salario'].mode()[0])
print('Mínimo: ', df['salario'].min())
print('Quartis:\n', df['salario'].quantile([0.25, 0.5, 0.75]))
print('Máximo: ', df['salario'].max())
print('Contagem de não nulos: ', df['salario'].count().sum())
print('Soma: ', df['salario'].sum())

# Estrutura dos dados
print('Coluna do DataFrame:\n', df['salario'])
print('Array do Campo: ', df['salario'].values)


# Estatísticas com Numpy
print('Estatísticas com Numpy')
print('Média com coluna: ', np.mean(df['salario']))
print('Média com array: ', np.mean(df['salario'].values))

array_campo = df['salario'].values
print('Mediana com array: ', np.median(array_campo))
print('Variância com array: ', np.var(array_campo))
print('Desvio Padrão com array: ', np.std(array_campo))
print('Mínimo com array: ', np.min(array_campo))
print('Quartis com array: ', np.quantile(array_campo, [0.25, 0.5, 0.75]))
print('Porcentagem 25%, 50% e 75%: ', np.percentile(array_campo, [25, 50, 75]))
print('Máximo com array: ', np.max(array_campo))
print('Contagem de Não Zeros com array: ', np.count_nonzero(array_campo))
print('Soma com array: ', np.sum(array_campo))