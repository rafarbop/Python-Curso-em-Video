# Desafio 51 Curso em Video Python
# By Rafabr

from sys import exit
from estrutura_modelo import cabecalho, rodape


cabecalho(51, "Termos de uma Progressão Aritmética - I")

try:
    p0 = float(input('Digite o Termo inicial da PA: '))
    r = float(input('Digite a razão da PA: '))
except ValueError:
    print('Voçe digitou um valor indevido!')
    exit()

print()

pa = []

for i in range(0, 10):
    pa.append(p0 + r*i)

print(f'A 10 primeiros termos da PA será:\n\n{pa}')

rodape()
