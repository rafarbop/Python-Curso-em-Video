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
print(f'TABUADA DE SOMA DO {num_tab}'.center(40,'-')+'|'+f'TABUADA MULTIPLIÇÃO DO {num_tab}'.center(40,'-'))
for k in list(range(1,11)):
    print(f'{num_tab} + {k} = {num_tab+k}'.ljust(15).center(40)+'|'+f'{num_tab} * {k} = {num_tab*k}'.ljust(15).center(40))
print('-'*81)

rodape()