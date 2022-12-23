#Dependencias do projeto
import requests #Requests permite enviar solicitações HTTP/1.1 com extrema facilidade. Não há necessidade de adicionar strings de consulta manualmente aos seus URLs ou de codificar seus dados POST. Keep-alive e pool de conexão HTTP são 100% automáticos, graças a urllib3
from bs4 import BeautifulSoup# Beautiful Soup é uma biblioteca Python para extrair dados de arquivos HTML e XML. Ele funciona com seu analisador favorito para fornecer formas idiomáticas de navegar, pesquisar e modificar a árvore de análise. Geralmente economiza horas ou dias de trabalho dos programadores.
import tabulate #Biblioteca de manipulação de tabelas.
import locale
from modelos import FundoImobiliario, Estrategia #importa a classe FundoImobiliário.

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8") #Faz a conversão dos dados.
def trata_porcentagem(porcentagem_str):
  #'7,04%
  #7,04
  #None
  return locale.atof(porcentagem_str.split('%')[0])

def trata_decimal(decimal_str):
  return locale.atof(decimal_str)




headers = {'user-Agent': 'Mozila/5.0'} #Permite fazer o acesso ao servidor como se fosse um navegador web.

resposta = requests.get('https://www.fundamentus.com.br/fii_resultado.php', headers=headers) #Faz a requisição na página especificada.

soup = BeautifulSoup(resposta.text, 'html.parser')


linhas = soup.find(id='tabelaResultado').find('tbody').find_all('tr') #Pega todas as linhas da tabela exceto o cabeçalho
#modelo = modelos()


resultado = [] #lista que vai guardar as estrategias.
estrategia = Estrategia(cotacao_atual_minima= 50.0, dividiend_yield_minimo=5, p_vp_minimo=0.70, valor_mercado_minimo=200000000, liquidez_minima= 50000, qt_imoveis_minima=5, vacancia_media_maxima=10)

for linha in linhas:

    dados_fundo = linha.find_all('td')
    codigo = dados_fundo[0].txt
    seguimento = dados_fundo[1].txt
    cotacao_atual = trata_decimal(dados_fundo[2].txt)
    ffo_yield = trata_porcentagem(dados_fundo[3].txt)
    dividiend_yield = trata_porcentagem(dados_fundo[4].txt)
    p_vp = trata_decimal(dados_fundo[5].txt)
    valor_mercado = trata_decimal(dados_fundo[6].txt)
    liquidez = trata_decimal(dados_fundo[7].txt)
    qt_imoveis = int(dados_fundo[8].txt)
    preco_n2 = trata_decimal(dados_fundo[9].txt)
    aluguel_n2 = trata_decimal(dados_fundo[10].txt)
    cap_rate = trata_porcentagem(dados_fundo[11].txt)
    vacancia_media = trata_porcentagem(dados_fundo[12].txt)


fundo_imobiliario = FundoImobiliario(codigo, seguimento, cotacao_atual, ffo_yield, dividiend_yield, p_vp, valor_mercado, liquidez, qt_imoveis, preco_n2, aluguel_n2, cap_rate, vacancia_media)#instancia a classe

if estrategia.aplica_estrategia(fundo_imobiliario): #Se for verdadeiro adiciona a lista.
  resultado.append(fundo_imobiliario)





    #dados_fundo = linha.find_all('td') #busca todas as células que estão dentro de cada linha.
    #print(
    #    f'[ {dados_fundo[2].text}]\n'
     ##  f'\tSetor:[ {dados_fundo[4].text}]\n'
       # f'\tDY:[ {dados_fundo[5].text}]\n'
        #f'\tP/VP:[ {dados_fundo[5].text}]\n'
         # )







      




