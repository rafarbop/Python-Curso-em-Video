# Desafio 7 Curso em Video Python

# Ler duas notas do aluno, calcula e mostra a média!

#By Rafabr

import sys,time

print('\nDesafio 7')
print('Este programa recebe duas notas e calcula a média delas!\n')

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