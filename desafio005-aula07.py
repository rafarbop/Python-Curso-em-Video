# Desafio 5 Curso em vídeo Python

# Receber um número do usuário emostrar sucessor e antecessor

#By Rafabr

import sys,time

import os
os.system('clear')
print('\033[1;47;30m',end="")
print('\n'+'*'*80)
print('Desafio 5'.center(80))
print('Este programa mostra o antecessor e o sucessor de qualquer número'.center(80))
print(80*'*')
print('\033[m',end="")
print('\033[1;36m')

try:
    x = int(input('Digite um número inteiro: '))
    print()
except ValueError:
    print('\nNao foi digitado um número inteiro\n')
    time.sleep(2)
    sys.exit()

print (f'O antecessor do número digitado é {x-1}')
print (f'O sucessor do número digitado é {x+1}')
print ('Sequência:',x-1,x,x+1)

print('\n---Fim da execução---\n')