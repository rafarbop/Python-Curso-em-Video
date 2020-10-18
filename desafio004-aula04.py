# Desafio 4 Curso em Video Python

# Usa uma função que retorna o tipo primitivo e utiliza alguns métodos utilizados com strings!

# By Rafabr


import os
os.system('clear')
print('\033[1;47;30m',end="")
print('\n'+'*'*80)
print('Desafio 4'.center(80))
print('Este programa estuda os tipos primitivos de Python e utiliza'.center(80))
print('alguns métodos utilizados com strings!'.center(80))
print(80*'*')
print('\033[m',end="")
print('\033[1;36m')


n1=input('Digite número: ')
print('\nEsse programa importou o valor como o seguinte tipo primitivo:\n',type(n1))

n=input('\nDigite algo:')
print('\nVoçe digitou algum número?')
print(n.isnumeric())
print('Voçe difitou alguma palavra?')
print(n.isalpha())
print('Voçe digitou uma palavra maiúscula?')
print(n.isupper())
print('Voçe digitou uma palavra minúscula?')
print(n.islower())
print('Voçe digitou uma palavra alfanumérica?')
print(n.isalnum())
print('Voçe digitou um espaço?')
print(n.isspace())

print('\n---Fim da execução---\n')
print(80*'*')


