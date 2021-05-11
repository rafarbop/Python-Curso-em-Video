# Desafio 65 Curso em Video Python
# By Rafabr

from estrutura_modelo import cabecalho, rodape

cabecalho(65, "Média, Maior e Menor valor de numeros informados")


def maisNumeros():
    try:
        qtd_numeros_incluir = int(
            input('\nInforme quantos números deseja incluir: ')
            )
    except ValueError:
        print('Voçe digitou um valor indevido!')
    n = 0
    numeros = []
    while n < qtd_numeros_incluir:
        try:
            numeros.append(float(input('Digite um número: ')))
        except ValueError:
            print('Voçe digitou um número invalido!')
        n += 1
    return numeros


numeros = maisNumeros()

while True:
    continuar = input('\nDeseja adicionar mais números (s/n): ').lower()
    if continuar == 's':
        numeros += maisNumeros()
    elif continuar == 'n':
        break
    else:
        print('Digite uma opção válida!')

print(f'\nOs números digitados são:\n»» {numeros} ')
print(f'\nA média dos Números digitados é {sum(numeros)/len(numeros)}')
print(f'O maior número da lista é {max(numeros)}')
print(f'O menor número da lista é {min(numeros)}')


rodape()
