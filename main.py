#Dependencias do projeto
import requests
from bs4 import BeautifulSoup
import tabulate


headers = {'user-Agent': 'Mozila/5.0'} #Permite fazer o acesso ao servidor como se fosse um navegador web.

resposta = requests.get('https://www.fundamentus.com.br/fii_resultado.php', headers=headers) #Faz a requisição na página especificada.

soup = BeautifulSoup(resposta.text, 'html.parser')


linhas = soup.find(id='tabelaResultado').find('tbody').find_all('tr') #Pega todas as linhas da tabela exceto o cabeçalho

for linha in linhas:
    dados_fundo = linha.find_all('td')#busca todas as células que estão dentro de cada linha.
    print(
        f'[ {dados_fundo[2].text}]\n'
        f'\tCotação:[ {dados_fundo[1].text}]\n'
        f'\tSetor:[ {dados_fundo[4].text}]\n'
        f'\tDY:[ {dados_fundo[5].text}]\n'
        f'\tP/VP:[ {dados_fundo[5].text}]\n'
          )




