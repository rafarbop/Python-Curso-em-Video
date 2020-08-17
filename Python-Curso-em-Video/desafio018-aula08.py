# Desafio 18 Curso em Video Python

# Calcula o valor do seno, cosseno e tangente de qualquer ângulo

#By Rafabr

import sys,time
import math as doido

print('\nDesafio 18')
print('Este programa calcula o valor do seno, cosseno e tangente de qualquer ângulo\n')

angulo_graus = float(input("Digite o valor do ângulo (EM GRAUS) que deseja calcular as relações trigonométricas básicas: "))
angulo_radianos = doido.radians(angulo_graus)

seno = doido.sin(angulo_radianos)
cosseno = doido.cos(angulo_radianos)
tangente = doido.tan(angulo_radianos)

print("Calculando ...")
time.sleep(2)
print("\nAs relações trigonométricas básicas do ângulo informado são as seguintes:")
print("-> sen({}) = {:.2f}".format(angulo_graus,seno))
print("-> cos({}) = {:.2f}".format(angulo_graus,cosseno))
print("-> tg({}) = {:.2f}".format(angulo_graus,tangente))

print('\n---Fim da execução---\n')