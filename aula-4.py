# String e listas

frase = "Oi, Gustavo"
lista = ['Joao','Gui','Fels','Guga']

lista.append("Geraldo")
lista.remove('Fels')
lista.insert(2, "Gustavo")
lista[1] = "Felipe"
contador_gustavo = lista.count("Gustavo")
lista.pop()

frase_separada = frase.split(',')
print(frase_separada)
print(frase.lower())

print(len(lista))
print(contador_gustavo)
print(type(lista))
print(lista[0:2])
print(lista[2])
print(frase[2:8])
print(frase[2:8:2])
print(frase[::-1])
print(lista)
lista.clear()