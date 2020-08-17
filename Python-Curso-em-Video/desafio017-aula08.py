# Desafio 17 Curso em Video Python

# Calcula o valor da hipotenusa de um triângulo retângulo a partir dos catetos informados

#By Rafabr

import sys,time
import math as matematica

print('\nDesafio 17')
print('Este programa calcula o valor da hipotenusa de um triângulo retângulo a partir dos catetos informados\n')

cateto1 = float(input("Informe o valor de um dos catetos do triângulo retângulo: "))
cateto2 = float(input("Informe o valor do outro cateto: "))

hip = matematica.hypot(cateto1,cateto2)

print("\nO valor da hipotenusa é : {:.5f}".format(hip))

print('\n---Fim da execução---\n')