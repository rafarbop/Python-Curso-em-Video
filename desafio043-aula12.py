# Desafio 43 Curso em Video Python

# By Rafabr

import os,time,sys
from estrutura_modelo import cabecalho,rodape

cabecalho(43,"Cálculo e Avaliação de IMC")

try:
    peso = float(input("Informe o seu peso(Em Kg - Ex.: 80) : ").replace(',','.'))
    altura = float(input('Informe sua altura(Em metros - Ex.: 1,73): ').replace(',','.'))
    print()

except ValueError:
    print('Voçe não digitou valores válidos!\nUse virgulas para casa decimais!')
    time.sleep(0.5)
    sys.exit()


if peso<0 or altura<0:
    print('Voçe digitou valores negativos!')
    time.sleep(0.5)
    sys.exit()

imc = peso/pow(altura,2)

print('Seu IMC é ',f'{imc:.2f}'.replace('.',','),'!\n')

if imc < 18.5:
    print('Voçe está ABAIXO do Peso!')
elif imc <= 25:
    print('Voçe está com Peso Normal ou Ideal!')
elif imc <= 30:
    print('Voçe está com SOBREPESO!')
elif imc <= 40:
    print('Voçe está com OBESIDADE!')
else:
    print('Voçe está com OBESIDADE MÓRBIDA!')


rodape()