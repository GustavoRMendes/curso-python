# Entrada,saída, variáveis, tipos e operadores

print("Hello World \nSegundo Print" )
print("\tTerceiro Print")
print('\tOi')

idade = 19
altura = 1.74
nome_completo = "Gustavo Mendes"
nome = "Gustavo"
print("Meu nome é " + nome + "!")
print(type(nome))
print(idade)
print(type(idade))
print(nome_completo)
print(altura)
print(type(altura))

print(nome,'tem',idade,'anos e',altura,' de altura')


nome_do_usuario = input('Escreva seu nome: ')
idade_do_usuario = input('Insira sua idade: ')
altura_do_usuario = input('Insira sua altura: ')
print(nome_do_usuario, 'tem', idade_do_usuario, 'anos e tem', altura_do_usuario, 'de altura.' )
print(type(nome_do_usuario), type(idade_do_usuario), type(altura_do_usuario))

numero1 = 27
numero2 = 53
resultado = numero1 + numero2
print(resultado)