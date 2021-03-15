# Desafio 48 Curso em Video Python

# By Rafabr


from time import sleep
from sys import exit
from os import system
from estrutura_modelo import cabecalho,rodape

cabecalho(48,"Soma dos Números Ímpares de um intervalo!")

try:
    numeroLimite = int(input("Digite um número positivo inteiro: "))
except ValueError:
    print("Valor inválido!")
    sleep(1)
    exit()

soma = 0
listaNumeros = []
for k in range(0,numeroLimite,3):
    if ((k%2)!= 0 ):
        soma += k
        listaNumeros.append(k)

print(f'\nOs números ímpares e múltiplos de três entre 1 e um {numeroLimite} são: \n{listaNumeros}')

print(f'\n\nA soma dos números acima é {soma}')

rodape()

