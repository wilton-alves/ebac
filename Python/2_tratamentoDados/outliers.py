import pandas as pd
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('clientes_tratado.csv')

df_filtro_basico = df[df['idade'] > 100]
print('Filtro Básico:\n', df_filtro_basico[['nome', 'idade']])

# identificando outliers com o z-score
z_score = stats.zscore(df['idade'].dropna())
outliers_zs = df[z_score >= 0.15]
print('\nOutliers com Z-score:\n', outliers_zs[['nome', 'idade']])

df_zscore = df[(stats.zscore(df['idade']) < 0.15)]
print('\nSem outliers com Z-score:\n', df_zscore[['nome', 'idade']])


# identificando outliers com o IQR

Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

print('\nLimites do IQR:\nLimite inferior: ', limite_inferior, '\nLimite Superior: ',limite_superior)

outliers_iqr = df[(df['idade'] < limite_inferior) | (df['idade'] > limite_superior)]
print('\nOutliers com IQR:\n', outliers_iqr[['nome', 'idade']])


# Filtrar os dados com base nos limites do IQR

df_iqr = df[(df['idade'] >= limite_inferior) & (df['idade'] <= limite_superior)]
print('\nSem outliers com IQR:\n', df_iqr[['nome', 'idade']])


# Tratar endereços inválidos
df['endereco'] = df['endereco'].apply(lambda x: 'Endereço inválido' if len(x.split('\n')) < 3 else x)
print('\nEndereços inválidos:', (df['endereco'] == 'Endereço inválido').sum())

# Tratar nomes inválidos
df['nome'] = df['nome'].apply(lambda x: 'Nome inválido' if isinstance(x, str) and len(x) > 50 else x)
print('\nNomes inválidos:', (df['nome'] == 'Nome inválido').sum())

print('\nTratamento de outliers concluído!\n', df)
df.to_csv('clientes_remove_outliers.csv', index=False)