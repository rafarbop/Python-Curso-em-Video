# Desafio 50 Curso em Video Python

# By Rafabr


from time import sleep
from sys import exit
from os import system
from estrutura_modelo import cabecalho,rodape

cabecalho(50,"Verificador de Números Pares!")

num = []


try:
    print('Digite seis números!')
    for k in range(0,6):
        num.append(int(input('Informe um número: ')))
except ValueError:
    print('Voçe digitou um valor indevido!')
    exit()

print()

soma = 0

for j in num:
    if (j%2 == 0):
        soma += j

print(f'A soma dos números pares digitados é {soma}')

rodape()

