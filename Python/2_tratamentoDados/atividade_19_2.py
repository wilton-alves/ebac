"""
Vamos continuar a partir dos dados gerados no exercício anterior.
1 - Trate os campos ‘Marca’; ‘Material’ e ‘Temporada’ para os valores serem em minúsculo
2 - Mantenha apenas os registros que tenham no mínimo 8 valores não nulos
"""

import pandas as pd

df = pd.read_csv('/data/ecommerce_ex2.csv')

# Escreva seu código abaixo

# Converter a coluna 'Marca' para letras minúsculas
df['Marca'] = df['Marca'].str.lower()

# Converter a coluna 'Material' para letras minúsculas
df['Material'] = df['Material'].str.lower()

# Converter a coluna 'Temporada' para letras minúsculas
df['Temporada'] = df['Temporada'].str.lower()

# Remover linhas duplicadas
df.drop_duplicates(inplace=True)

# Remover linhas com menos de 8 valores não nulos
# O parâmetro 'thresh' define o número mínimo de valores não nulos necessários para manter a linha
df.dropna(thresh=8, inplace=True)