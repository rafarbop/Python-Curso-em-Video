# Desafio 26 Curso em Video Python

# Este programa verifica se uma frase digitada tem a letra 'a' e mostras algumas informações.

#By Rafabr

import sys,time,subprocess

subprocess.run(['clear'])
print('\nDesafio 26')
print('Este programa verifica se uma frase digitada tem a letra \'a\' e mostras algumas informações.\n\n')

frase = str(input('Digite uma frase: ')).strip().lower()
print()
 
if frase.count('a'):
    print(f"A frase digitada possui {frase.count('a')} letras 'a'.")
    print(f"\nA letra 'a' apareçe pela primeira vez na posição {frase.find('a')+1} da frase")
    print(f"\nA letra 'a' apareçe pela primeira vez na posição {frase.rfind('a')+1} da frase")
else:
    print("A frase não possui nenhuma letra 'a'!")


print('\n---Fim da execução---\n')