#Declaração das libs
import requests
import json

#Acessando a API
requ = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL,EUR-BRL,BTC-BRL')
#Retorno a API
cotacao = requ.json()

#Manipulando os dados
def valores (msg):
  print('.*.*.*.*. Cotação .*.*.*.*.')
  print(msg)
  print()

#Informações dos dados internos da API
  ##name: Nome da moeda
  ##create_date: data da cotação
  ##bid: Valor do dia
valores('MOEDA:'+cotacao['EUR']['name']+ '\nData:'+cotacao['EUR']['create_date']+'\nValor atual: R$'+ cotacao['EUR']['bid'])
valores('MOEDA:'+cotacao['USD']['name']+'\nData:'+cotacao['USD']['create_date']+'\nValor atual: R$'+ cotacao['USD']['bid'])
valores('MOEDA:'+cotacao['BTC']['name']+'\nData:'+cotacao['BTC']['create_date']+'\nValor atual: R$'+ cotacao['BTC']['bid'])