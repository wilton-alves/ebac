# https://finance.yahoo.com/quote/%5EBVSP/history/

import requests
from bs4 import BeautifulSoup
import pandas


print('\n\n#############################')
print('### EXTRAÇÃO COM RESPONSE ###')
print('#############################\n\n')
response = requests.get('https://finance.yahoo.com/quote/%5EBVSP/history/')
print(response.text[:600])


print('\n\n#############################')
print('#### EXTRAÇÃO COM SOUP ######')
print('#############################\n\n')
soup = BeautifulSoup(response.text, features='html.parser')
print(soup.prettify()[:1000])


print('\n\n##############################')
print('#### EXTRAÇÃO COM PANDAS #####')
print('##############################\n\n')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
resposta = requests.get('https://finance.yahoo.com/quote/%5EBVSP/history/', headers=headers)
url_dados = pandas.read_html(resposta.text)
print(url_dados[0].head(10))