import pygame
import time
from game import *
from panel import *

win_size = [700,450]
level_tab = [50,30,25,10]
n_bomb = [8,20,50,200]
level = 0

window = pygame.display.set_mode(win_size)
window.fill([193, 198, 199])
panel = Panel()
game = Game(window,panel,grid=level_tab[2],n_bomb=n_bomb[2])
clock = pygame.time.Clock()
timer = 0
tick = 0

panel.plabel_2.text = f"Time : {timer}"
panel.plabel_2.apply(panel.surface)

def lose():
     global game
     global timer
     game.game_surface.fill([131, 135, 138])
     game = Game(window,panel,grid=level_tab[2],n_bomb=n_bomb[2])
     window.blit(game.game_surface , [250,0])
     timer = 0

panel.pbutton_1.function_target = lose

while game.run:

     if tick == 60:
          timer += 1
          panel.plabel_2.text = f"Time : {timer}"
          panel.plabel_2.apply(panel.surface)
          tick=0
     
     if game.lose:
          game.game_surface.fill([131, 135, 138])
          game = Game(window,panel,grid=level_tab[2],n_bomb=n_bomb[2])
          window.blit(game.game_surface , [250,0])
          level = 0
          timer = 0
     
     if game.finished:
          time.sleep(1)
          game.game_surface.fill([131, 135, 138])
          game = Game(window,panel,grid=level_tab[2],n_bomb=n_bomb[2])
          window.blit(game.game_surface , [250,0])
          timer = 0
     
     if panel.pbutton_1.is_overflight:
          panel.pbutton_1.overfly(panel.surface)
     else:
          panel.pbutton_1.apply(panel.surface)
     window.blit(game.game_surface , [250,0])
     window.blit(panel.surface , [0,0])
     game.game_event(window)
     pygame.display.flip()
     clock.tick(60)
     tick+=1


