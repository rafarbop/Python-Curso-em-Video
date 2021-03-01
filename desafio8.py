# Desafio 8 Curso em Video Python

# Converte um valor de metros para centímetros e milímetros

#By Rafabr

import sys,time

import os
os.system('clear')
print('\033[1;47;30m',end="")
print('\n'+'*'*80)
print('Desafio 8'.center(80))
print('Este programa converte um valor de metros para centímetros e milímetros!'.center(80))
print(80*'*')
print('\033[m',end="")
print('\033[1;36m')


try:
    metros = float(input('Digite a medida em metros - OBS. Somente números - : '))
    print()
except ValueError:
    print('\nNao foi digitado um valor válido\n')
    time.sleep(2)
    sys.exit()

print('Escolha para qual medida deseja converter o valor digitado:')
print('(Para sair do programa digite: \'sair\')')
print('1 - Centímetros\n2 - Milímetros')
converter_para = input(':')

while converter_para != '1' and converter_para != '2' and converter_para != 'sair':
    print('Escolha para qual medida deseja converter o valor digitado:')
    print('(Para sair do programa digite: \'sair\')')
    print('1 - Centímetros\n2 - Milímetros')
    converter_para = input(':')

if converter_para == 'sair':
    print('\nExecução encerrada pelo usuário!\n')
    sys.exit()
    print()
if converter_para == '1':
    print(f'\n{metros} metros é equivalente à {metros*100} centímetros!')
if converter_para == '2':
    print(f'\n{metros} metros é equivalente à {metros*1000} milímetros!')

print('\n---Fim da execução---\n')