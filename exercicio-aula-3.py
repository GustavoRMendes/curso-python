'''
Exercício
Faça um programa que pergunte a idade, o peso, a altura de uma pessoa e decida se ela está pronta para ser do
exército. É preciso ter mais de 18 anos, pesar mais de 60 kilos, e ter mais de 1.70 metros
'''

idade = input("Sua idade: ")
peso = input("Seu peso: ")
altura = input("Sua altura: ")

if idade < "18" or peso < "60" or altura < "1.70" :
    print("Não está apta para entrar.")
else:
    print("Apto para entrar.")