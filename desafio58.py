# Desafio 58 Curso em Video Python
# By Rafabr

from time import sleep
from os import system
from random import randint
from estrutura_modelo import cabecalho, rodape

cabecalho(58, "Jogo de Adivinha II")

print('O computador irá escolher um número de 0 a 10!')
print('Tente adivinhar qual!\n')

numero_da_sorte = randint(0, 10)

tentativas = 0

while True:
    try:
        numero_jogador = int(
            input("Digite um número maior/igual a 0 e menor/igual a 10: ")
            )
    except ValueError:
        print('\nVoçe digitou um valor inválido!')
        sleep(1)
        continue
    tentativas += 1
    print(f'Número de tentativas: {tentativas}')
    if numero_jogador == numero_da_sorte:
        system('clear')
        cabecalho(58, "Jogo de Adivinha II")
        print('\nParabens!')
        print(f'Voçe Acertou o Número Secreto - {numero_da_sorte}')
        print(f'Precisou de {tentativas} tentativas!\n')
        break
    else:
        print('Errou! Tente Novamente!\n')


rodape()
