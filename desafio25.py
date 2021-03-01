# Desafio 25 Curso em Video Python

# Este programa verifica se uma pessoa tem 'silva' no nome.

# By Rafabr

import os

os.system('clear')
print('\nDesafio 25')
print('Este programa verifica se uma pessoa tem \'silva\' no nome.\n\n')

nome = input('Digite seu nome completo: ')
print()

nome = nome.lower()

lista_nome = nome.split()

if 'silva' in lista_nome:
    print("Parabéns!\nVoçe faz parte da família 'SILVA'!!!")
else:
    print("Voçe não tem o nome silva no seu nome!")


print('\n---Fim da execução---\n')
