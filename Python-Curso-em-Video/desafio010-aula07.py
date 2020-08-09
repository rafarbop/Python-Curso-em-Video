# Desafio 10 Curso em Video Python

# Converte um valor em reais para dólares americanos!

#By Rafabr

import sys,time

print('\nDesafio 10')
print('Este programa converte um valor em reais para dólares americanos!\n')

try:
    reais = float(input('Digite o valor em reais que deseja converter: '))
    print()
except ValueError:
    print('\nNao foi digitado um valor válido\n')
    time.sleep(2)
    sys.exit()

print('Considerando a taxa de conversão atual: U$ 1.00 = R$ 3.27\n')

dolares = reais / 3.27

print('Com R$ {:.2f}, voçe pode adquirir U$ {:.2f}'.format(round(reais,2),round(dolares,2)))

print('\n---Fim da execução---\n')