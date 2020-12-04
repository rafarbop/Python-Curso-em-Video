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

print('Seu IMC é',f'{imc:.2f}'.replace('.',','),'!\n')

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

peso_ideal_min = 18.5 * (altura**2)

peso_ideal_max = 25 * (altura**2)

print(f'\nPara um IMC ideal, seu peso deveria está entre: '+f'{peso_ideal_min:.2f}Kg → {peso_ideal_max:.2f}Kg'.replace('.',','))

print('\033[1;33;41m'+'''
A verificação de Obesidade pelo Índice IMC pode não ser       
eficaz, pois não considera a gordura corporal!                
Para uma melhor avaliação veja um Nutrólogo ou Nutricionista! 
'''+'\033[m')

rodape()
