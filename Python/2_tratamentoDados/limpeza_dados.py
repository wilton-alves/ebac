import pandas as pd

df = pd.read_csv('clientes.csv')

pd.set_option('display.width', None)
print(df.head())

# Remover dados que não serão utilizados
df.drop('pais', axis=1, inplace=True)

# Normalizar campos de texto
df['nome'] = df['nome'].str.title()
df['endereco'] = df['endereco'].str.lower()
df['estado'] = df['estado'].str.strip()
df['estado'] = df['estado'].str.upper()

# Converter Tipo de Dados
df['idade'] = df['idade'].astype(int)

# Tratar valores nulos
df_fillna = df.fillna(0)  # Preenche valores nulos com 0
df_dropna = df.dropna()  # Remove as linhas que contenham valores nulos
df_dropna4 = df.dropna(thresh=4) # Remove as linhas que contenham 4 ou mais valores nulos
df_dropna_cpf = df.dropna(subset=['cpf'])  # Remove as linhas que contenham valores nulos na coluna 'cpf'

# def conta_remocoes(metodo):
#     remocoes = df.shape[0] - metodo.shape[0]
#     return remocoes

# print('Fillna removeu ', conta_remocoes(df_fillna), ' linhas')
# print('Dropna removeu ', conta_remocoes(df_dropna),  ' linhas')
# print('Dropna(4) removeu ', conta_remocoes(df_dropna4), ' linhas')
# print('Dropna(CPF) removeu ', conta_remocoes(df_dropna_cpf), ' linhas')

# Tratar valores duplicados
print(len(df))
df.drop_duplicates(subset=['cpf'], keep='first', inplace=True)  # Remove os valores duplicados considerando a coluna 'cpf'

print(len(df))

df.fillna('não informado', inplace=True)

df.to_csv('clientes_tratado.csv', index=False)
print(df.head())