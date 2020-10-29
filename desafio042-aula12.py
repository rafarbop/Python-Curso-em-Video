# Desafio 42 Curso em Video Python

# By Rafabr

import os,time,sys
from estrutura_modelo import cabecalho,rodape

cabecalho(42,"Classificação de Triângulos 2")

try:
    retas = str(input("Informe 3 medidas de reta separadas por virgula ','(Ex.: 4,5,6): ")).strip().split(',')
    r = [float(retas[0]),float(retas[1]),float(retas[2])]
    print()

except ValueError:
    print('Voçe não digitou valores válidos!')
    time.sleep(0.5)
    sys.exit()

except IndexError:
    print('Voçe não digitou 3 valores!')
    time.sleep(0.5)
    sys.exit()

if len(r)>3:
    print('Voçe digitou mais que 3 valores!')
    time.sleep(0.5)
    sys.exit()

if r[0]<0 or r[1]<0 or r[2]<0:
    print('Voçe digitou valores negativos!')
    time.sleep(0.5)
    sys.exit()

if r[0] < r[1] + r[2] and r[1] < r[0] + r[2] and r[2] < r[1] + r[0]:
    print(f'As medidas informadas {r}, formam um triângulo!')
    if r[0] == r[1] == r[2]:
        print('O triângulo formado é um triângulo Equilátero!')
    elif r[0] == r[1] or r[0] == r[2] or r[1] == r[2]:
        print('O triângulo formado é um triângulo Isósceles!')
    else:
        print('O triângulo formado é um triângulo Escaleno!!')
else:
    print('As medidas informadas NÃO formam um triângulo!')

rodape()