'''
Exercício
Faça um programa que leia a quantidade de pessoas
que serão convidadas para uma festa. Após isso, o
programa irá perguntar o nome de todas as pessoas
e colocar numa lista de convidados. Após isso,
irá imprimir todos os nomes da lista.
'''

convidados = input("Número de convidados: ")
lista = []

i = 0
while i < int(convidados):
    nome_convidado = input("Seu nome: #" + str(i))
    lista.append(nome_convidado)
    i += 1
print('\nNome dos convidados: ')
for nome in lista:
    print(nome)
