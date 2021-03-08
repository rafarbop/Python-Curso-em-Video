# Desafio 44 Curso em Video Python

# By Rafabr



import os,time,sys
from estrutura_modelo import cabecalho,rodape

cabecalho(44,"Valor de Produto com Diversas Meios de Pagamentos")

try:
    valor_normal = float(input("Informe o preço normal do produto(Em R$ - Ex.: 20,44) : ").replace(',','.'))
    meio_pag = int(input('''Informe qual o meio de pagamento:
    1 - À vista em Dinheiro ou PIX - Desconto de 10%
    2 - À vista no Cartão de Crédito ou Débito - Desconto de 5%
    3 - Cartão de Crédito em 2 parcelas - Sem Desconto
    4 - Cartão de Crédito em 3 ou mais parcelas - Juros de 20%
    : '''))
    print()

except ValueError:
    print('Voçe não digitou valores válidos!\nUse virgulas para casa decimais!')
    time.sleep(0.5)
    sys.exit()


if valor_normal<0:
    print('Voçe digitou valores negativos!')
    time.sleep(0.5)
    sys.exit()

if meio_pag not in [1,2,3,4]:
    print('Voçe digitou uma condição de pagamento inválida!')
    time.sleep(0.5)
    sys.exit()
if meio_pag == 1:
    print(f'Com o meio de pagamento informado voçe terá um Desconto de 10%\n\nO valor do Produto será R$ {(valor_normal*0.9):.2f}'.replace('.',','))
elif meio_pag == 2:
    print(f'Com o meio de pagamento informado voçe terá um Desconto de 5%\n\nO valor do Produto será R$ {(valor_normal*0.95):.2f}'.replace('.',','))
elif meio_pag == 3:
    print(f'Com o meio de pagamento informado voçe pagará o valor normal do Produto\n\nO valor do Produto será R$ {valor_normal:.2f}'.replace('.',','))
elif meio_pag == 4:
    print(f'Com o meio de pagamento informado voçe pagará Juros de 20%\n\nO valor do Produto será R$ {(valor_normal*1.2):.2f}'.replace('.',','))

rodape()
