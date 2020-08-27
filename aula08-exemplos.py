#Aula 8 do Curso Python em Video!

#Exercício da Aula 08!

#By Rafabr

'''Este exercicio testa o comando import para importar módulos com comandos
 não disponíveis em python. Foi testado a biblioteca math para importar.
 Foi testado também a importação somente da função específica através do comando from'''

from math import sqrt,floor,ceil
import math,random,emoji

print('************************************************************')
print('\nAula 08 - Exemplos e Testes')

num = int(input('Digite um número: '))

raiz = sqrt(num)

print(f'\nA Raiz de {num} é igual a {raiz:.10f} - Aproximado com 10 casas decimais!')
print(f'A Raiz de {num} é igual a {floor(raiz)} - Aproximado com para baixo!')
print(f'A Raiz de {num} é igual a {ceil(raiz)} - Aproximado com para cima!')
print(f'A Raiz de {num} é igual a {math.trunc(raiz)} - Truncado, sem casas decimais!')

print()
print('Teste de número aleatório usando a biblioteca ramdom: {}'.format(random.random()))
print('Teste de número aleatório entre 1 e 5: {}'.format(random.randint(1,5)))
print(emoji.emojize("teste emoji :cry:",use_aliases=True))

print('\nFim da execução\n')
print('************************************************************')


