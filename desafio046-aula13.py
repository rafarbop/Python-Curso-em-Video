# Desafio 46 Curso em Video Python

# By Rafabr


from time import sleep
from sys import exit
from os import system
from estrutura_modelo import cabecalho,rodape

from emoji import emojize as em

def fireworks():
    system('clear')
    cabecalho(46,"Contagem Regressiva!")
    print(em(':balloon::balloon::balloon:'))
    sleep(0.5)
    print(em(':sparkles::sparkles::sparkles::sparkles:'))
    sleep(0.5)
    print(em(':fireworks::fireworks::fireworks::fireworks::fireworks:'))
    sleep(0.5)
    print(em(':eight-pointed_star: :eight-pointed_star: :eight-pointed_star: :eight-pointed_star: :eight-pointed_star: :eight-pointed_star:'))
    sleep(0.5)
    print(em(':fireworks::fireworks::fireworks::fireworks::fireworks:'))
    sleep(0.5)
    print(em(':sparkles::sparkles::sparkles::sparkles:'))
    sleep(0.5)
    print(em(':balloon::balloon::balloon:'))
    sleep(1)
    print('FELIZ ANO NOVO!!!')
    sleep(2)

def contagem(num:int):
    cabecalho(46,"Contagem Regressiva!")
    print(em(':partying_face::partying_face: Festa de Fim de Ano :party_popper::party_popper:\n\n'))
    for k in range(10,0,-1):
        if (k == 10):
            print(em(f' -{k} - '.center(30,em(':raising_hands:'))))
        else:
            print(em(f' - {k} - '.center(30,em(':raising_hands:'))))
        sleep(1)

cabecalho(46,"Contagem Regressiva!")

print('Vamos a contagem regressiva?!')

sleep(2)
system('clear')

contagem(10)

fireworks()

rodape()

