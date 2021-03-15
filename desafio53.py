# Desafio 53 Curso em Video Python

# By Rafabr

from estrutura_modelo import cabecalho, rodape

cabecalho(53, "Verificador de Palíndromo")

text = str(input('Digite a frase a ser análisada: ')).strip().upper()

text_in_list = []

for k in text.replace(' ', ''):
    text_in_list.append(k)

text_reversed = text_in_list.copy()
text_reversed.reverse()
print('\nFrase Informada: ', ''.join(text_in_list))

print('Frase Inversa  : ', ''.join(text_reversed))

if (text_in_list == text_reversed):
    print(f"A frase informada é um palíndromo!")
else:
    print(f'A frase informada NÃO é um palíndromo.')

rodape()
