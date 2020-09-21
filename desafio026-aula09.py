# Desafio 25 Curso em Video Python

# Este programa verifica se uma frase digitada tem a letra 'a' e mostras algumas informações.

#By Rafabr

import sys,time,subprocess

subprocess.run(['clear'])
print('\nDesafio 23')
print('Este programa verifica se uma frase digitada tem a letra \'a\' e mostras algumas informações.\n\n')

frase = input('Digite uma frase: ')
print()

frase = frase.lower()

tam_frase = len(frase)

a = 0

for k in range(tam_frase):
    if frase[k] == 'a':
        a = a + 1

if a > 0:
    print(f"A frase digitada possui {a} letras 'a'.")
    print(f"\nA letra 'a' apareçe pela primeira vez no índice {frase.find('a')} da frase")
    print(f"\nA letra 'a' apareçe pela primeira vez no índice {frase.rfind('a')} da frase")
else:
    print("A frase não possui nenhuma letra 'a'!")


print('\n---Fim da execução---\n')