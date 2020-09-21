# Desafio 23 Curso em Video Python

# Este programa mostra a divisão entre unidades, dezenas, centenas e milhares de um número.

#By Rafabr

import sys,time,subprocess

subprocess.run(['clear'])
print('\nDesafio 23')
print('Este programa mostra a divisão entre unidades, dezenas, centenas e milhares de um número.\n\n')

numero = input('Digite um número natural (Máximo: 9999): ')
print()

if not(numero.isdecimal()) or int(numero)>9999:
    print("Voçe digitou número diferente do especificado!\n\n")
    sys.exit()

print("Processando...\n")

numero = "000"+numero
print(f"Número Digitado: {numero}")
print(f"Unidade: {numero[-1]}")
print(f"Dezena:  {numero[-2]}")
print(f"Centena: {numero[-3]}")
print(f"Milhar:  {numero[-4]}")

print('\n---Fim da execução---\n')