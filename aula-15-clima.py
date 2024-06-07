import requests
import json

cidade = input("Escreva sua cidade: ")
requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=29a246b1b59f2718d4e4c81c23a8e5a9')

tempo = json.loads(requisicao.text)

print('Condição do tempo: ', tempo['weather'][0]['main'])
print('Temperatura: ', float(tempo['main']['temp']) - 273.15)