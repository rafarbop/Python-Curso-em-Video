# Desafio 27 Curso em Video Python

# Este programa ler o nome completo de uma pessoa e mostra o primeiro e o último nome.

# By Rafabr

import os

os.system('clear')
print('\nDesafio 27')
print('Este programa ler o nome completo de uma pessoa e mostra o primeiro e o último nome.\n\n')

nome = str(input('Digite o nome completo de uma pessoa: ')).lower().strip()
print()
print(f"O primeiro nome da pessoa informada é: {nome.split()[0].title()}")
print(f"O último nome da pessoa informada é:   {nome.split()[-1].title()}")

print('\n---Fim da execução---\n')
