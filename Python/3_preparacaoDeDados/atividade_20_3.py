'''
Vamos finalizar o exercício com mais algumas preparações. Siga os passos a seguir.
Todos campos devem ser criado no mesmo DataFrame df:

Crie o campo Qtd_Vendidos_Cod com a transformação do campo Qtd_Vendidos para número de acordo com as suas grandezas
('Nenhum', '1', '2', '3', '4', '+5', '+25', '+50', '+100', '+1000', '+10mil' '+50mil'), exemplo +10mil = 10000.

Crie o campo Marca_Freq com a transformação do campo Marca para número de acordo com a frequência do valor.

Crie o campo Material_Freq com a transformação do campo Material para número de acordo com a frequência do valor.

'''

import pandas as pd

df = pd.read_csv('/data/ecommerce_tratados_ex3.csv')

# Escreva seu código abaixo

map_vendidos = {
    'Nenhum': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '+5': 5,
    '+25': 25,
    '+50': 50,
    '+100': 100,
    '+1000': 1000,
    '+10mil': 10000,
     '+50mil': 50000
}

df['Qtd_Vendidos_Cod'] = df['Qtd_Vendidos'].map(map_vendidos)

marca_freq = df['Marca'].value_counts() / len(df)
df['Marca_Freq'] = df['Marca'].map(marca_freq)

material_freq = df['Material'].value_counts() / len(df)
df['Material_Freq'] = df['Material'].map(material_freq)