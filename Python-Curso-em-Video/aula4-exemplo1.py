#Aula 04 do Curso Python em Video!

#Exercício de Desafio da Aula 04!

#By Rafabr

'''Este programa pergunta o nome da pessoa e retorna uma saudação, após isso
solicita o dia o mês e o ano do usuário e retorna a data completade nascimento
de forma configurada'''

print('************************************************************')
print('\nAula 04 - Exemplos')
print('Este programa pergunta alguns dados seus e retorna os dados\npara confirmação')

#pergunta o nome do usuário e retorna uma saudação
nome = input('\nQual é o seu nome?\n')
print('\tOlá {}!\n\tSeja bem vindo ao python!'.format(nome))
print('\nATENÇÃO: Aprenda com Sabedoria!\n')

#pergunta os dados de nascimento e retorna o nascimento completo
dia = input('Qual dia voçe nasceu?\n')
mes = input('Qual mês voçe nasceu?\n')
ano = input('E o ano, qual foi?\n')
print('\n\t\tObrigado pelas informações!')

print('\nData de nascimento de',nome,':',dia,'de',mes,'de',ano)
print('\nFim da execução\n')

print('************************************************************')


