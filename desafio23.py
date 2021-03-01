# Desafio 23 Curso em Video Python

# Este programa separa um número em unidades, dezenas, centenas e milhares de um número.

# By Rafabr

import sys
import time
import os

os.system('clear')
print('\nDesafio 23')
print('Este programa separa um número em unidades, dezenas, centenas e milhares de um número.\n')

numero = input('Digite um número natural (Máximo: 9999): ')
print()

if not(numero.isdecimal()) or int(numero) > 9999:
    print("Voçe digitou número diferente do especificado!\n\n")
    sys.exit()

print("Processando...\n")
time.sleep(1)

numero = int(numero)
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centeza = numero // 100 % 10
milhar = numero // 1000 % 10

print(f"Número Digitado: {numero}")
print(f"Unidade: {unidade}")
print(f"Dezena:  {dezena}")
print(f"Centena: {centeza}")
print(f"Milhar:  {milhar}")

print('\n---Fim da execução---\n')
