import pandas as pd
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head())

df = df[['idade', 'salario']]

# Normalização - MinMaxScaler
scaler = MinMaxScaler()  # Intervalo padrão (0, 1)
df['idade_MinMaxScaler'] = scaler.fit_transform(df[['idade']])
df['salario_MinMaxScaler'] = scaler.fit_transform(df[['salario']])

min_max_scaler = MinMaxScaler(feature_range=(-1,1))  # Intervalo personalizado (-1, 1)
df['idade_MinMaxScaler_fr'] = min_max_scaler.fit_transform(df[['idade']])
df['salario_MinMaxScaler_fr'] = min_max_scaler.fit_transform(df[['salario']])


# Padronização - StandardScaler
scaler = StandardScaler()
df['idade_StandardScaler'] = scaler.fit_transform(df[['idade']])
df['salario_StandardScaler'] = scaler.fit_transform(df[['salario']])

# Padronização - RobustScaler
scaler = RobustScaler()
df['idade_RobustScaler'] = scaler.fit_transform(df[['idade']])
df['salario_RobustScaler'] = scaler.fit_transform(df[['salario']])

print(df.head())

print('MinMaxScaler de 0 a 1:')
print(f'Idade:\nMin: {df['idade_MinMaxScaler'].min():.4f} Max: {df['idade_MinMaxScaler'].max():.4f} Mean: {df['idade_MinMaxScaler'].mean():.4f} Std: {df['idade_MinMaxScaler'].std():.4f}')
print(f'Salário:\nMin: {df['salario_MinMaxScaler'].min():.4f} Max: {df['salario_MinMaxScaler'].max():.4f} Mean: {df['salario_MinMaxScaler'].mean():.4f} Std: {df['salario_MinMaxScaler'].std():.4f}')

print('MinMaxScaler de -1 a 1:')
print(f'Idade:\nMin: {df['idade_MinMaxScaler_fr'].min():.4f} Max: {df['idade_MinMaxScaler_fr'].max():.4f} Mean: {df['idade_MinMaxScaler_fr'].mean():.4f} Std: {df['idade_MinMaxScaler_fr'].std():.4f}')
print(f'Salário:\nMin: {df['salario_MinMaxScaler_fr'].min():.4f} Max: {df['salario_MinMaxScaler_fr'].max():.4f} Mean: {df['salario_MinMaxScaler_fr'].mean():.4f} Std: {df['salario_MinMaxScaler_fr'].std():.4f}')

print('\nStandardScaler (Ajuste a média a 0 e desvio padrão a 1):')
print(f'Idade:\nMin: {df['idade_StandardScaler'].min():.4f} Max: {df['idade_StandardScaler'].max():.4f} Mean: {df['idade_StandardScaler'].mean():.4f} Std: {df['idade_StandardScaler'].std():.4f}')
print(f'Salário:\nMin: {df['salario_StandardScaler'].min():.4f} Max: {df['salario_StandardScaler'].max():.4f} Mean: {df['salario_StandardScaler'].mean():.4f} Std: {df['salario_StandardScaler'].std():.4f}')

print('\nRobustScaler (Ajuste a mediana e IQR):')
print(f'Idade:\nMin: {df['idade_RobustScaler'].min():.4f} Max: {df['idade_RobustScaler'].max():.4f} Mean: {df['idade_RobustScaler'].mean():.4f} Std: {df['idade_RobustScaler'].std():.4f}')
print(f'Salário:\nMin: {df['salario_RobustScaler'].min():.4f} Max: {df['salario_RobustScaler'].max():.4f} Mean: {df['salario_RobustScaler'].mean():.4f} Std: {df['salario_RobustScaler'].std():.4f}')
