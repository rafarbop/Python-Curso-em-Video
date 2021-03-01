# Desafio 15 Curso em Video Python

# Calcula o valor a pagar pelo aluguel de um carro

#By Rafabr

import sys,time

print('\nDesafio 15')
print('Este programa calcula o valor a pagar pelo aluguel de um carro.\n')

try:
    km = float(input('Informe quantos Km (número inteiro ou decimal) voçe percorreu com o carro alugado\n: '))
    dias = int(input('Informe quantos Dias (número inteiro) voçe ficou com o carro\n: '))
    print()
except ValueError:
    print('\nNao foi digitado um valor numérico!\n')
    time.sleep(1)
    sys.exit()

print('Valores a pagar por Km e por Dia do carro alugado:\n1 dia --> R$ 60.00\n1 km --> R$ 0.15\n')

valor_aluguel = dias * 60 + km * 0.15

print('O valor total a pagar pelo aluguel do carro será R$ {:.2f}'.format(valor_aluguel))

print('\n---Fim da execução---\n')
