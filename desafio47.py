# Desafio 47 Curso em Video Python

# By Rafabr


from time import sleep
from sys import exit
from os import system
from estrutura_modelo import cabecalho,rodape

cabecalho(47,"Números pares entre 1 e um número positivo qualquer!")

try:
    numeroLimite = int(input("Digite um número positivo inteiro: "))
except ValueError:
    print("Valor inválido!")
    sleep(1)
    exit()

print(f'\nOs números pares entre 1 e {numeroLimite} são:')
numerosPares = []
for k in range(0,numeroLimite,2):
    numerosPares.append(k)

print(numerosPares)

rodape()

