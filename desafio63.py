# Desafio 63 Curso em Video Python
# By Rafabr

from estrutura_modelo import cabecalho, rodape

cabecalho(63, "Sequência de Fibonacci")

while True:
    try:
        print('Esse programa mostra alguns termos da Sequência de Finobacci!')
        termos = float(input('Digite o número de Termos que deseja ver: '))
    except ValueError:
        print('Voçe digitou um valor indevido!\n')
        continue
    break


n = 0
n_1 = 1
n_2 = 0
n_0 = 0
print('\n0 » 1', end="")
while (n < termos):
    n_0 = n_2 + n_1
    print(f' » {n_0}', end="")
    n_2 = n_1
    n_1 = n_0
    n += 1
print()


rodape()
