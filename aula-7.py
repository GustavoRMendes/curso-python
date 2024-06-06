print("Olá Mundo")

print(len("Olá mundo!"))

def soma(n1,n2):
    return n1 + n2

print(soma(10,20))

def imprimeOi():
    print("OI")


imprimeOi()

def temSeteLetras(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False

print(temSeteLetras("1234567"))
