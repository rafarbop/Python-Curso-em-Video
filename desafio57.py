# Desafio 57 Curso em Video Python
# By Rafabr

from estrutura_modelo import cabecalho, rodape

cabecalho(57, "Solicitar entrada enquanto valor padrão não for digitado")

sexo_opcoes = ['M', 'F']

while True:
    sexo = input('Informo que é o seu sexo (M ou F): ').strip().upper()
    if sexo in sexo_opcoes:
        break


print(f'\nFoi informado o sexo {sexo}')


rodape()
