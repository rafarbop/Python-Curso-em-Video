# Desafio 37 Curso em Video Python

# By Rafabr

import os,time,sys
from estrutura_modelo import cabecalho,rodape

cabecalho(37,"Programa para converter número de base decimal para outras bases númericas")

try:
    n_decimal = int(input('Digite um número inteiro: '))
    base = int(input('Escolha para base númerica deseja converter:\n 1 - Converter para Binário\n 2 - Converter para Octal\n 3 - Converter para Hexadecimal\n\t:'))
except ValueError:
    print('Voçe digitou um valor indevido!')
    time.sleep(0.5)
    sys.exit()

if base == 1:
    print(f'\nO número {n_decimal} convertido para binário é: ',end="")
    print(bin(n_decimal)[2:])
elif base == 2:
    print(f'\nO número {n_decimal} convertido para octal é: ',end="")
    print(oct(n_decimal)[2:])
elif base == 3:
    print(f'\nO número {n_decimal} convertido para hexadecimal é: ',end="")
    print(hex(n_decimal)[2:])
else:
    print('Voçe Escolheu uma opção inexistente!')
    time.slice(0.5)
    sys.exit()




rodape()