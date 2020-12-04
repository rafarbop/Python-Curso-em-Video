# Desafio 45 Curso em Video Python

# By Rafabr



import os,time,sys
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

if player == 0:
    print('Ta com medo de perder?!\n')
    time.sleep(1)
    print('Quando ganhar coragem volte para jogar!\n')
    sys.exit()

if player == 1:
    print('O computador escolheu ... Nada1')

if player == 2:
    print('O computador escolheu ... Nada2')

if player == 3:
    print('O computador escolheu ... Nada3')


rodape()
