import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('clientes-v3-preparado.csv')

# Uso do Pandas
print('Estatísticas do DataFrame:\n', df.describe())

print('\nEstatíticas de um campo:\n', df[['salario', 'anos_experiencia']].describe())

print('\nCorrelação entre Salário e idade:\n', df[['salario', 'idade']].corr())
print('\nCorrelação entre Salário e Idade com normalização (MinMaxScaler):\n', df[['salarioMinMaxScaler', 'idadeMinMaxScaler']].corr())
print('\nCorrelação entre Salário e Idade com normalização (StandardScaler):\n', df[['salarioStandardScaler', 'idadeStandardScaler']].corr())
print('\nCorrelação entre Salário e Idade com normalização (RobustScaler):\n', df[['salarioRobustScaler', 'idadeRobustScaler']].corr())

print('Correlação (MinMaxScaler, StandardScaler e RobustScaler):\n', df[['salario', 'idade', 'idadeMinMaxScaler', 'idadeStandardScaler', 'idadeRobustScaler']].corr())

df_filtro_idade = df[df['idade'] < 60]

print('\nCorrelação de clientes menores de 65 anos:\n', df_filtro_idade[['salario', 'idade']].corr())

# Variável Espúria
df['variavel_espuria'] = np.arange(len(df))
print('\nVariavel Espúria:\n', df['variavel_espuria'].values)

pearson_corr = df[['salario', 'idade', 'anos_experiencia', 'idade_anos_experiencia_interac', 'numero_filhos', 'nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod', 'variavel_espuria']].corr(method='pearson')
spearman_corr = df[['salario', 'idade', 'anos_experiencia', 'idade_anos_experiencia_interac', 'numero_filhos', 'nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod', 'variavel_espuria']].corr(method='spearman')

print('\nCorrelação de Pearson:\n', pearson_corr)
print('\nCorrelação de Spearman:\n', spearman_corr)