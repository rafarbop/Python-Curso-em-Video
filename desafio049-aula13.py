# Desafio 49 Curso em Video Python

# By Rafabr


from time import sleep
from sys import exit
from os import system
from estrutura_modelo import cabecalho,rodape

cabecalho(49,"Tabuada!")

try:
    num_tab = int(input('Informe o número que deseja ver a tabuada completa: '))
except ValueError:
    print('Voçe digitou um valor indevido!')
    exit()

if num_tab not in list(range(1,11)):
    print('Voçe digitou um valor indevido!')
    exit()

print()
print('Fazer a tabuada aqui!')

rodape()

