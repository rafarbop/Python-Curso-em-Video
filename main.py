import os,re

nome = os.listdir()

nome2 = []
for k in nome:
  if re.findall(".py$", k):
    nome2.append(k)

nome3 = []

for k in nome2:
  if re.findall("^desafio", k):
    nome3.append(k)


for k in nome3:
  print(k)