# gerando dados ficticios

import pandas as pd
import random
from faker import Faker

faker = Faker('pt_BR')

dados_pessoas = []

for _ in range(10):
    nome = faker.name()
    cpf = faker.cpf()
    idade = random.randint(18, 60)
    data_nascto = faker.date_of_birth(minimum_age=idade, maximum_age=idade).strftime("%d/%m/%Y")
    enderco = faker.address()
    estado = faker.state()
    pais = 'Brasil'

    pessoa = {
        'nome': nome,
        'cpf': cpf,
        'idade': idade,
        'data_nascto': data_nascto,
        'enderco': enderco,
        'estado': estado,
        'pais': pais
    }

    dados_pessoas.append(pessoa)

df_pessoas = pd.DataFrame(dados_pessoas)
print(df_pessoas)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)
