import matplotlib.pyplot as plt
import pandas as pd

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas
# https://matplotlib.org/stable/users/explain/colors/colormaps.html

df = pd.read_csv('clientes-v3-preparado.csv')
# print(df.head(20).to_string())

# # Gráfico de barras
# plt.figure(figsize=(10, 6))
# df['nivel_educacao'].value_counts().plot(kind='bar', color='#90ee70')
# plt.title('Divisão de escolaridade - 1')
# plt.xlabel('Nível de Escolaridade')
# plt.ylabel('Quantidade')
# plt.xticks(rotation=0)
# plt.show()

X = df['nivel_educacao'].value_counts().index
Y = df['nivel_educacao'].value_counts().values

# plt.figure(figsize=(10, 6))
# plt.bar(X, Y, color='#60aa65')
# plt.title('Divisão de escolaridade - 2')
# plt.xlabel('Nível de Escolaridade')
# plt.ylabel('Quantidade')
# plt.xticks(rotation=0)
# plt.show()

# # Gráfico de pizza
# plt.figure(figsize=(10, 6))
# plt.pie(Y, labels=X, autopct='%.1f%%', startangle=90)
# plt.title('Divisão de escolaridade - 3')
# plt.show()

# Gráfico de dispersão com cmap
plt.hexbin(df['idade'], df['salario'], gridsize=40, cmap='Blues')
plt.colorbar(label='Frequência')
plt.title('Idade X Salário')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.show()