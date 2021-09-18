import pygame
import random
import time
from constants import *
from panel import *

pygame.init()

class Game:

     def __init__(self,window,panel,gs_size=[450,450],grid=50,n_bomb=10):
          self.await_user_action = False
          self.panel = panel
          self.panel_width,self.panel_height = self.panel.get_width() , self.panel.get_height()
          self.gs_size = gs_size
          self.grid_scale = grid
          self.finished = False
          self.main_window = window
          self.game_surface = pygame.Surface(self.gs_size)
          self.game_surface.fill([131, 135, 138])
          window.blit(self.game_surface , [self.panel_width,0])
          self.run = True
          self.lose = False
          self.n_bomb = n_bomb
          self.bomb_demined = 0
          self.nfcp = self.n_bomb
          self.tab_grid = []
          self.pos_bomb = []
          self.detector = []

          for a in range(0,self.n_bomb):
               final_pos = False
               while not final_pos:
                    pos = [random.randint(0,self.gs_size[0]/self.grid_scale-1),random.randint(0,self.gs_size[1]/self.grid_scale-1)]
                    if(not pos in self.pos_bomb):
                         self.pos_bomb.append(pos)
                         final_pos = True


          for j in range(0,int(self.gs_size[0]/self.grid_scale)):
               for i in range(0,int(self.gs_size[1]/self.grid_scale)):
                    nada = False
                    for b in self.pos_bomb:
                         if b[0] == i and b[1] == j:
                              self.tab_grid.append([self.panel_width+i*self.grid_scale , j*self.grid_scale , "BOMB" , False , "NONE"])
                              nada = True
                              break
                    if not nada:
                         self.tab_grid.append([self.panel_width+i*self.grid_scale , j*self.grid_scale , "NONE", False , "NONE"])

          for i in self.tab_grid:
               number = 0
               already_listed = []
               for b in self.pos_bomb:
                    if (i[0]-self.grid_scale-self.panel_width<=b[0]*self.grid_scale<=i[0]+self.grid_scale-self.panel_width and b not in already_listed):
                         if(i[1]-self.grid_scale<=b[1]*self.grid_scale<=i[1]+self.grid_scale):
                              # print(self.tab_grid.index(i),b,"[",int(i[0]/self.grid_scale)-250/self.grid_scale,",",int(i[1]/self.grid_scale),"]")
                              already_listed.append(b)
                              number += 1
               self.detector.append([number,int(i[0]/self.grid_scale)-self.panel_width/self.grid_scale,int(i[1]/self.grid_scale)])
          
          for i in self.tab_grid:
               if self.detector[self.tab_grid.index(i)][0] == 0:
                    surface = pygame.Surface([self.grid_scale,self.grid_scale])
                    surface.fill(GRAY_COLOR_2)
                    self.game_surface.blit(surface , (i[0]-self.panel_width,i[1])) 
                    self.game_surface.blit(pygame.font.Font(None , 2*int(self.grid_scale/2)).render(f"{self.detector[self.tab_grid.index(i)][0]}",True,(0,0,0)) , [i[0]+int(self.grid_scale/4)-(self.panel_width-2) , i[1]+int(self.grid_scale/4)])
          
          # self.game_surface.fill(GRAY_COLOR_2)
          # for b in self.pos_bomb:
          #      surface = pygame.Surface([self.grid_scale,self.grid_scale])
          #      surface.fill(RED_COLOR)
          #      self.game_surface.blit(surface , (b[0]*self.grid_scale,b[1]*self.grid_scale))
          # window.blit(self.game_surface , [250,0])
          # pygame.display.flip()
     

     def game_event(self,screen):

          bomb_demined = 0
          for i in self.tab_grid:
               if(i[2] == "BOMB" and i[3] == True):
                    bomb_demined += 1
          
          self.bomb_demined = bomb_demined

          plabel_1.text = f"Flag remaining : {self.nfcp}"
          plabel_1.apply(self.panel)
          
          if(self.bomb_demined == self.n_bomb):
               self.finished = True

          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    self.run = False
               if event.type == pygame.MOUSEMOTION:
                    Pbutton.overfly(event.pos , self.panel , pbutton_1 , uplevel_button , lowerlevel_button)
                    
               if event.type == pygame.MOUSEBUTTONUP:

                    pos = event.pos

                    Pbutton.on_click(event.button,pbutton_1 , lowerlevel_button , uplevel_button)
                    # if pbutton_1.is_overflight and event.button == 1:
                    #      pbutton_1.clicked()

                    if not self.await_user_action: 

                         if pos[0] <= self.panel_width :
                              return
                         if event.button == 3:
                              
                              for i in self.tab_grid:
                                   if(i[0] < pos[0] < i[0]+self.grid_scale and i[1] < pos[1] < i[1]+self.grid_scale and not i[3] and self.nfcp != 0 and not i[4] == "VISIBLE"):
                                        surface = pygame.Surface([self.grid_scale,self.grid_scale])
                                        surface.fill(GREEN_COLOR)
                                        self.game_surface.blit(surface , (i[0]-self.panel_width,i[1]))
                                        self.game_surface.blit(pygame.font.Font(None , 2*int(self.grid_scale/2)).render(f"D",True,(0,0,0)) , [i[0]+int(self.grid_scale/4)-(self.panel_width-2) , i[1]+int(self.grid_scale/4)])
                                        i[3] = True
                                        self.nfcp -= 1
                                        i[4] = "FLAGED"  
                                        break
                                   elif(i[0] < pos[0] < i[0]+self.grid_scale and i[1] < pos[1] < i[1]+self.grid_scale and i[3] and not i[4] == "VISIBLE"):
                                        surface = pygame.Surface([self.grid_scale,self.grid_scale])
                                        surface.fill([131, 135, 138])
                                        self.game_surface.blit(surface , (i[0]-self.panel_width,i[1]))
                                        i[3] = False
                                        self.nfcp += 1
                                        i[4] = "NONE" 
                                        break

                         elif event.button == 1:
                              
                              for i in self.tab_grid:
                                   if(i[0] < pos[0] < i[0]+self.grid_scale and i[1] < pos[1] < i[1]+self.grid_scale and i[2] == "NONE"):
                                        if i[4] == "FLAGED":
                                             self.nfcp += 1
                                             i[4] = "VISIBLE"
                                        surface = pygame.Surface([self.grid_scale,self.grid_scale])
                                        surface.fill(GRAY_COLOR_2)
                                        self.game_surface.blit(surface , (i[0]-self.panel_width,i[1]))
                                        self.game_surface.blit(pygame.font.Font(None , 2*int(self.grid_scale/2)).render(f"{self.detector[self.tab_grid.index(i)][0]}",True,(0,0,0)) , [i[0]+int(self.grid_scale/4)-(self.panel_width-2), i[1]+int(self.grid_scale/4)])
                                        break

                                   elif(i[0] < pos[0] < i[0]+self.grid_scale and i[1] < pos[1] < i[1]+self.grid_scale and i[2] == "BOMB"):
                                        self.game_surface.fill(GRAY_COLOR_2)
                                        for b in self.pos_bomb:
                                             surface = pygame.Surface([self.grid_scale,self.grid_scale])
                                             surface.fill(RED_COLOR)
                                             self.game_surface.blit(surface , (b[0]*self.grid_scale,b[1]*self.grid_scale))
                                        screen.blit(self.game_surface , [self.panel_width,0])
                                        pygame.display.flip()
                                        time.sleep(5)
                                        self.lose = True
                                        break
