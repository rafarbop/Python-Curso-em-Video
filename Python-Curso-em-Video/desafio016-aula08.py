# Desafio 16 Curso em Video Python

# Separa qualquer número informado em uma parte inteira e outra parte fracionária

#By Rafabr

import sys,time
import math as rafael_bruno_paiva

print('\nDesafio 16')
print('Este programa separa qualquer número informado em uma parte inteira e outra parte fracionária.\n')

numero = float(input('Digite um número qualquer (preferencialmente fracionário): '))
num_inteiro = int(rafael_bruno_paiva.trunc(numero))
num_fracionario = numero - num_inteiro

print(F"A parte inteira de {numero} é: {num_inteiro}")
print(F"A parte fracionária de {numero} é: {num_fracionario}")



print('\n---Fim da execução---\n')