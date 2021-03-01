# Desafio 21 Curso em Video Python

# Executa um arquivo de música MP3

# By Rafabr

import time
import playsound
try:
    import replit
except ImportError:
    import pygame

print('\nDesafio 21')
print('Este programa executa um arquivo de música MP3.\n')

# playsound.playsound('a.mp3')

try:
    source = replit.audio.play_file('a.mp3')
    time.sleep(10)
except NameError:
    playsound.playsound('a.mp3')
    time.sleep(10)

print('\n---Fim da execução---\n')
