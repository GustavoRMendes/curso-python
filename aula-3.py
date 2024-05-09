# Boolean
verdadeiro = True
falso = False
print(type(verdadeiro))
print(type(falso))

# Comparações: == != > < >= <=
if verdadeiro == True :
    print("Verdade")
elif verdadeiro == False:
    print("Falso")
else:
    print("Nenhum")

# and or

# 1 == 1 and 1 == 2 FALSE
# 1 == 1 and 1 == 1 TRUE
# 1 == 2 or 1 == 1  TRUE
# True or False     TRUE
# True and False    FALSE

if 2 > 1:
    print("2 maior que 1")
else:
    print("1 maior que 2")



idade = 40

if not idade == 40:
    print("Nao tem 40")
else:
    print("Tem 40")