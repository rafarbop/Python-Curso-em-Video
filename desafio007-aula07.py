# Desafio 7 Curso em Video Python

# Ler duas notas do aluno, calcula e mostra a média!

#By Rafabr

import sys,time

import os
os.system('clear')
print('\033[1;47;30m',end="")
print('\n'+'*'*80)
print('Desafio 7'.center(80))
print('Este programa recebe duas notas e calcula a média delas!'.center(80))
print(80*'*')
print('\033[m',end="")
print('\033[1;36m')


try:
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    print()
except ValueError:
    print('\nNao foi digitado um valor válido.\n')
    time.sleep(2)
    sys.exit()

media_notas = (nota1 + nota2) / 2

print(f'A média das notas {nota1} e {nota2} é: {media_notas}')

print('\n---Fim da execução---\n')