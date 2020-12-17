# Desafio 47 Curso em Video Python

# By Rafabr


from time import sleep
from sys import exit
from os import system
from estrutura_modelo import cabecalho,rodape

cabecalho(47,"Números pares entre 1 e 50!")

print('Os números pares entre 1 e 50 são:')
for k in range(0,50,2):
    print(str(k).center(30))

rodape()

