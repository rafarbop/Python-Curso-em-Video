# Desafio 39 Curso em Video Python

# By Rafabr

import os,time,sys
from estrutura_modelo import cabecalho,rodape

cabecalho(39,"Informação sobre alistamento militar")

try:
    ano_nasc = int(input('Digite o ano de seu nascimento: '))
    print()
except ValueError:
    print('Voçe digitou um valor indevido!')
    time.sleep(0.5)
    sys.exit()

idade = time.localtime().tm_year - ano_nasc
if idade < 18:
    print('\tVoçe não completou 18 anos, ainda vai se alistar no serviço militar')
    print(f'\tFaltam {18 - idade} anos para o alistamento')
elif idade == 18:
    print(f'\tVoçe tem {idade} anos!')
    print('\tDeverá se listar esse ano no serviço militar')
else:
    print('\tVoçe já passou do tempo de alistamento militar')
    print(f'\tO prazo para seu alistamento passou há {idade - 18} anos')

rodape()