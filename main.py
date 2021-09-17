import pygame
import time
from game import *
from panel import *
from constants import *

win_size = [700,450]
level_tab = [50,30,25,10]
n_bomb = [8,20,50,200]
texts =["You demined all the bombs !","thanks for played !"]
await_user_reset = False
level = 0

window = pygame.display.set_mode(win_size)
window.fill([193, 198, 199])
panel = pygame.Surface([250,450])
panel.fill(GRAY_COLOR)
game_finished_label = Plabel(texts[0],FONT_1,font_color=[200,200,200],rect_color=[11, 11, 11, 96],rect_size=[450,450])
game = Game(window,panel,grid=level_tab[2],n_bomb=n_bomb[2])
clock = pygame.time.Clock()
timer = 0
tick = 0

plabel_2.text = f"Time : {timer}"
plabel_2.apply(panel)

def lose():
     global game
     global timer
     game.game_surface.fill([131, 135, 138])
     game = Game(window,panel,grid=level_tab[2],n_bomb=n_bomb[2])
     window.blit(game.game_surface , [250,0])
     timer = 0

def flip():
     window.blit(game.game_surface , [250,0])
     window.blit(panel , [0,0])
     game.game_event(window)
     pygame.display.flip()

pbutton_1.function_target = lose

while game.run:

     if tick == 60:
          timer += 1
          plabel_2.text = f"Time : {timer}"
          plabel_2.apply(panel)
          tick=0
     
     if game.lose:
          game.await_user_action = False
          game.finished = False
          game.game_surface.fill([131, 135, 138])
          game = Game(window,panel,grid=level_tab[2],n_bomb=n_bomb[2])
          window.blit(game.game_surface , [250,0])
          level = 0
          timer = 0
     
     if game.finished and not game.await_user_action:
          
          game_finished_label.apply(game.game_surface)
          timer = 0
          game.await_user_action = True
          flip()
          # game.game_surface.fill([131, 135, 138])
          # game = Game(window,panel,grid=level_tab[2],n_bomb=n_bomb[2])
          # window.blit(game.game_surface , [250,0])
     
     if pbutton_1.is_overflight:
          pbutton_1.overfly(panel)
     else:
          pbutton_1.apply(panel)
     flip()
     clock.tick(60)
     tick+=1


