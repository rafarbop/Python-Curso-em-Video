#Aula 9 do Curso Python em Video!

#Exercício da Aula 09!

#By Rafabr

''''''


print('************************************************************')
print('\nAula 04 - Exemplos e Testes')

frase = input("Digite uma Frase para testar alguns métodos utilizados com Strings: ")
print(f'\nA frase digitada possui {len(frase)} caracteres!\n')

print(f"O primeiro caractere (frase[0]) é: ".ljust(50)+f"'{frase[0]}'")
print(f"O quinto caractere (frase[4]) é: ".ljust(50)+f"'{frase[4]}'")
print(f"Os primeiros 10 caracteres (frase[:10]) são: ".ljust(50)+f"'{frase[:10]}'")
print("Caracteres 5º a 15º (frase[4:14]) são: ".ljust(50)+f"'{frase[4:14]}'")
print()
print(f"O último caractere (frase[-1]) é: ".ljust(50)+f"'{frase[-1]}'")
print(f"Os últimos 10 caracteres (frase[-10:]) são: ".ljust(50)+f"'{frase[-10:]}'")
print(f"10 caracteres iniciais pulando de 2 em 2 (frase[:10:2]) é: ".ljust(50)+f"'{frase[:10:2]}'")
print()
print(f"A quantidade de Espaços (frase.count(' ')) na frase digitada é: ".ljust(50)+f"'{frase.count(' ')}'")



frase.count(' ')

frase.strip()
frase.lstrip()
frase.rstrip()

frase.split()
' '.join(frase)



print('\nFim da execução\n')
print('************************************************************')


