# Desafio 56 Curso em Video Python

# By Rafabr

from time import sleep
from sys import exit
from estrutura_modelo import cabecalho, rodape

cabecalho(56, "Analisar dados - médio, maior, menor")

try:
    dicionario_pessoas = {}
    quantidade_pessoas = int(input("Informe quantas pessoas deseja cadastrar para serem analisadas: "))
    for _ in range(quantidade_pessoas):
        print('\nIniciando o cadastro de uma nova pessoa!')
        nome = input("Informe o nome da pessoa: ").strip()
        dicionario_pessoas[nome.split()[0]] = [nome]
        dicionario_pessoas[nome.split()[0]] += [input('Informe a idade da pessoa: ')]
        dicionario_pessoas[nome.split()[0]] += [input('Informe o sexo da pessoa:(M ou F) ')]
except ValueError:
    print("Voçe digitou algum valor errado ou indevido!")
    sleep(1)
    exit()



print(dicionario_pessoas)


print(f"A média de idade das pessoas informadas é {0}")
print(f"O homem mais velho se chama {'???'}")
print(f"{0} mulheres possuem menos de 20 anos!")


rodape()
