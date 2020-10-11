# Desafio 34 Curso em Video Python

# Este programa calcula o aumento de salario onde o aumento é maior para que ganha menos.

#By Rafabr

import sys,time,subprocess
import random

subprocess.run(['clear'])
print('\nDesafio 34')
print('Este programa calcula o aumento de salario onde o aumento é maior para que ganha menos.\n\n')

try:
    sal = float(input('Informe a salário atual: ').strip())

except ValueError:
    subprocess.run(['clear'])
    print('Voçe não digitou um valor válido!')
    time.sleep(0.5)
    sys.exit()

subprocess.run(['clear'])

if sal < 0:
    subprocess.run(['clear'])
    print('Voçe digitou uma valor de salário negativo!')
    time.sleep(0.5)
    sys.exit()

print(f'O salário novo será de R$',end = "")
print(sal*1.15 if sal <= 1250 else sal*1.1)

print('\n---Fim da execução---\n')