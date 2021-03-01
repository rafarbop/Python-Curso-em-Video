# Desafio 24 Curso em Video Python

# Este programa verifica se uma cidade informada começa com a palavra 'santo(a)' ou 'são'.

# By Rafabr

import os

os.system('clear')
print('\nDesafio 24')
print('Este programa verifica se uma cidade informada começa com a palavra \'santo(a)\' ou \'são\'.\n\n')

cidade = input('Digite o nome de uma Cidade: ')
print()

teste_cidade = cidade.split()[0]

if teste_cidade.lower() in ['santo', 'santa', 'são', 'sao']:
    print("Voçe digitou uma cidade que começa com nome de santo (santo(a) ou são)!")
else:
    print(f"A cidade que voçe digitou - {cidade} - não é nome de santo!")

print('\n---Fim da execução---\n')
