import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.max_columns', None)
# pd.set_option('display.max_colwidth', None)

df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head())

# Codificação one-hot para 'estado_civil'
df = pd.concat([df, pd.get_dummies(df['estado_civil'], prefix='estado_civil')], axis=1)

print('\nDataFrame com a codificação one-hot para Estado Civil:', df.head())


# Codificação ordinal para 'nivel_educacao'
educacao_ordem = {'Ensino Fundamental': 1, 'Ensino Médio': 2, 'Ensino Superior': 3, 'Pós-Graduação': 4}
df['nivel_educacao_ordinal'] = df['nivel_educacao'].map(educacao_ordem)

print('\nDataFrame com a codificação ordinal para Nível de Educação:', df.head())


# Transformar 'area_atuacao' em categorias codificadas usando o método .cat.codes
df['area_atuacao_cod'] = df['area_atuacao'].astype('category').cat.codes

print('\nDataFrame com a codificação para Área de Atuação:', df.head())

# Label Encoding para 'estado'
# Label Encoder converte cada valor unico em números de 0 a n_classes-1
label_encoder = LabelEncoder()
df['estado_cod'] = label_encoder.fit_transform(df['estado'])

print('\nDataFrame com o Label Encoding para Estado:', df.head())