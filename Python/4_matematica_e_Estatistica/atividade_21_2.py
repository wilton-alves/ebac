'''
Continuando nossa análise estatística, siga as instruções:

Calcule a correlação do campo Qtd_Vendidos_Cod, para cada um dos 3 campos N_Avaliacoes_MinMax, Nota_MinMax e Preco_MinMax.
Armazene o resultado correspondente nas variáveis coor_n_avaliacoes, corr_nota, corr_preco.
Obs: Reflita sobre qual tem a maior correlação e o que isso pode indicar.
'''

import pandas as pd

df = pd.read_csv('/data/ecommerce_preparados.csv')
df = df.dropna()

# Escreva seu código abaixo

# Calcula a correlação entre a quantidade vendida e o número de avaliações
corr_n_avaliacoes = df[['Qtd_Vendidos_Cod','N_Avaliacoes_MinMax']].corr()

# Calcula a correlação entre a quantidade vendida e a nota média
corr_nota = df[['Qtd_Vendidos_Cod','Nota_MinMax']].corr()

# Calcula a correlação entre a quantidade vendida e o preço
corr_preco = df[['Qtd_Vendidos_Cod', 'Preco_MinMax']].corr()

# Exibe os resultados
print("Correlação com o número de avaliações:", corr_n_avaliacoes)
print("Correlação com a nota média:", corr_nota)
print("Correlação com o preço:", corr_preco)


'''
['Unnamed: 0' 'Titulo' 'Nota' 'N_Avaliacoes' 'Desconto' 'Marca' 'Material'
 'Genero' 'Temporada' 'Review1' 'Review2' 'Review3' 'Qtd_Vendidos' 'Preco'
 'Nota_MinMax' 'N_Avaliacoes_MinMax' 'Desconto_MinMax' 'Preco_MinMax'
 'Marca_Cod' 'Material_Cod' 'Temporada_Cod' 'Qtd_Vendidos_Cod'
 'Marca_Freq' 'Material_Freq']
'''