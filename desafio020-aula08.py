# Desafio 19 Curso em Video Python

# Sorteia a ordem de apresentação de um trabalho de quatro alunos informados.

#By Rafabr

import sys,time
import random as ale

print('\nDesafio 19')
print('Este programa sorteia a ordem de apresentação de um trabalho de quatro alunos informados.\n')

a1 = input("Digite o nome do primeiro aluno: ")
a2 = input("Digite o nome do segundo aluno: ")
a3 = input("Digite o nome do terceiro aluno: ")
a4 = input("Digite o nome do quarto aluno: ")

alunos = [a1,a2,a3,a4]

ordem_alunos = ale.sample(alunos,4)

print("\nA ordem de apresenação será:")
print(f"1 - {ordem_alunos[0]}")
print(f"2 - {ordem_alunos[1]}")
print(f"3 - {ordem_alunos[2]}")
print(f"4 - {ordem_alunos[3]}")

print('\n---Fim da execução---\n')