# Estruturas de Laço
frase = "Olá, Gustavo Mendes!"
nomes = ['Gustavo', 'Felipe', 'Camilo','Júlio']
print(nomes)

for letra in frase:
    print(letra)

# For x in array:
for nome in nomes:
    print(nome)

# range = cria uma lista de números.
lista_de_numeros = range(0,102,2)

for cont in lista_de_numeros:
    print(cont)

for nome in range(len(nomes)):
    print(nomes[nome])

for i in range(len(nomes)):
    print(nomes[i])
    nomes.append("hello")

print(nomes)


# while
i = 0
while i < 10:
    print("I ainda é menor do que 10: ", i)
    i += 1

# break
numero = 15
while True:
    print(numero)
    if numero == 20:
        break
    numero += 1
print("Saiu do while")