# Desafio 57 Curso em Video Python
# By Rafabr

from estrutura_modelo import cabecalho, rodape

cabecalho(57, "Solicitar entrada enquanto valor padrão não for digitado")


while True:
    sexo = input('Informe qual é o seu sexo (M ou F): ').strip().upper()
    if sexo in 'MmFf':
        break
    print('Dado Inválido!')


print(f'\nFoi informado o sexo {sexo}')


rodape()
