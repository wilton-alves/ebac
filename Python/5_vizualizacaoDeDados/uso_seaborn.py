import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('Python\\clientes-v3-preparado.csv')

# # Gráfico de dispersão
# sns.jointplot(x='idade', y='salario', data=df, kind='scatter')
# plt.show()

# # Gráfico de Densidade
# plt.figure(figsize=(10, 6))
# sns.kdeplot(df['salario'], fill=True, color='#863e9c')
# plt.title('Densidade de Salário')
# plt.xlabel('Salário')
# plt.ylabel('Densidade')
# plt.show()

# # Gráfico de Pairplot - Dispersão e Histograma
# sns.pairplot(df[['idade', 'salario', 'anos_experiencia', 'nivel_educacao']])
# plt.show()

# # Gráfico de Regressão
# sns.regplot(x='idade', y='salario', data=df, color='#278f65', scatter_kws={'alpha':0.5, 'color':'#34c289'})
# plt.title('Regressão - Idade X Salário')
# plt.xlabel('Idade')
# plt.ylabel('Salário')
# plt.show()

# Gráfico countplot com hue (agrupamento)
sns.countplot(x='estado_civil', hue='nivel_educacao', data=df, palette='pastel')
plt.title('Contagem de Nível de Educação por Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Contagem')
plt.legend(title='Nível de Educação')
plt.show()