# Desafio 52 Curso em Video Python

# By Rafabr


from time import sleep
from sys import exit
from os import system
from estrutura_modelo import cabecalho,rodape

cabecalho(52,"Verificador de número primo!")

try:
    numero = int(input('Digite o número a ser análisado: '))
except ValueError:
    print('Voçe digitou um valor indevido!')
    exit()

if numero < 0:
    print('Números negativos não podem ser números primos!')
    sleep(1)
    exit()

print()

numeros_divisores = []

if numero in [0,1]:
    print(f'O número {numero} não é um número primo!')
else:
    for i in range(1,numero):
        if numero%i == 0:
            numeros_divisores.append(i)
    if len(numeros_divisores) == 1:
        print(f'O número {numero} informado é um número primo!')
    else:
        print(f'O número informado não é número primo, pois tem os seguintes divisores:\n\n{numeros_divisores}')



rodape()

