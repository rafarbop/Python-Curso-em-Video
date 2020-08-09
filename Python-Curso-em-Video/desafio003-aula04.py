# Desafio 3 Curso em Video Python

# Fazer a soma e diferença de valores informados pelo usuário, convertendo a entrada para números!

#By Rafabr

'''O detalhe do exercício e saber como converter caractere de entrada
em uma variável do tipo float para poder realizar a soma dos números'''


print('\nDesafio 3')
print(80*'*')
print('Este programa calcula a soma ou a diferença de 2 números informados!')

#solicita dois números do usuário
x=float(input('\nDigite um número qualquer:\n\t'))
y=float(input('\nDigite outro número:\n\t'))

'''realiza a soma e a diferença dos números informados convertendo
os caracteres informados para números'''
soma=x+y
dif=x-y

#Imprime como saida a soma e a diferença dos números informados
print('\n\t+ A soma dos dois números é: {} + {} = {}'.format(x,y,soma))
print('\t- A diferença entre eles é: {} - {} = {}'.format(x,y,dif))

print('\n---Fim da execução---\n')
print(80*'*')
