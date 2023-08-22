import pygame
from time import sleep
print('\nDesafio 21 - Tocando um MP3.')
print('\nTocando sons de raios elétricos.')
pygame.init()
pygame.mixer.init()
sleep(1)
pygame.mixer.music.load('raio.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

