import os
import requests

def enviar_arquivo():
    caminho = os.getenv('FILE_PATH', 'C:/Users/walve/Downloads/Resultados_CE.csv')

    if not os.path.exists(caminho):
        print('Arquivo não encontrado')
        return
    
    with open(caminho, 'rb') as file:
        requisicao = requests.post('https://file.io', files={'file': file})
        saida_requisicao = requisicao.json()

        if 'link' in saida_requisicao:
            url = saida_requisicao['link']
            print('Arquivo enviado. Link: ', url)
        else:
            print('Erro ao enviar o arquivo. Nenhum link recebido.')
            return


if __name__ == "__main__":

    from bs4 import BeautifulSoup
    arquivo = 'C:/Users/walve/Downloads/teste_file_io.txt'
    if not os.path.exists(arquivo):
        print('Arquivo não encontrado')
        exit()

    with open(arquivo, 'rb') as file:
        response = requests.post('https://file.io', files={'file': file})

        # se a resposta for um arquivo json
        if response.headers['Content-Type'] == 'application/json':
            print(response.json())
        else:
            soup = BeautifulSoup(response.text, features='html.parser')
            print(soup.body.text)