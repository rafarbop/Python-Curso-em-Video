#Aula 8 do Curso Python em Video!

#Exercício da Aula 08!

#By Rafabr

'''Este exercicio testa o comando import para importar módulos com comandos
 não disponíveis em python. Foi testado a biblioteca math para importar.
 Foi testado também a importação somente da função específica através do comando from'''

from math import sqrt,floor

print('************************************************************')
print('\nAula 04 - Exemplos e Testes')

num = int(input('Digite um número: '))

raiz = sqrt(num)

print(f'A Raiz de {num} é igual a {raiz:.5f}')

print(f'O número arrendodado {raiz:.5f} elevado ao quadrado é: {(raiz*raiz):.5f}')


print('\nFim da execução\n')
print('************************************************************')


