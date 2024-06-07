import requests
import json

def requisicao(titulo):
    try:
        req = requests.get('http://www.omdapi.com/?t=' + titulo)
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print("Erro na conexão.")
        return None


def printar_detalhes(filme):
    print('Titulo: ', filme['Title'])
    print('Atores: ', filme['Actors'])
    print('Ano: ', filme['Year'])
    print('Diretor: ', filme['Director'])
    print('Nota: ', filme['imdbRating'])
    print('')

sair = False
while not sair:
    op = input("Escreva o nome de um filme ou SAIR para fechar: ")

    if op == 'SAIR':
        sair = True
    else:
        filme = requisicao(op)
        if filme['Response'] == "False":
            print("Filme não encontrado")
        else:
            printar_detalhes(filme)

