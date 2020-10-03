# Desafio 27 Curso em Video Python

# Este programa ler o nome completo de uma pessoa e mostra o primeiro e o último nome.

#By Rafabr

import sys,time,subprocess

subprocess.run(['clear'])
print('\nDesafio 27')
print('Este programa ler o nome completo de uma pessoa e mostra o primeiro e o último nome.\n\n')

nome = input('Digite o nome completo de uma pessoa: ')
print()

nome = nome.lower()

print(f"O primeiro nome da pessoa informada é: {nome.split()[0]}")
print(f"O último nome da pessoa informada é:   {nome.split()[-1]}")

print('\n---Fim da execução---\n')