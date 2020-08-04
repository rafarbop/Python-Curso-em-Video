#Aula 04 do Curso Python em Video!

#Exercício de Desafio da Aula 04!

#By Rafabr

'''Este programa solicita 2 números do usuário e retorna a soma desse números!
O detalhe do exercício e saber como converter caractere de entrada
em uma variável do tipo inteiro para poder realizar a soma dos números'''


print('\nDesafio Aula 04')
print('************************************************************')
print('Este programa calcula a soma de 2 números informados!')

#solicita dois números do usuário
x=int(input('\nDigite um número qualquer:\n\t'))
y=int(input('\nDigite outro número:\n\t'))

'''realiza a soma e a diferença dos números informados convertendo
os caracteres informados para números'''
soma=x+y
dif=x-y

#Imprime como saida a soma e a diferença dos números informados
print('\n\t\t+ A soma dos dois números é: {} + {} = {}'.format(x,y,soma))
print('\t\t- A diferença entre eles é: {} - {} = {}'.format(x,y,dif))
print('\nFim da Execução!\n')

print('************************************************************')
