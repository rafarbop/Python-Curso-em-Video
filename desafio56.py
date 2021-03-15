# Desafio 56 Curso em Video Python

# By Rafabr

from time import sleep
from sys import exit
from estrutura_modelo import cabecalho, rodape
from statistics import fmean

cabecalho(56, "Analisar dados - médio, maior, menor")

try:
    dicionario_pessoas = {}
    quantidade_pessoas = int(input("Informe quantas pessoas deseja cadastrar para serem analisadas: "))
    for _ in range(quantidade_pessoas):
        print('\nIniciando o cadastro de uma nova pessoa!')
        nome = input("Informe o nome da pessoa: ").strip()
        dicionario_pessoas[nome.split()[0]] = [nome]
        dicionario_pessoas[nome.split()[0]] += [int(input('Informe a idade da pessoa: '))]
        dicionario_pessoas[nome.split()[0]] += [input('Informe o sexo da pessoa:(M ou F) ')]
except ValueError:
    print("Voçe digitou algum valor errado ou indevido!")
    sleep(1)
    exit()

print()
idades = [dicionario_pessoas[item][1] for item in dicionario_pessoas]

dict_idade_crescente = sorted(dicionario_pessoas.items(), key=lambda x: x[1][1],reverse=True)

lista_homem_velho = []

for lista in dict_idade_crescente: 
    if lista[1][2] == 'M':
        lista_homem_velho.append(lista)
print()

mulheres_menor20 = []

for item in dicionario_pessoas:
    if dicionario_pessoas[item][2] == 'F' and dicionario_pessoas[item][1] < 20:
        mulheres_menor20.append(item)


print(f"A média de idade das pessoas informadas é {fmean(idades):.2f}")
print(f"O homem mais velho se chama {lista_homem_velho[0][0]}")
print(f"{len(mulheres_menor20)} mulheres possuem menos de 20 anos!")


rodape()
