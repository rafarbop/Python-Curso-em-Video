# Desafio 10 Curso em Video Python

# Converte um valor em reais para dólares americanos!

#By Rafabr

import sys,time

import os
os.system('clear')
print('\033[1;47;30m',end="")
print('\n'+'*'*80)
print('Desafio 10'.center(80))
print('Este programa converte um valor em reais para dólares americanos!'.center(80))
print(80*'*')
print('\033[m',end="")
print('\033[1;36m')

try:
    reais = float(input('Digite o valor em reais que deseja converter: '))
    print()
except ValueError:
    print('\nNao foi digitado um valor válido\n')
    time.sleep(2)
    sys.exit()

print('Considerando a taxa de conversão atual: U$ 1.00 = R$ 3.27\n')

dolares = reais / 3.27

print('Com R$ {:.2f}, voçe pode adquirir U$ {:.2f}'.format(round(reais,2),round(dolares-0.005,2)))

print('\n---Fim da execução---\n')