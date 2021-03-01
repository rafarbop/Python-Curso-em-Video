# Desafio 34 Curso em Video Python

# Este programa calcula o aumento de salario onde o aumento é maior para que ganha menos.

# By Rafabr

import sys
import time
import os
import random

os.system('clear')
print('\nDesafio 34')
print('Este programa calcula o aumento de salario onde o aumento é maior para que ganha menos.\n\n')

try:
    sal = float(input('Informe a salário atual: ').strip())

except ValueError:
    os.system('clear')
    print('Voçe não digitou um valor válido!')
    time.sleep(0.5)
    sys.exit()

os.system('clear')

if sal < 0:
    os.system('clear')
    print('Voçe digitou uma valor de salário negativo!')
    time.sleep(0.5)
    sys.exit()

print(f'O salário novo será de R$', end="")
print(f'{(sal*1.15 if sal <= 1250 else sal*1.1):.2f}')

print('\n---Fim da execução---\n')
