import pandas as pd

df = pd.read_csv('clientes.csv')

print('\n\n########### VERIFICANDO O INICIO DO ARQUIVO ###########')
print('#######################################################\n\n')

print(df.head().to_string())

print('\n\############ VERIFICANDO O FIM DO ARQUIVO #############')
print('#######################################################\n\n')

print(df.tail().to_string())


print('\n\n################# OUTRAS VERIFICAÇÕES #################')
print('#######################################################\n\n')

print('Qtd de linhas e colunas: ',df.shape)
print('Tipos de dados:\n',df.dtypes)
print('Quantidade de dados nulos:\n',df.isnull().sum())
print('Quantidade de dados nulos por coluna:\n',df.isnull().sum(axis=0))
print('Método Info:\n', df.info())