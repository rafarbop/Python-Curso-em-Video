# Desafio XX Curso em Video Python

# O QUE FAZ?

#By Rafabr

import time
import os


def cabecalho(aula,sobre:str):
    os.system('clear')
    print('\033[;1;44;37m',end="")
    print('\n'+'*'*100)
    print(f'Aula/Desafio {aula}'.center(100))
    print(sobre.center(100))
    print('*'*100+'\n')
    print('\033[m',end="")

def rodape():
    print('\n')
    print('\033[1;41;37m',end="")
    print(f'Fim de Aula'.center(100))
    print('*'*100+'\n')
    print('\033[m')
    

