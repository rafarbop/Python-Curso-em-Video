# Desafio 32 Curso em Video Python

# Este programa verifica se o ano informado é bissexto.

# By Rafabr

import sys
import time
import os
import random

os.system('clear')
print('\nDesafio 32')
print('Este programa verifica se o ano informado é bissexto\n\n')

try:
    ano = int(input('Informe o ano que deseja verificar: ').strip())
except ValueError:
    os.system('clear')
    print('Voçe não digitou um ano válido!')
    time.sleep(1)
    sys.exit()

if ano < 0:
    os.system('clear')
    print('Voçe digitou um ano negativo!\n')
    time.sleep(1)
    sys.exit()


os.system('clear')

if (ano % 4) == 0:
    print(f'\nVoçe informou o ano {ano}.')
    print(f'\n{ano} é um ano bissexto!')
else:
    print(f'\nVoçe informou o ano {ano}.')
    print(f'\n{ano} não é um ano bissexto!')

print('\n---Fim da execução---\n')
