# Desafio 30 Curso em Video Python

# Este programa informa se um número informado é par ou ímpar.

# By Rafabr

import sys
import time
import os
import random

os.system('clear')
print('\nDesafio 30')
print('Este programa informa se um número informado é par ou ímpar.\n\n')

try:
    numero = int(input('Informe um número inteiro: ').strip())
except ValueError:
    os.system('clear')
    print('Voçe digitou um valor não reconhecido!')
    time.sleep(1)
    sys.exit()

if ((numero//1)-numero) != 0:
    os.system('clear')
    print('Voçe não digitou um número inteiro!')
    time.sleep(1)
    sys.exit()


os.system('clear')

if (numero % 2) == 0:
    print(f'\nO número digitado, {numero}, é um número par!')
else:
    print(f'\nO número digitado, {numero}, é um número ímpar!')


print('\n---Fim da execução---\n')
