# Desafio 64 Curso em Video Python
# By Rafabr

from estrutura_modelo import cabecalho, rodape

cabecalho(64, "Soma de números informados - com while")

print('Digite abaixo os números que deseja incluir ou digite 999 para sair!')

numeros = []

while True:
    try:
        n = float(input('Digite um número: '))
    except ValueError:
        print('Voçe digitou um valor indevido!\n')
        continue
    if int(n) == 999:
        break
    else:
        numeros.append(n)


print(f'\nForam digitados {len(numeros)-1} números no total!')
print(f'A soma de todos os números é {sum(numeros):.2f}!')


rodape()
