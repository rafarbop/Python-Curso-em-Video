# Desafio 54 Curso em Video Python

# By Rafabr

from time import sleep
from datetime import date
from sys import exit
from estrutura_modelo import cabecalho, rodape

cabecalho(54, "Verificar maioridade de pessoas")

print("Este programa irá verificar quantas das pessoas informadas são maiores que 18 anos!\n")

try:
    lista_ano_nascimento = list(map(int,input("Digite os anos de nascimento das pessoas separadas por espaço: ").split()))
except ValueError:
    print("Voçe digitou algum valor errado ou indevido!")
    sleep(1)
    exit()

quantidade_maiores = 0
for k in lista_ano_nascimento:
    quantidade_maiores += 1 if (date.today().year - k >= 18) else 0

print(f"\nForam digitados anos de nascimento de {len(lista_ano_nascimento)} pessoas!")
print(f"{quantidade_maiores} pessoas são maiores de 18 anos!")


rodape()
