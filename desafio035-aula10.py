# Desafio 35 Curso em Video Python

# Este programa verifica se 3 comprimentos de retas informados formam um triângulo.

#By Rafabr

import sys,time,subprocess
import random

subprocess.run(['clear'])
print('\nDesafio 35')
print('Este programa verifica se 3 comprimentos de retas informados formam um triângulo.\n\n')

try:
    retas = str(input("Informe 3 medidas de reta separadas por virgula ','(Ex.: 4,5,6): ")).strip().split(',')
    r1 = float(retas[0])
    r2 = float(retas[1])
    r3 = float(retas[2])

except ValueError:
    subprocess.run(['clear'])
    print('Voçe não digitou valores válidos!')
    time.sleep(0.5)
    sys.exit()

except IndexError:
    subprocess.run(['clear'])
    print('Voçe não digitou 3 valores!')
    time.sleep(0.5)
    sys.exit()

subprocess.run(['clear'])

if len(retas)>3:
    subprocess.run(['clear'])
    print('Voçe digitou mais que 3 valores!')
    time.sleep(0.5)
    sys.exit()

if r1<0 or r2<0 or r3<0:
    subprocess.run(['clear'])
    print('Voçe digitou valores negativos!')
    time.sleep(0.5)
    sys.exit()
 
t= 0

if r1 < r2 + r3:
    t = t + 1
if r2 < r1 + r3:
    t = t + 1
if r3 < r2 + r1:
    t = t + 1

if t == 3:
    print(f'As retas de medidas {retas}, formam um triângulo!')
else:
    print(f'As retas de medidas {retas}, NÃO formam um triângulo!')

print('\n---Fim da execução---\n')