# Desafio 33 Curso em Video Python

# Este programa ordena três números em sequência.

# By Rafabr

import sys
import time
import os
import random

os.system('clear')
print('\nDesafio 33')
print('Este programa ordena três números em sequência.\n\n')

try:
    n1 = float(input('Informe o primeiro número: ').strip())
    n2 = float(input('Informe o segundo número: ').strip())
    n3 = float(input('Informe o terceiro número: ').strip())

except ValueError:
    os.system('clear')
    print('Voçe não digitou números válido!')
    time.sleep(0.5)
    sys.exit()

if n1 == n2 or n1 == n3 or n2 == n3:
    os.system('clear')
    print('Voçe digitou 2 números ou mais iguais!')
    time.sleep(0.5)
    sys.exit()

os.system('clear')


if n1 < n2:
    if n1 < n3:
        print(f'O menor número é {n1}')
        if n2 < n3:
            print(f'O maior número é {n3}')
            print(f'A sequência crescente é {n1} -> {n2} -> {n3}')
        else:
            print(f'O maior número é {n2}')
            print(f'A sequência crescente é {n1} -> {n3} -> {n2}')
    else:
        print(f'O menor número é {n3}')
        print(f'O maior número é {n2}')
        print(f'A sequência crescente é {n3} -> {n1} -> {n2}')
else:
    if n2 < n3:
        print(f'O menor número é {n2}')
        if n1 < n3:
            print(f'O maior número é {n3}')
            print(f'A sequência crescente é {n2} -> {n1} -> {n3}')
        else:
            print(f'O maior número é {n1}')
            print(f'A sequência crescente é {n2} -> {n3} -> {n1}')
    else:
        print(f'O menor número é {n3}')
        print(f'O maior número é {n1}')
        print(f'A sequência crescente é {n3} -> {n2} -> {n1}')


print('\n---Fim da execução---\n')
