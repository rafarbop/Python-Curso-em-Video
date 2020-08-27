# Desafio 6 Curso em Video Python

# Receber um número da usuário e informar o seu dobro, triplo e a raiz quadrada

#By Rafabr

import sys,time

print('\nDesafio 6')
print('Este programa mostra o dobro, o triplo e a raiz quadrada de qualquer número.\n')

try:
    x = float(input('Digite número qualquer: '))
    print()
except ValueError:
    print('\nNao foi digitado um valor válido\n')
    time.sleep(2)
    sys.exit()

print(f'O dobro de {x} é {2*x}')
print(f'O triplo de {x} é {3*x}')
print (f'A raiz quadrada de {x} é {x**(1/2)}')

print('\n---Fim da execução---\n')