# Desafio 53 Curso em Video Python

# By Rafabr

from time import sleep
from sys import exit
from os import system
from estrutura_modelo import cabecalho, rodape

cabecalho(53, "Verificador de Palíndromo")

frase = input('Digite a frase a ser análisada: ').strip

for k in range(0, len(frase)):
    print(f'{frase[k]}-{frase[-k+1]}')

rodape()
