# Desafio 40 Curso em Video Python

# By Rafabr

import os,time,sys,statistics
from estrutura_modelo import cabecalho,rodape

cabecalho(40,"Verificar a média do aluno e sua situação escolar")

try:
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    print()
except ValueError:
    print('Voçe digitou um valor indevido!')
    time.sleep(0.5)
    sys.exit()

media = float(statistics.mean([n1,n2])) 
print(f'\tSua média escolar foi {media}')
if media < 5.0:
    print('\tVoçe não conseguiu as notas suficientes para passar de ano')
    print(f'\tSITUAÇÃO: \033[1;31mREPROVADO\033[m')
elif media > 6.9:
    print('\tPARABÉNS!\n\tVoçe conseguiu as notas suficientes para passar de ano')
    print(f'\tSITUAÇÃO: \033[1;36mAPROVADO\033[m')
else:
    print('\tVoçe não conseguiu as notas suficientes para passar de ano, porém ainda tem chances')
    print(f'\tSITUAÇÃO: \033[1;33mRECUPERAÇÃO\033[m')

rodape()