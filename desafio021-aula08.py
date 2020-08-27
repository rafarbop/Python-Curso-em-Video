# Desafio 21 Curso em Video Python

# Executa um arquivo de música MP3

#By Rafabr

import sys,time
import playsound
import pygame

print('\nDesafio 21')
print('Este programa executa um arquivo de música MP3.\n')

#playsound.playsound('a.mp3')

pygame.init()
pygame.mixer_music.load('a.mp3')
pygame.mixer_music.play()
time.sleep(10)
pygame.mixer_music.stop

print('\n---Fim da execução---\n')