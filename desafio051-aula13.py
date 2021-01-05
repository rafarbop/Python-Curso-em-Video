# Desafio 51 Curso em Video Python

# By Rafabr


from time import sleep
from sys import exit
from os import system
from estrutura_modelo import cabecalho,rodape

cabecalho(51,"Cálcular os 10 primeiros termo de uma Progressão Aritmética!")

try:
    p0 = float(input('Digite o Termo inicial da PA: '))
    r = float(input('Digite a razão da PA: '))
except ValueError:
    print('Voçe digitou um valor indevido!')
    exit()

print()

pa = []

for i in range(0,10):
    pa.append(p0 + r*i)    

print(f'A 10 primeiros termos de uma PA com termo inicial {p0} e razão {r} será:\n\n{pa}')

rodape()

