import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score
import joblib

df = pd.read_csv('Python\\clientes-v3-preparado.csv')

# X = df[['anos_experiencia']] # Preditor
X = df[['idade', 'anos_experiencia', 'nivel_educacao_cod', 'area_atuacao_cod']] # preditor

Y = df['salario'] # prever


# Dividir os dados: Treinamento e Teste
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Criar e treinar o modelo de Regressão Linear
modelo_lr  = LinearRegression()
modelo_lr.fit(X_train, Y_train)


# Prever valores de teste
Y_prev = modelo_lr.predict(X_test)


# Métricas de avaliação
r2 = r2_score(Y_test, Y_prev)
print(f'Coeficiente de determinação (R²): {r2:.2f}')

rmse = root_mean_squared_error(Y_test, Y_prev)
print(f'Raiz do Erro Médio Quadrático (RMSE): {rmse:.2f}')
print(f'Desvio Padrão do campo salario: {df["salario"].std():.2f}')

'''
Para X = df[['anos_experiencia']] a saída está muito próxima do Desvio Padrão do campo salario
Isso significa que o modelo de regressão linear não consegue explicar muito bem a variabilidade nos dados.
Note ainda que o R² está muito baixo. Ou seja, possui uma margem de erro muito alta.

--- Saída para X = df[['anos_experiencia']] ---
Coeficiente de determinação (R²): 0.18
Raiz do Erro Médio Quadrático (RMSE): 3237.46
Desvio Padrão do campo salario: 3478.14
---

Adicionando mais variáveis no modelo, otemos um resultado melhor.
Para X = df[['idade', 'anos_experiencia', 'nivel_educacao_cod', 'area_atuacao_cod']]
o R² teve um aumento significativo, indicando maior assertividade do modelo e o RMSE
variou significativamente em relação ao desvio padrão do campo salario.

--- Saída para X = df[['idade', 'anos_experiencia', 'nivel_educacao_cod', 'area_atuacao_cod']] ---
Coeficiente de determinação (R²): 0.57
Raiz do Erro Médio Quadrático (RMSE): 2334.96
Desvio Padrão do campo salario: 3478.14
---

'''

# Salvar o modelo treinado
joblib.dump(modelo_lr, 'modelo_regressao_linear.pkl')