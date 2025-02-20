import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')

df_corr = df[['salario', 'idade', 'anos_experiencia', 'numero_filhos', 'nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod']].corr()

# Heatmap correlação
plt.figure(figsize=(10, 8))
sns.heatmap(df_corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlação entre variáveis')
plt.savefig('graf_heatmap_correlacao.png')
plt.show()

# Countplot
sns.countplot(x='estado_civil', data=df)
plt.title('Distribuição de Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Contagem')
plt.savefig('graf_countplot_estado_civil.png')
plt.show()

# Countplot com agrupamento
sns.countplot(x='estado_civil', hue='nivel_educacao', data=df)
plt.title('Distribuição de Estado Civil por Nível de Educação')
plt.xlabel('Estado Civil')
plt.ylabel('Contagem')
plt.legend(title='Nível de Educação')
plt.savefig('graf_countplot_com_hue.png')
plt.show()