"""
Dando continuação ao exercício, vamos filtrar os produtos com maiores quantidades de comentários (N_Avaliações).
Para isso, utilizaremos o método do Intervalo Interquartil (IQR).

Passos:

Calcular o IQR: O IQR é a diferença entre o terceiro quartil (Q3) e o primeiro quartil (Q1): iqr = q3 - q1.
Determinar o Limite Superior para Outliers: O limite superior é calculado como limite_alto = q3 + 1.5 * iqr.
Filtrar Produtos Acima do Limite: Filtre os produtos que têm N_Avaliações maior que limite_alto e armazene o
resultado na variável df_avaliados.
"""

import pandas as pd

df = pd.read_csv('/data/ecommerce_ex3.csv')

# Escreva seu código abaixo

# Calcular o intervalo interquartil (IQR)
q1 = df['N_Avaliacoes'].quantile(0.25)
q3 = df['N_Avaliacoes'].quantile(0.75)
iqr = q3 - q1

# Definir o limite superior para identificar outliers
limite_alto = q3 + 1.5 * iqr

# Filtrar os produtos que possuem um número de avaliações maior que o limite superior
df_avaliados = df[df['N_Avaliacoes'] > limite_alto]
