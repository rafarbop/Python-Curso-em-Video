# Desafio 11 Curso em Video Python

# Calcula a área de uma parede a apartir da largura e altura informadas, e quantos litros de tinta são necessários para pintá-la.

#By Rafabr

import sys,time

print('\nDesafio 11')
print('Este programa calcula a área de uma parede a partir da largura e altura informadas,\ne mostra quantos litros de tinta são necessários para pintá-la.\n')

try:
    width = float(input('Informe a largura da parede em metros: '))
    height = float(input('Informe a altura da parede em metros: '))
    print()
except ValueError:
    print('\nNao foi digitado um valor numérico!\n')
    time.sleep(2)
    sys.exit()

area = width*height
print('Uma parede de {:.2f} metros de largura e {:.2f} metros de altura, possui uma área de {:.2f} metros quadrados.\n'.format(width,height,area))

total_litros = area / 2
print('Considerando que um litro de tinta é suficiente para pintar 2 metros quadrados de área:')
print('Serão necessários {:.2f} litros de tinta para a pintura dessa parede.'.format(total_litros))

print('\n---Fim da execução---\n')