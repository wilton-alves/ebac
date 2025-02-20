import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
import joblib

df = pd.read_csv('Python\\clientes-v3-preparado.csv')

# Categorizar 'salario' acima e abaixo da mediana
df['salario_categoria'] = (df['salario'] > df['salario'].median().astype(int)) # 1 = acima da mediana, 0 = abaixo ou igual a mediana

X = df[['idade', 'anos_experiencia', 'nivel_educacao_cod', 'area_atuacao_cod']] # Preditor
Y = df['salario_categoria'] # Prever

# Dividir os dados: Treinamento e Teste
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Criar e treinar o modelo de Regressão Logística
modelo_lr = LogisticRegression()
modelo_lr.fit(X_train, Y_train)

# Para efeitos de comparação, vamos criar também um modelo de Árvore de Decisão
modelo_dt = DecisionTreeClassifier()
modelo_dt.fit(X_train, Y_train)

# Prever valores de teste
Y_prev_lr = modelo_lr.predict(X_test)
Y_prev_dt = modelo_dt.predict(X_test)

# Métricas de avaliação - Regressão Logística
accuracy_lr = accuracy_score(Y_test, Y_prev_lr)
precision_lr = precision_score(Y_test, Y_prev_lr)
recall_lr = recall_score(Y_test, Y_prev_lr)

print('\nMétricas de avaliação - Regressão Logística:')
print(f'Acurácia (Regressão Logística): {accuracy_lr:.2f}')
print(f'Precisão (Regressão Logística): {precision_lr:.2f}')
print(f'Recall OU Sensibilidade (Regressão Logística): {recall_lr:.2f}')

# Métricas de avaliação - Árvore de Decisão
accuracy_dt = accuracy_score(Y_test, Y_prev_dt)
precision_dt = precision_score(Y_test, Y_prev_dt)
recall_dt = recall_score(Y_test, Y_prev_dt)

print('\nMétricas de avaliação - Árvore de Decisão:')
print(f'Acurácia (Árvore de Decisão): {accuracy_dt:.2f}')
print(f'Precisão (Árvore de Decisão): {precision_dt:.2f}')
print(f'Recall OU Sensibilidade (Árvore de Decisão): {recall_dt:.2f}')

'''
Para este conjunto de dados, o modelo de Regressão Logística obteve melhores resultados em termos de acurácia, precisão e recall.
'''

# Salvar os modelos treinados
joblib.dump(modelo_lr, 'modelo_regressao_logistica.pkl')
joblib.dump(modelo_dt, 'modelo_arvore_decisao.pkl')