# Desafio 48 Curso em Video Python

# By Rafabr


from time import sleep
from sys import exit
from os import system
from estrutura_modelo import cabecalho,rodape

cabecalho(48,"Soma dos Números Ímpares de um intervalo!")

print('Os números ímpares e múltiplos de 3 entre 1 e 500 são:')

soma = 0
for k in range(0,500,3):
    if ((k%2)!= 0 ):
        soma += k
        print(str(k).rjust(3,'0'),end='  ')

print(f'\n\nA soma dos números acima é {soma}')

rodape()

