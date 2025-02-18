'''
Para finalizar, vamos desenvolver um modelo de Regressão Linear:

Divida os dados em 2 partes: 20% para testes e 80% para treinamento. Armazene nas variáveis correspondentes:
x_train, x_test, y_train e y_test. Atenção, você deve utilizar os parâmetros com esses valores: test_size=0.2 e random_state = 42.

Crie um modelo de Regressão Linear, utilizando o sklearn, e ajuste-o sobre os dados de treinamento.
Armazene o modelo na variável modelo_lr.

Faça uma previsão dos valores utilizando a base de teste e armazene o resultado na variável y_prev.
Calcule as seguintes métricas para avaliar o seu modelo: R², RMSE e o desvio padrão do campo Qtd_Vendidos_Cod,
e armazene nas respectivas variáveis: r2, rmse, desvio_padrao.
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, root_mean_squared_error
from math import sqrt

# Carrega os dados
df = pd.read_csv('/data/ecommerce_preparados.csv')
df = df.dropna()

# Define as variáveis preditoras e a variável alvo
X = df[['N_Avaliacoes_MinMax', 'Nota_MinMax', 'Preco_MinMax', 'Desconto_MinMax', 'Temporada_Cod', 'Marca_Freq', 'Material_Freq']]  # Preditor
Y = df['Qtd_Vendidos_Cod']

# Escreve seu código abaixo

# Divide os dados em conjuntos de treino e teste
# Atenção, utilize os parâmetros com esses valores: `test_size=0.2` e `random_state = 42`.
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Cria e treina o modelo de Regressão Linear
modelo_lr = LinearRegression()
modelo_lr.fit(x_train, y_train)

# Faz previsões com o conjunto de teste
y_prev = modelo_lr.predict(x_test)

# Avalia o modelo
r2 = r2_score(y_test, y_prev)
print(f'Coeficiente de Determinação - R²: {r2:.2f}')

rmse = sqrt(mean_squared_error(y_test, y_prev))
print(f"Raiz do Erro Quadrático Médio - RMSE: {rmse:.2f}")

desvio_padrao = df['Qtd_Vendidos_Cod'].std()
print(f"Desvio Padrão do campo Qtd_Vendidos_Cod: {desvio_padrao}")
