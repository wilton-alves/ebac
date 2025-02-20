import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')

# # Histograma
# plt.hist(df['salario'])
# plt.show()

# # Histograma com parametros
# plt.figure(figsize=(10, 6))
# plt.hist(df['salario'], bins=100, color='green', alpha=0.9)
# plt.title('Histograma do Salário')
# plt.xlabel('Salário')
# plt.xticks(rotation=45, ticks=range(0, int(df['salario'].max() + 2000), 2000))
# plt.ylabel('Frequência')
# plt.grid(True)
# plt.show()

# Múltiplos gráficos
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1) # 2 linhas, 2 colunas, 1º gráfico
# Diagrama de dispersão
plt.scatter(df['salario'], df['idade'], alpha=0.6)
plt.title('Salário X Idade')
plt.xlabel('Salário')
plt.ylabel('Idade')
plt.grid(True)

plt.subplot(1, 2, 2) # 1 linha, 2 colunas, 2º gráfico
plt.bar(df['nivel_educacao_cod'], df['salario'], alpha=0.6, color='green')
plt.title('Salaário X Nível de Educação')
plt.xlabel('Nível de Educação')
plt.ylabel('Salário')
plt.grid(True)

plt.subplot(2, 2, 3) # 2 linhas, 2 colunas, 3º gráfico
plt.scatter(df['salario'], df['anos_experiencia'], alpha=0.6)
plt.title('Salário X Anos de Experiência')
plt.xlabel('Salário')
plt.ylabel('Anos de Experiência')
plt.grid(True)

plt.tight_layout()
plt.show()