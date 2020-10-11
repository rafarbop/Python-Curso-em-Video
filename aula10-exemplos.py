#Aula 10 do Curso Python em Video!

#By Rafabr

import time,sys,subprocess

subprocess.run(['clear'])
print('\n'+'*'*80)
print('Aula 10 - Exemplos e Testes'.center(80)+'\n')

print('Questionário sobre carros:')
tem_carro = str(input('Voçe possui carro? (s/n) : ')).strip().lower()

if tem_carro == 's':
    pass
else:
    if tem_carro == 'n':
        print('Voçe não está apto a participar da pesquisa!')
        time.sleep(2)
        sys.exit()
    else:
        print('Voçe digitou uma informação inválida!')
        time.sleep(2)
        sys.exit()

carro = str(input('Informe a marca e modelo do seu carro (Ex. Ford Ká): '))
carro_tempo = int(input('Há quantos anos voçe comprou o carro? '))

ano_compra = int(time.strftime('%Y')) - carro_tempo

print(f"\nVoçe possui o seguinte carro: {carro}")
print(f'Seu Carro tem {carro_tempo} anos, logo voçe comprou ele em {ano_compra}')
if carro_tempo >= 5:
    print("Seu carro já tá meio velinho né!")
else:
    print('Seu carro ainda é novinho!')
print('Obrigado pelas informações!')


print('\nFim da execução\n')
print('\n'+'*'*80)
time.sleep(2)


