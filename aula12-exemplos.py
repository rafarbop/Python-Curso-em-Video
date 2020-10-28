#Aula 12 do Curso Python em Video!

#By Rafabr

import time,sys
import os
from estrutura_modelo import cabecalho,rodape

cabecalho(12,"Esta Aula ira falar sobre Condições Aninhadas!")

escolha = input("Escolha qual opções deseja:\n 1 - Primeira opção\n 2 - Segunda opção\n 3 - Terceira opção\n\t:")

print(f'Voçe escolheu opção {escolha}\n\n')

nome = str(input("Qual é o seu nome: "))
if nome == 'Rafael':
    print('Que nome bonito!')
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print("Seu nome é bem popular no Brasil.")
elif nome in "Lya Paula Lyara":
    print('Que belo bome feminino.')
else:
    print("Seu nome é bem normal.")
print(f"Tenha um bom dia, {nome}")

rodape()



