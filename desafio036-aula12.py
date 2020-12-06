# Desafio 36 Curso em Video Python

# By Rafabr

import os,time
from estrutura_modelo import cabecalho,rodape

cabecalho(36,"Análise de um financiamento de Imóvel")

print('\tPrezado Cliente,\n\tIremos coletar algumas informações para analisar sua solicitação de financiamento.\n')
valor_casa = float(input('Informe o valor do imóvel que deseja financiar: '))
prazo_finan = int(input('Informe qual o prazo desejado do financiamento (em anos): '))
salario = float(input('Informe qual o seu salário: '))
prestacao_mensal = valor_casa/(prazo_finan*12)
limite_prest = salario*0.3


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
print(f'Prazo do financiamento:'.ljust(25)+f'{prazo_finan} Anos')
print(f'Prestação mensal:'.ljust(25)+f'R$ {prestacao_mensal:.2f}\n')

if prestacao_mensal <= limite_prest:
    print('\n\tParabens!\n\tSeu financiamento foi aprovado!')
    print('\tEntraremos em contato para prosseguirmos com o financiamento.\n\tObrigado por usar nossos serviços.')
else:
    print('\n\tSeu financiamento não foi aprovado!\n\tTente novamente quando tiver um aumento salarial ou procure uma casa de menor valor.')
    print(f'\nPrestação mensal máxima para o seu salário: R$ {limite_prest:.2f}')

rodape()