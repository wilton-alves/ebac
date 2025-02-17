import pymysql
import pandas as pd
from sqlalchemy import create_engine

def conexao_mysql(host, user, password, db, table):
    # criar conexão
    conn = pymysql.connect(host=host, user=user, password=password, db=db)

    # criar cursor
    cursor = conn.cursor()

    # executar consulta
    query = f'SELECT * FROM {table} limit 100'
    cursor.execute(query)

    # Buscar resultados
    resultados = cursor.fetchall()

    # Exibir resultados
    print('Tabela MySQL:')
    for linha in resultados:
        print(linha)

    # Fechar conexão
    cursor.close()
    conn.close()


# Conexão com data frame
def df_conexao_mysql(host, user, pwd, db, table):
    # conn = pymysql.connect(host=host, user=user, password=pwd, db=db)
    conn = create_engine(f'mysql+pymysql://{user}:{pwd}@{host}/{db}') # Conexão com SQLAlchemy

    query = f'SELECT * FROM {table}'
    df = pd.read_sql(query, conn)
    print('Tabela MySQL com DataFrame:\n', df.head())

    # conn.close()
    conn.dispose() # com o SQLAlchemy se usa o dispose ao invés do close para fechar a conexão
    return df


# ler aquivo csv
def conexo_csv(caminho):
    df = pd.read_csv(caminho)
    print('Tabela CSV:\n', df.head())
    df.to_json('C:/Users/walve/Downloads/EBAC/cliente.json', orient='records', index=False) # salvar em json


if __name__ == '__main__':
    # conexao_mysql('localhost', 'root', 'admin', 'loja_informatica', 'cliente')

    df_cliente = df_conexao_mysql('localhost', 'root', 'admin', 'loja_informatica', 'cliente')
    df_cliente.to_csv('C:/Users/walve/Downloads/EBAC/cliente.csv', index=False) # salvar em csv