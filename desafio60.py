# Desafio 60 Curso em Video Python
# By Rafabr

from estrutura_modelo import cabecalho, rodape

cabecalho(60, "Fatorial de um Número!")

while True:
    try:
        numero = int(
            input("Digite um número inteiro: ")
            )
    except ValueError:
        print('Valor inválido inserido! Tente Novamente!')
        continue
    if numero < 0:
        print('O número não pode ser negativo! Tente Novamente')
        continue
    break

fatorial = 1
fator = numero

while (fator > 0):
    fatorial *= fator
    fator -= 1

print(f'O fatorial de {numero} é {fatorial}!')

rodape()
