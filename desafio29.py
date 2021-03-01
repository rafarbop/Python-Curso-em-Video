# Desafio 29 Curso em Video Python

# Este programa retorna mensagem de excesso de velocidade baseado em uma condição usando IF

# By Rafabr

import sys
import time
import os
import random

os.system('clear')
print('\nDesafio 29')
print('Este programa  retorna mensagem de excesso de velocidade baseado em uma condição usando IF\n\n')

try:
    v_atual = int(
        input('Informe a velocidade atual do veículo(Em Km/h): ').strip())
except ValueError:
    os.system('clear')
    print('Voçe digitou um valor não reconhecido!')
    time.sleep(1)
    sys.exit()

if v_atual < 0:
    os.system('clear')
    print('Voçe digitou um número negativo!')
    time.sleep(1)
    sys.exit()

multa = 0

os.system('clear')
if v_atual > 80:
    multa = (v_atual-80)*7
    print('O carro ultrapassou o limite de velocidade da via - LIMITE: 80Km/h')
    print(f'Velocidade Informada: {v_atual}km/h')
    print(f'Devido a infração comentida será aplicada multa de R$ {multa:.2f}')
else:
    print(f'Velocidade Informada: {v_atual}km/h')
    print('O veiculo está com velocidade dentro do limite da via!\n\n\
---Não Corra, sua vida não vale o risco!---')


print('\n---Fim da execução---\n')
