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


n = 3

n1 = 0
n2 = 1
n_atual = 0

print('\n0 » 1', end="")
while (n <= termos):
    n_atual = n1 + n2
    print(f' » {n_atual}', end="")
    n1, n2 = n2, n_atual
    n += 1
print()


rodape()
