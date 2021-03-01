# Desafio 13 Curso em Video Python

# Calcula um aumento de 15% no salário de uma pessoa

#By Rafabr

import sys,time

import os
os.system('clear')
print('\033[1;47;30m',end="")
print('\n'+'*'*80)
print('Desafio 13'.center(80))
print('Este programa calcula um aumento de 15% no salário de uma pessoa.'.center(80))
print(80*'*')
print('\033[m',end="")
print('\033[1;36m')

try:
    salario = float(input('Digite o valor de seu Salário atual: '))
    print()
except ValueError:
    print('\nNao foi digitado um valor válido\n')
    time.sleep(2)
    sys.exit()

print('Seu Salário atual é R$ {:.2f}'.format(salario))
print('Seu novo salário com aumento de 15% é de R$ {:.2f}'.format(salario*1.15))
print('Parabéns!')


print('\n---Fim da execução---\n')