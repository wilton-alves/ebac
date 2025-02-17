import pandas as pd
import numpy as np
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('clientes-v2-tratados.csv')
print(df.head())

# Transformação Logarítmica
df['salario_log'] = np.log1p(df['salario']) # log1p(x) = log(1 + x) --> evita o problema de log(0)
print('\nDataframe após transformação Logarítmica do Salário:\n', df.head())


# Transformação Box-Cox
df['salario_BoxCox'], _ = stats.boxcox(df['salario'] +1)


# Codificação de Frequência para a coluna 'Estado'
estado_freq = df['estado'].value_counts() / len(df)
df['estado_freq'] = df['estado'].map(estado_freq)

print('\nDataframe após Codificação de Frequência para a coluna Estado:\n', df.head())


# Interações
df['interacoes_idade_filhos'] = df['idade'] * df['numero_filhos']
print('\nDataframe após Interações:\n', df.head())