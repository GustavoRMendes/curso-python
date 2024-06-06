import time
try:
    a = 1200 / 0
except ZeroDivisionError:
    print("Erro na divisao")
except NameError:
    print("Voce digitou errado.")
except Exception as erro:
    print(erro)
    time.sleep(5)
except:
    print("Algum erro aconteceu.")

print("continua")