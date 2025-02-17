"""
Finalize o exercício seguindo os passos abaixo:

Crie duas novas colunas baseadas na coluna Condicao:
Condicao_Atual: Extraia a primeira parte do campo Condicao (por exemplo, "Novo | +10mil vendidos" deve se tornar "Novo").
Qtd_Vendidos: Extraia a quantidade de itens vendidos do campo Condicao (por exemplo, "Novo | +10mil vendidos"
deve se tornar "+10mil"). Se não houver quantidade especificada, escreva "Nenhum".

Converta a coluna Desconto para o tipo string.
Modifique a coluna Desconto para exibir apenas o valor numérico do desconto (por exemplo, "18% OFF" deve se tornar "18").

--

Saiba mais: Caso queria explorar outra solução, você pode usar a função assign para adicionar ou modificar várias
colunas de um DataFrame de maneira encadeada. Lembre-se de que você pode passar funções lambda dentro do assign
para aplicar transformações nas colunas:

df = pd.read_csv('/data/ecommerce_ex4.csv', encoding='utf-8').assign(
  # Adicione suas transformações aqui
)
Docs: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.assign.html
"""

import pandas as pd

df = pd.read_csv('/data/ecommerce_ex4.csv', encoding='utf-8')

# Escreva seu código abaixo

# Extrair e limpar os dados da coluna 'Condicao'
# A função lambda é usada aqui para pegar a primeira palavra da string na coluna 'Condicao'
# x.split(' ')[0] pega a primeira palavra da string.
df['Condicao_Atual'] = df['Cindicao'].apply(lambda x: x.split(' ')[0])

# A função lambda é usada aqui para pegar a quinta palavra da string na coluna 'Condicao' se existir,
# caso contrário, retorna 'Nenhum'
df['Qtd_Vendidos'] = df['Condicao'].apply(lambda x: x.split(' ')[4] if len(x.split(' ')) > 2 else 'Nenhum')

# Converter a coluna 'Desconto' para string
df['Desconto'] = df['Desconto'].astype(str)

# A função lambda é usada aqui para remover o símbolo '%' da string na coluna 'Desconto'
df['Desconto'] = df['Desconto'].apply(lambda x: x.split('%')[0])

