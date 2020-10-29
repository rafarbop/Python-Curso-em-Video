# Desafio 41 Curso em Video Python

# By Rafabr

import os,time,sys
from estrutura_modelo import cabecalho,rodape

cabecalho(41,"Categorizar atletas de natação")

try:
    nasc = float(input('Digite o ano de nascimento do atleta: '))
    print()
except ValueError:
    print('Voçe digitou um valor indevido!')
    time.sleep(0.5)
    sys.exit()

idade = time.localtime().tm_year - nasc

if idade <= 9:
    print('O atleta faz parte da categoria \033[1;35mMIRIM\033[m')
elif idade <= 14:
    print('O atleta faz parte da categoria \033[1;35mINFANTIL\033[m')
elif idade <= 19:
    print('O atleta faz parte da categoria \033[1;35mJUNIOR\033[m')
elif idade <= 20:
    print('O atleta faz parte da categoria \033[1;35mSÊNIOR\033[m')
else:
    print('O atleta faz parte da categoria \033[1;35mMASTER\033[m')

rodape()