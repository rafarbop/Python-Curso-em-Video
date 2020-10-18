# Desafio 9 Curso em Video Python

# Mostra a tabuada multiplicativa de um número digitado!

#By Rafabr

import sys,time

import os
os.system('clear')
print('\033[1;47;30m',end="")
print('\n'+'*'*80)
print('Desafio 9'.center(80))
print('Este programa mostra a tabuada multiplicativa de um número digitado!'.center(80))
print(80*'*')
print('\033[m',end="")
print('\033[1;36m')

try:
    n = int(input('Digite um número inteiro: '))
    print()
except ValueError:
    print('\nNao foi digitado um valor válido\n')
    time.sleep(2)
    sys.exit()

print(f'A tabuada multiplicativa do número {n} é:')

for k in [0,1,2,3,4,5,6,7,8,9]:
    print(f'--> {n}*{k} = {n*k}')

print('\n---Fim da execução---\n')