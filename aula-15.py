import requests
import json
import time
import datetime

while True:
    requisicao = requests.get('http://api.promasters.net.br/cotacao/v1/valores')
    cotacao = json.loads(requisicao.text)
    print("COTAÇÃO ", datetime.datetime.now())
    print('Dólar: ', cotacao['valores']['USD']['valor'])
    time.sleep(2)
