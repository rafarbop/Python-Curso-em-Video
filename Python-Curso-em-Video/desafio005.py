#Desafio 5 Curso em vídeo Python

#Receber um número do usuário emostrar sucessor e antecessor

import sys,time

print('Desafio 5\n')

try:
    x = int(input('Digite um número inteiro:\n'))
except ValueError:
    print('Nao foi digitado um número inteiro')
    time.sleep(2)
    sys.exit()

print (f'O antecessor do número digitado é {x-1}')
print (f'O sucessor do número digitado é {x+1}')
print (x-1,x,x+1)