import pygame
import time
from game import *

win_size = [700,450]
level_tab = [50,30,25,10]
n_bomb = [8,20,50,200]
level = 0

window = pygame.display.set_mode(win_size)
window.fill([193, 198, 199])
game = Game(window,grid=level_tab[2],n_bomb=n_bomb[2])

while game.run:
     if game.lose:
          game.game_surface.fill([131, 135, 138])
          game = Game(window,grid=level_tab[2],n_bomb=n_bomb[2])
          window.blit(game.game_surface , [250,0])
          level = 0
     
     if game.finished:
          time.sleep(1)
          game.game_surface.fill([131, 135, 138])
          game = Game(window,grid=level_tab[2],n_bomb=n_bomb[2])
          window.blit(game.game_surface , [250,0])

     window.blit(game.game_surface , [250,0])
     game.game_event(window)
     pygame.display.flip()


