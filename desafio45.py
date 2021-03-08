# Desafio 45 Curso em Video Python

# By Rafabr


import os,time,sys
import random
from estrutura_modelo import cabecalho,rodape

cabecalho(45,"Jogo do Jokenpô!")

try:
    player = int(input('''Bem vindo ao Jogo da Pedra, Papel e Tesoura!
    
    Para Jogar escolha umas das opções abaixo:
    1 - Pedra
    2 - Papel
    3 - Tesoura
    0 - Não Quero Jogar - Sair
    : '''))
    print()

except ValueError:
    print('Voçe não escolheu uma opção válida!\n')
    time.sleep(0.5)
    sys.exit()

if player not in [1,2,3,0]:
    print('Voçe não escolheu uma opção válida!')
    time.sleep(0.5)
    sys.exit()

choice_pc = random.choice(['PEDRA','PAPEL','TESOURA'])

if player == 0:
    print('Ta com medo de perder?!\n')
    time.sleep(1)
    print('Quando ganhar coragem volte para jogar!\n')
    sys.exit()

if player == 1:
    os.system('clear')
    cabecalho(45,"Jogo do Jokenpô!")
    print(f'Voçe escolheu PEDRA!')
    time.sleep(1)
    print(f'O computador escolheu {choice_pc}')
    if choice_pc == 'TESOURA':
        print('\n\tPARABÉNS, Pedra quebra Tesoura, Voçe Ganhou!')
    elif choice_pc == 'PAPEL':
        print('\n\tTente Novamente,Papel enrola Pedra, Voçe Perdeu!')
    else:
        print('\n\tDeu Empate!')
    

if player == 2:
    os.system('clear')
    cabecalho(45,"Jogo do Jokenpô!")
    print(f'Voçe escolheu PAPEL!')
    time.sleep(1)
    print(f'O computador escolheu {choice_pc}')
    if choice_pc == 'PEDRA':
        print('\n\tPARABÉNS, Papel enrola Pedra, Voçe Ganhou!')
    elif choice_pc == 'TESOURA':
        print('\n\tTente Novamente, Tesoura corta Papel, Voçe Perdeu!')
    else:
        print('\n\tDeu Empate!')

if player == 3:
    os.system('clear')
    cabecalho(45,"Jogo do Jokenpô!")
    print(f'Voçe escolheu TESOURA!')
    time.sleep(1)
    print(f'O computador escolheu {choice_pc}')
    if choice_pc == 'PAPEL':
        print('\n\tPARABÉNS, Tesoura corta Papel, Voçe Ganhou!')
    elif choice_pc == 'PEDRA':
        print('\n\tTente Novamente, Pedra quebra Tesoura, Voçe Perdeu!')
    else:
        print('\n\tDeu Empate!')


rodape()
