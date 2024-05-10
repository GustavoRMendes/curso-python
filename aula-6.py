# Tupla / Tuple === ESTÁTICO
tupla = []
minha_tupla = ("Gustavo","Joao")
print(minha_tupla[0])
for nome in minha_tupla:
    print(nome)

minha_tupla = ("Felipe","Ohs") # tem que mudar a tupla toda para ela ser alterada
print(minha_tupla)

if 'Ohs' in minha_tupla:
    print("está!")


# Dicionário (dict)

dicionario = {}
dicionario2 = dict()
meu_dicionario = {
    'nome': "Gustavo",
    'idade': 19,
    'programador': True
}
print(meu_dicionario['programador'])
print(len(meu_dicionario))
meu_dicionario['endereco'] = "Avenida sete de setembro"

print(meu_dicionario)
if 'idade' in meu_dicionario.keys():
    print("verdade")
if 'Gustavo' in meu_dicionario.values():
    print("Tem gustavo")


# Conjunto (set) ===  NÃO TEM ÍNDICE, QUANDO NÃO QUER DADOS REPETIDOS

conjunto = set()
meu_conjunto = {'Gui','Joao'}
meu_conjunto.add("Maria")
print(meu_conjunto)
if 'Maria' in meu_conjunto:
    print("Maria foi encontrada no meu conjunto.")

meu_conjunto.remove("Maria")
