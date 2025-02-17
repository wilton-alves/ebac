import requests
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
response = requests.get('https://finance.yahoo.com/quote/%5EBVSP/history/', headers=headers)

tabela = pd.read_html(response.text)
print(tabela[0].head(10))