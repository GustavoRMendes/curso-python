from veiculo import Veiculo
from carro import Carro
caminhao = Veiculo("azul",3,"ford",10)
print("caminhao")
print(caminhao.cor)
print(caminhao.rodas)
print(caminhao.marca)
print(caminhao.tanque)

carro_azul = Veiculo("azul",4,"bmw",30)
print("carro_azul")
print(carro_azul.cor)
print(carro_azul.rodas)
print(carro_azul.marca)
print(carro_azul.tanque)
carro_azul.abastecer(35)
print(carro_azul.tanque)
