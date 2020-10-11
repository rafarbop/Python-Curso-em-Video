# Desafio 31 Curso em Video Python

# Este programa calcula o preço de viagem cujo valor depende da distâcia a ser percorrida.

#By Rafabr

import sys,time,subprocess
import random

subprocess.run(['clear'])
print('\nDesafio 31')
print('Este programa calcula o preço de viagem cujo valor depende da distâcia a ser percorrida.\n\n')

try:
    km = int(input('Informe a distâcia a ser percorrida na viagem que pretende fazer (Em km): ').strip())
except ValueError:
    subprocess.run(['clear'])
    print('Voçe digitou um valor não númerico!')
    time.sleep(1)
    sys.exit()

if km < 0:
    subprocess.run(['clear'])
    print('Voçe digitou um valor negativo!\nNão existe distância negativa!')
    time.sleep(1)
    sys.exit()


subprocess.run(['clear'])

if km <= 200:
    print('\nPara essa viagem, o valor por kilometro percorrido será R$ 0,50!')
    print(f'Voçe pagará o total de R$ {km*0.5:.2f}')
else:
    print('\nPara essa viagem, o valor por kilometro percorrido será R$ 0,45!')
    print(f'Voçe pagará o total de R$ {km*0.45:.2f}')


print('\n---Fim da execução---\n')