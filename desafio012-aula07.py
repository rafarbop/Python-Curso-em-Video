# Desafio 12 Curso em Video Python

# Recebe o preço de um produto e cálcula uma desconto de 5% eno preço.

#By Rafabr

import sys,time

import os
os.system('clear')
print('\033[1;47;30m',end="")
print('\n'+'*'*80)
print('Desafio 12'.center(80))
print('Este programa recebe o preço de um produto e calcula uma desconto de 5%.'.center(80))
print(80*'*')
print('\033[m',end="")
print('\033[1;36m')

try:
    preco = float(input('Digite o preço do produto a ser calculado o desconto: '))
    print()
except ValueError:
    print('\nNao foi digitado um valor válido\n')
    time.sleep(2)
    sys.exit()

preco = preco *0.95

print('O preço do produto com desconto de 5% é R$ {:.2f}'.format(preco))

print('\n---Fim da execução---\n')