#Aula 9 do Curso Python em Video!

#Exercício da Aula 09!

#By Rafabr

''''''

print('\n'+'*'*80)
print('Aula 09 - Exemplos e Testes'.center(80)+'\n')

frase = input("Digite uma Frase para testar alguns métodos utilizados com Strings: ")
print(f'\nA frase digitada possui {len(frase)} caracteres!\n')
print('\t',end = "")
for k in range(len(frase)):
    print(frase[k].center(4),end = "")
print('\n\t',end = "")
for k in range(len(frase)):
    print(str(k).center(4),end = "")
print("\n")

print(f"O primeiro caractere (frase[0]) é: ".ljust(50)+f"'{frase[0]}'")
print(f"O quinto caractere (frase[4]) é: ".ljust(50)+f"'{frase[4]}'")
print(f"Os primeiros 10 caracteres (frase[:10]) são: ".ljust(50)+f"'{frase[:10]}'")
print("Caracteres 5º a 15º (frase[4:14]) são: ".ljust(50)+f"'{frase[4:14]}'")
print()
print(f"O último caractere (frase[-1]) é: ".ljust(60)+f"'{frase[-1]}'")
print(f"Os últimos 10 caracteres (frase[-10:]) são: ".ljust(60)+f"'{frase[-10:]}'")
print(f"10 caracteres iniciais pulando de 2 em 2 (frase[:10:2]) é: ".ljust(60)+f"'{frase[:10:2]}'")
print()
print(f"A quantidade de Espaços (frase.count(' ')) na frase digitada é: ".ljust(110)+f"'{frase.count(' ')}'")
print(f"Podemos procurar uma string(Ex.:frase.find('no')) na frase digitada (Retorna índice): ".ljust(110)+f"'{frase.find('no')}'")
print(f"Podemos verificar se existe uma string na frase digitada ('no' in frase): ".ljust(110)+f"'{'no' in frase}'")
print()
print(f"Podemos substituir parte de uma string(frase.replace('a','y')) na frase digitada: ".ljust(85)+f"'{frase.replace('a','y')}'")
print()
print(f"A primeira palavra (frase.split[0]) da frase digitada é: ".ljust(85)+f"'{frase.split()[0]}'")
print(f"A última palavra (frase.split[-1]) da frase digitada é: ".ljust(85)+f"'{frase.split()[-1]}'")
join_teste = " ".join([frase.split()[0],frase.split()[-1]])
print(f"Juntando as duas palavras(" ".join(['frase.split[0]','frase.split[-1]'])) teremos: ".ljust(85)+"'"+" ".join([frase.split()[0],frase.split()[-1]])+"'")

print('\nFim da execução\n')
print('************************************************************')


