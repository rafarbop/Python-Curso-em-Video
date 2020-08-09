# Desafio 6 Curso em Video Python

# Receber um número da usuário e informar o seu dobro, triplo e a raiz quadrada

import sys,time

print('Desafio 6\n')

try:
    x = float(input('Digite número qualquer:\n'))
except ValueError:
    print('Nao foi digitado um valpr válido')
    time.sleep(2)
    sys.exit()

print(f'O dobro de {x} é {2*x}')
print(f'O triplo de {x} é {3*x}')
print (f'A raiz quadrada de {x} é {x**(1/2)}')