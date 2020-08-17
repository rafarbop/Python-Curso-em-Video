# Desafio 19 Curso em Video Python

# Sorteia um aluno entre quatro alunos informados

#By Rafabr

import sys,time
import random as ale

print('\nDesafio 19')
print('Este programa sorteia um aluno entre quatro alunos informados\n')

a1 = input("Digite o nome do primeiro aluno: ")
a2 = input("Digite o nome do segundo aluno: ")
a3 = input("Digite o nome do terceiro aluno: ")
a4 = input("Digite o nome do quarto aluno: ")

alunos = [a1,a2,a3,a4]

sorteio = ale.randint(0,3)

print("\nSorteando um dos alunos...")
time.sleep(2)


print("\nO aluno sorteado foi: {}".format(alunos[sorteio]))

print('\n---Fim da execução---\n')