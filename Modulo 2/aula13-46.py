from time import sleep
import pygame
pygame.mixer.init()
pygame.init()
print('\nDesafio 46 - Contagem Regressiva!\n')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
    if c == 1:
        print('\n\n', '._.' * 20, 'FIM!!', '._.' * 100)
        pygame.mixer.music.load('fogos.mp3')
        pygame.mixer.music.play()
        while(pygame.mixer.music.get_busy()): pass

        #pygame.event.wait()
