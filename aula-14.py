## Expressões Regulares

import re
import requests

email_teste = 'asasad@asad.com'
string_de_teste = "O gato é bonito, a gata, os gatoes"
requisicao = requests.get("http://lacoxinha.com.br/contato")

padrao_email = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text)
padrao = re.search(r'gat\w', string_de_teste) # RAW String
padrao1 = re.findall(r'gat\w*', string_de_teste)
padrao1_1 = re.findall(r'gat\w+', string_de_teste)
padrao1_2 = re.findall(r'gat\w.', string_de_teste)
padrao1_3 = re.findall(r'[gat]+w+', string_de_teste)
padrao2 = re.search(r'gat.', string_de_teste) # RAW String

if padrao:
    print(padrao.group())
else:
    print("Padrão não encontrado")

print("Oi pessoal \nSegunda Linha")