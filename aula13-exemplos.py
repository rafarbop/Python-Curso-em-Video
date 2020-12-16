#Aula 13 do Curso Python em Video!

#By Rafabr

import time,sys
import os
from estrutura_modelo import cabecalho,rodape

cabecalho(13,"Esta Aula será sobre Estruturas de Repetição FOR!")

print('Exemplo 01 - Imprimindo usando repetição!')
for c in range(0,6):
    print(c)
print('Usado range(0,6)')
print('─── Fim Exemplo 01!\n'.upper()+'─'*30)

print('Exemplo 02 - Imprimindo usando repetição - Testando iteração reversa!')
for c in range(6,0,-1):
    print(c)
print('Usado range(6,0,-1)')
print('─── Fim Exemplo 02!\n'.upper()+'─'*30)

print('Exemplo 03 - Imprimindo usando repetição - Testando iterações com incrementos diversos!')
for c in range(6,0,-2):
    print(c)
print('Usado range(6,0,-2)')
for c in range(0,10,3):
    print(c)
print('Usado range(0,10,3)')
for c in range(0,4,5):
    print(c)
print('Usado range(0,4,5)')
print('─── Fim Exemplo 03!\n'.upper()+'─'*30)

print('Exemplo 04 - Imprimindo usando repetição - Lendo dados do usuário para as repetições!')
i = int(input('Digite o início: '))
f = int(input('Digite o final: '))
passo = int(input('Digite o passo(incremento): '))
for c in range(i,f+1,passo):
    print(c)
print('Usado range(6,0,-1)')
print('─── Fim Exemplo 04!\n'.upper()+'─'*30)

print('Exemplo 05 - Leitura de varios dados usando repetição!')
dados = []
for c in range(0,5):
    dados.append(input(f'Digite o dado{c}: '))
print(dados)
print('─── Fim Exemplo 05!\n'.upper()+'─'*30)

print('Exemplo 06 - Somando varios valores informados usando repetição!')
soma = 0
for c in range(0,5):
    n = int(input('Digite um número: '))
    soma += n
print(f'A soma dos números digitados é {soma}!')
print('─── Fim Exemplo 06!\n'.upper()+'─'*30)

rodape()



