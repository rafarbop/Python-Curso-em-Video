# Desafio 30 Curso em Video Python

# Este programa informa se um número informado é par ou ímpar.

#By Rafabr

import sys,time,subprocess
import random

subprocess.run(['clear'])
print('\nDesafio 30')
print('Este programa informa se um número informado é par ou ímpar.\n\n')

try:
    numero = int(input('Informe um número inteiro: ').strip())
except ValueError:
    subprocess.run(['clear'])
    print('Voçe digitou um valor não reconhecido!')
    time.sleep(1)
    sys.exit()

if ((numero//1)-numero)!=0:
    subprocess.run(['clear'])
    print('Voçe não digitou um número inteiro!')
    time.sleep(1)
    sys.exit()


subprocess.run(['clear'])

if (numero%2)==0:
    print(f'\nO número digitado, {numero}, é um número par!')
else:
    print(f'\nO número digitado, {numero}, é um número ímpar!')



print('\n---Fim da execução---\n')