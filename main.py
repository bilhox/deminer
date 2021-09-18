import pygame
import time
from game import *
from panel import *
from constants import *

win_size = [700,450]
n_bomb = [50,65,80,110]
await_user_reset = False
level = 0

#icon
icon = pygame.image.load("./imgs/logo bilhox.png")

window = pygame.display.set_mode(win_size)
pygame.display.set_caption("Deminor - V1.4.2 - By bilhox")
pygame.display.set_icon(icon)
window.fill([193, 198, 199])
panel = pygame.Surface([250,450])
panel.fill(GRAY_COLOR)
game = Game(window,panel,gs_size=gs_size[level],grid=25,n_bomb=n_bomb[level])
clock = pygame.time.Clock()
timer = 0
tick = 0

plabel_2.text = f"Time : {timer}"
plabel_2.apply(panel)
pbutton_1.apply(panel)
uplevel_button.apply(panel)
lowerlevel_button.apply(panel)

def levelup():
     global game
     global window
     global panel
     global level
     global timer

     timer = 0

     level += 1
     if level <= 3:
          pbutton_1.pos[1] = gs_size[level][1]-50
          lowerlevel_button.pos[1] = gs_size[level][1]-100
          uplevel_button.pos[1] = gs_size[level][1]-100
          window = pygame.display.set_mode([250+gs_size[level][0],gs_size[level][1]])
          panel = pygame.Surface([250,gs_size[level][1]])
          panel.fill(GRAY_COLOR)
          game = Game(window,panel,gs_size=gs_size[level],grid=25,n_bomb=n_bomb[level])
          window.blit(game.game_surface , [250,0])
     else:
          level = 0
          pbutton_1.pos[1] = gs_size[level][1]-50
          lowerlevel_button.pos[1] = gs_size[level][1]-100
          uplevel_button.pos[1] = gs_size[level][1]-100
          window = pygame.display.set_mode([250+gs_size[level][0],gs_size[level][1]])
          panel = pygame.Surface([250,gs_size[level][1]])
          panel.fill(GRAY_COLOR)
          game = Game(window,panel,gs_size=gs_size[level],grid=25,n_bomb=n_bomb[level])
          window.blit(game.game_surface , [250,0])

def lowerlevel():
     global game
     global window
     global panel
     global level
     global timer

     timer = 0

     level-=1
     if level >= 0:
          pbutton_1.pos[1] = gs_size[level][1]-50
          lowerlevel_button.pos[1] = gs_size[level][1]-100
          uplevel_button.pos[1] = gs_size[level][1]-100
          window = pygame.display.set_mode([250+gs_size[level][0],gs_size[level][1]])
          panel = pygame.Surface([250,gs_size[level][1]])
          panel.fill(GRAY_COLOR)
          game = Game(window,panel,gs_size=gs_size[level],grid=25,n_bomb=n_bomb[level])
          window.blit(game.game_surface , [250,0])
     else:
          level = 3
          pbutton_1.pos[1] = gs_size[level][1]-50
          lowerlevel_button.pos[1] = gs_size[level][1]-100
          uplevel_button.pos[1] = gs_size[level][1]-100
          window = pygame.display.set_mode([250+gs_size[level][0],gs_size[level][1]])
          panel = pygame.Surface([250,gs_size[level][1]])
          panel.fill(GRAY_COLOR)
          game = Game(window,panel,gs_size=gs_size[level],grid=25,n_bomb=n_bomb[level])
          window.blit(game.game_surface , [250,0])


def lose():
     global game
     global timer
     game.game_surface.fill([131, 135, 138])
     game = Game(window,panel,gs_size=gs_size[level],grid=25,n_bomb=n_bomb[level])
     window.blit(game.game_surface , [250,0])
     timer = 0
     

def flip():
     window.blit(game.game_surface , [250,0])
     window.blit(panel , [0,0])
     game.game_event(window)
     pygame.display.flip()

pbutton_1.function_target = lose
uplevel_button.function_target = levelup
lowerlevel_button.function_target = lowerlevel

while game.run:

     if tick == 60:
          timer += 1
          plabel_2.text = f"Time : {timer}"
          plabel_2.apply(panel)
          tick=0
     
     if game.lose:
          lose()
          timer = 0
     
     if game.finished and not game.await_user_action:
          
          game_finished_label.rect_size = gs_size[level]
          game_finished_label.apply(game.game_surface)
          timer = 0
          game.await_user_action = True
          flip()

     flip()
     clock.tick(60)
     tick+=1


