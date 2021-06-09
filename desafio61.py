# Desafio 61 Curso em Video Python
# By Rafabr

from estrutura_modelo import cabecalho, rodape

cabecalho(61, "Termos de uma Progressão Aritmética - II")

while True:
    try:
        p0 = float(input('Digite o Termo inicial da PA: '))
        r = float(input('Digite a razão da PA: '))
    except ValueError:
        print('Voçe digitou um valor indevido!\n')
        continue
    break

n = 1

print()

while (n <= 10):
    print(f'Termo {n}:'.ljust(10) + f'{p0 + (n-1)*r}')
    n += 1


rodape()
