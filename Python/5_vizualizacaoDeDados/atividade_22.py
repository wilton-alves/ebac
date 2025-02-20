'''
EBAC - Análise de dados
Atividade 22 - Vizualização de dados

Leia o arquivo ‘ecommerce_estatistica.csv’ dentro de um dataframe.
Faça uma análise detalhada dos dados, descubra quais dados gostaria de destacar e crie os seguintes gráficos:
- Gráfico de Histograma
- Gráfico de dispersão
- Mapa de calor
- Gráfico de barra
- Gráfico de pizza
- Gráfico de densidade
- Gráfico de Regressão
Adicione títulos nos gráficos e nos eixos para ficar claro os objetivos dos gráficos
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ecommerce_estatistica.csv')

# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())

# df_numericas = df.select_dtypes(exclude='object')
# df_categoricas = df.select_dtypes(exclude='number')
# print(df_numericas.columns)
# print(df_categoricas.columns)

# Histograma
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Preço', kde=True, bins=20)
plt.title('Distribuição de Preços')
plt.xlabel('Preço')
plt.ylabel('Frequência')
plt.tight_layout()
plt.show()

# Gráfico de dispersão
sns.jointplot(x='Qtd_Vendidos_Cod', y='Temporada_Cod', data=df, kind='scatter').figure.set_size_inches(10, 6)
plt.title('Relação entre Quantidade Vendida e Temporada')
plt.xlabel('Quantidade Vendida')
plt.ylabel('Temporada')
plt.tight_layout()
plt.show()

# Mapa de calor
df_corr = df[['Nota', 'N_Avaliações', 'Qtd_Vendidos_Cod', 'Preço', 'Marca_Cod', 'Material_Cod', 'Temporada_Cod']].corr()
plt.figure(figsize=(10, 6))
sns.heatmap(df_corr, annot=True, linewidth=.5, cmap='flare', fmt='.2f')
plt.title('Correlação entre variáveis do Dataframe')
plt.tight_layout()
plt.show()

# Gráfico de barras
plt.figure(figsize=(10, 6))
sns.countplot(x='Nota', hue='Temporada_Cod', data=df, palette='pastel')
plt.title('Distribuição de Nota por Temporada')
plt.xlabel('Nota')
plt.ylabel('Contagem')
plt.legend(title='Temporada')
plt.tight_layout()
plt.show()

# Gráfico de pizza
X = df['Gênero'].value_counts().index
Y = df['Gênero'].value_counts().values
plt.figure(figsize=(10, 6))
plt.pie(Y, autopct='%.1f%%', startangle=-180, colors=sns.color_palette('pastel'))
plt.title('Distribuição por Gênero')
plt.legend(title='Gênero', labels=X, loc='center left', bbox_to_anchor=(0.95, 0.5))
plt.tight_layout()
plt.show()

# Gráfico de Densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Preço'], fill=True, color='#863e9c')
plt.title('Densidade de Preço')
plt.xlabel('Preço')
plt.ylabel('Densidade')
plt.tight_layout()
plt.show()

# Gráfico de Regressão
plt.figure(figsize=(10, 6))
sns.regplot(x='Preço', y='Desconto', data=df, color='#278f65', scatter_kws={'alpha':0.5, 'color':'#34c289'})
plt.title('Regressão - Preço X Desconto')
plt.xlabel('Preço')
plt.ylabel('Desconto')
plt.tight_layout()
plt.show()