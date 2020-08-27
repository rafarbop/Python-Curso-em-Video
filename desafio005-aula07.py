# Desafio 5 Curso em vídeo Python

# Receber um número do usuário emostrar sucessor e antecessor

#By Rafabr

import sys,time

print('\nDesafio 5')
print('Este programa mostra o antecessor e o sucessor de qualquer número.\n')

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