# Desafio 28 Curso em Video Python

# Este programa  escolhe um número aleatório e verifica se o usuário adivinha o número.

#By Rafabr

import sys,time,subprocess
import random

subprocess.run(['clear'])
print('Desafio 28'.center(80))
print('<>'*40)
print('Este programa escolhe um número aleatório e verifica se o usuário adivinha o número.')
print('<-->'*20)
print('\n')

chave = random.choice(range(6))

try:
    escolha = int(input('O computador escolheu um número entre 0 e 5.\n\
Voçe consegue adivinhar que número é esse?\nTente acertar: ').strip())
except ValueError:
    print('Voçe digitou um valor não númerico!')
    time.sleep(1)
    sys.exit()

if escolha not in range(6):
    subprocess.run(['clear'])
    print('Voçe digitou um valor fora do intervalo solicitado!')
    time.sleep(1)
    sys.exit()

subprocess.run(['clear'])
print('Verificando')
time.sleep(0.5)
subprocess.run(['clear'])
print('Verificando.')
time.sleep(0.5)
subprocess.run(['clear'])
print('Verificando..')
time.sleep(0.5)
subprocess.run(['clear'])
print('Verificando...')
time.sleep(0.5)
subprocess.run(['clear'])
print('Resposta de sua adivinhação!')


if escolha == chave :
    print('\v\tPARABEŃS!\nVoçe acertou o número escolhido aleatoriamente pelo computador!')
else:
    print(f"\nNão foi dessa vez!\nO número escolhido pelo computador foi {chave}!")


print('\n---Fim da execução---\n')