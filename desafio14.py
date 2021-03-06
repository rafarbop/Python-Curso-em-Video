# Desafio 14 Curso em Video Python

# Transforma uma temperatura em Celsuis para Fahrenheit 

#By Rafabr

import sys,time

import os
os.system('clear')
print('\033[1;47;30m',end="")
print('\n'+'*'*80)
print('Desafio 14'.center(80))
print('Este programa transforma uma temperatura em Celsuis para Fahrenheit!'.center(80))
print(80*'*')
print('\033[m',end="")
print('\033[1;36m')


try:
    temp_c = float(input('Digite a temperatura em ºC: '))
    print()
except ValueError:
    print('\nNao foi digitado um valor válido\n')
    time.sleep(2)
    sys.exit()

temp_f = temp_c*1.8+32

print('Resultado: {}ºC equivalem a {}ºF'.format(temp_c,temp_f))

print('\n---Fim da execução---\n')