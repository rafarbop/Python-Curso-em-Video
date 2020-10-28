# Desafio 36 Curso em Video Python

# By Rafabr

import os,time
from estrutura_modelo import cabecalho,rodape

cabecalho(36,"Verificar se uma pessoa pode fazer um financiamento de Imóvel")

print('\tSenhor Cliente,\n\tIremos coletar algumas informações para analisar sua solicitação de financiamento.\n')
valor_casa = float(input('Informe o valor do imóvel que deseja financiar: '))
qt_anos = int(input('Informe qual o prazo desejado do financiamento (em anos): '))
salario = float(input('Informe qual o seu salário: '))

print('\nCadastrando dados informados')
time.sleep(1)
cabecalho(36,"Verificar se uma pessoa pode fazer um financiamento de Imóvel")
print('Processando dados de sua análise')
time.sleep(0.5)
cabecalho(36,"Verificar se uma pessoa pode fazer um financiamento de Imóvel")
print('Processando dados de sua análise.')
time.sleep(0.8)
cabecalho(36,"Verificar se uma pessoa pode fazer um financiamento de Imóvel")
print('Processando dados de sua análise..')
time.sleep(1.1)
cabecalho(36,"Verificar se uma pessoa pode fazer um financiamento de Imóvel")
print('Processando dados de sua análise...')
time.sleep(1.5)
cabecalho(36,"Verificar se uma pessoa pode fazer um financiamento de Imóvel")

print('\nSeus dados foram processados pelo sistema e sua análise foi concluída.')

print(f'Valor do financiamento:'.ljust(25)+f'R$ {valor_casa:.2f}')
print(f'Prazo do financiamento:'.ljust(25)+f'R$ {qt_anos}')
print(f'Prestação mensal:'.ljust(25)+f'R$ {(valor_casa/qt_anos/12):.2f}\n')



rodape()