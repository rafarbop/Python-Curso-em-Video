# Desafio 22 Curso em Video Python

# Este programa utiliza diversos métodos de strings para mostrar algumas informações.

#By Rafabr

import sys,time

print('\nDesafio 22')
print('Este programa utiliza diversos métodos de strings para mostrar algumas informações.\n')

print()
nome = str(input('Digite seu nome completo: ')).strip()
print()

print('Maiúsculo: '+nome.upper())
print('Minúsculo: '+nome.lower())
nome_sem_espaco = nome.replace(" ","")
print(f'O nome digitado tem {len(nome_sem_espaco)} caracteres e {len(nome) - len(nome_sem_espaco)} espaços entre as palavras')
nome_separado = nome.split()
print(f'A primeira palavra ({nome_separado[0]}) possui {len(nome_separado[0])} caracteres')

print('\n---Fim da execução---\n')