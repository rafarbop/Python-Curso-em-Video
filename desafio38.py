# Desafio 38 Curso em Video Python

# By Rafabr

import os,time,sys
from estrutura_modelo import cabecalho,rodape

cabecalho(38,"Comparar dois números")

try:
    n1 = int(input('Digite um número inteiro: '))
    n2 = int(input('Digite outro número inteiro: '))
    print()
except ValueError:
    print('Voçe digitou um valor indevido!')
    time.sleep(0.5)
    sys.exit()

if n1 > n2:
    print(f'O primeiro valor digitado, {n1}, é o maior valor!')
elif n1 < n2:
    print(f'O segundo valor digitado, {n2}, é o maior valor!')
else:
    print(f'Não existe valor maior entre os dois números, {n1} e {n2}, eles são iguais!')

rodape()