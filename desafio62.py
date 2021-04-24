# Desafio 62 Curso em Video Python
# By Rafabr

from estrutura_modelo import cabecalho, rodape

cabecalho(62, "Termos de uma Progressão Aritmética - III")

while True:
    try:
        p0 = float(input('Digite o Termo inicial da PA: '))
        r = float(input('Digite a razão da PA: '))
    except ValueError:
        print('Voçe digitou um valor indevido!\n')
        continue
    break


n = 0
print()
while (n < 10):
    print(f'Termo {n+1}:'.ljust(14) + f'{p0 + n*r}')
    n += 1
print()


def maisTermos():
    '''Pergunta se deseja-se informar mais termos da PA'''
    while True:
        try:
            termos_adicionais = int(input('Digite quantos termos a mais deseja\
 visualizar?\n(Para sair digite 0)\n»»: '))
        except ValueError:
            print('Valor inválido!')
            continue
        if (termos_adicionais < 0):
            continue
        break
    return (termos_adicionais)


while True:
    n_termos = maisTermos()
    if (n_termos == 0):
        break
    total_termos = n_termos + n
    print()
    while (n < total_termos):
        print(f'Termo {n+1}:'.ljust(14) + f'{p0 + n*r}')
        n += 1
    print()


rodape()
