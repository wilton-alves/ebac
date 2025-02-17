import requests
from bs4 import BeautifulSoup

url = 'https://wiki.python.org.br/AprendaMais'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, features='html.parser')

# Exibe o texto da página
def exibe_texto_completo():
    print(extracao.text.strip())


# Filtrar a exibição pela tag
def filtrar_pela_tag():
    for linha_texto in extracao.find_all('h2'):
        titulo = linha_texto.text.strip()
        print('Titulo: ', titulo)


# Desafio: contar quantas tags H2 e P tem na página
def conta_tag():
    cont_h2 = 0
    cont_p = 0

    for linha_texto in extracao.find_all(['h2','p']):
        if linha_texto.name == 'h2':
            cont_h2 += 1
        elif linha_texto.name == 'p':
            cont_p += 1
    
    print('Total de tags H2: ', cont_h2)
    print('Total de tags P: ', cont_p)


# Desafio: Exibir títulos e parágrafos
def exibe_texto_titulos_e_paragrafos():
    for linha_texto in extracao.find_all(['h2','p']):
        if linha_texto.name == 'h2':
            titulo = linha_texto.text.strip()
            print(f'Titulo: {titulo}\n')
        elif linha_texto.name == 'p':
            paragrafo = linha_texto.text.strip()
            print(f'Parágrafo: {paragrafo}\n')


# Exibir tags aninhadas
def exibe_tags_aninhadas():
    for titulo in extracao.find_all('h2'):
        print(titulo.text.strip())

        for paragrafo in titulo.find_next_siblings('p'):
            for a in paragrafo.find_all('a', href=True):
                print('Link: ', a.text.strip(), ' | URL: ', a['href'])


if __name__ == '__main__':
    exibe_tags_aninhadas()