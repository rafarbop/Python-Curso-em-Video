#Aula 06 do Curso Python em Video!

#Tipos Primitivos

#By Rafabr

''' '''

print('************************************************************')
print('\nTarefa 01 - Aula 06')
print('Este programa estuda os tipos primitivos de Python e utiliza')
print('alguns métodos da função print.\n')

#
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

print('\nFim da execução\n')
print('************************************************************')


