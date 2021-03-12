# Desafio 55 Curso em Video Python

# By Rafabr

from time import sleep
from sys import exit
from estrutura_modelo import cabecalho, rodape

cabecalho(55, "Maior e Menor número da sequência.")

print("Digite o peso de várias pessoas separadas por espaço para compararmos!\n")

try:
    lista_pesos = list(map(int,input("Digite os pesos (em Kg) das pessoas: ").split()))
except ValueError:
    print("Voçe digitou algum valor errado ou indevido!")
    sleep(1)
    exit()

for peso in lista_pesos:
    if peso < 0:
        print("Voçe digitou algum peso negativo!")
        sleep(1)
        exit()

lista_pesos.sort()


print(f"\nForam verificados os pesos de {len(lista_pesos)} pessoas")
print(f"O maior peso é {lista_pesos[-1]}")
print(f"O menor peso é {lista_pesos[0]}")


rodape()
