# Desafio 59 Curso em Video Python
# By Rafabr

from time import sleep
from os import system
from estrutura_modelo import cabecalho, rodape

cabecalho(59, "Menu de Operações Aritméticas")

print('Este programa calcula uma operação matemática com os números \
informados.'.center(100).upper(), end='\n\n')

while True:
    try:
        numeros = list(
            map(
                float, input(
                    "Digite os números separados por espaço: \n »"
                    ).split()
                )
            )
    except ValueError:
        print('Valor(es) inválidos inseridos! Tente Novamente!')
        continue
    break

while True:
    while True:
        try:
            menu = int(input('''
            [1] Somar
            [2] Multiplicar
            [3] Maior
            [4] Novos Números
            [5] Sair do Programa
            '''))
        except ValueError:
            print('Opção do menu inválida, tente novamente!')
            sleep(2)
            system('clear')
            cabecalho(59, "Menu de Operações Aritméticas")
            print(f'{numeros=}')
            continue
        break
    if menu == 1:
        system('clear')
        cabecalho(59, "Menu de Operações Aritméticas")
        print(f'{numeros=}')
        print(f'\nA soma dos números é:\n» {sum(numeros):.2f}')
    elif menu == 2:
        system('clear')
        cabecalho(59, "Menu de Operações Aritméticas")
        print(f'{numeros=}')
        multiplicacao = 1
        for n in numeros:
            multiplicacao *= n
        print(f'\nA multiplicação dos números é:\n» {multiplicacao:.2f}')
    elif menu == 3:
        system('clear')
        cabecalho(59, "Menu de Operações Aritméticas")
        print(f'{numeros=}')
        print(f'\nO maior número é:\n» {max(numeros)}')
    elif menu == 4:
        system('clear')
        cabecalho(59, "Menu de Operações Aritméticas")
        print(f'Números Antigos: {numeros}')
        while True:
            try:
                numeros = list(
                    map(
                        float, input(
                            "Digite os novos números separados por espaço:\n »"
                            ).split()
                        )
                    )
            except ValueError:
                print('Valor(es) inválidos inseridos! Tente Novamente!')
                continue
            break
        print(f'\nNovos Números: {numeros}')
    elif menu == 5:
        print('Saindo do Programa...')
        sleep(1)
        break
    else:
        print('Menu inválido! Tente Novamente!')


rodape()
