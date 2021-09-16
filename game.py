import pygame
import random
import time

pygame.init()

RED_COLOR = (222, 57, 35)
GRAY_COLOR_1 = [100, 103, 107]
GREEN_COLOR = [113, 230, 78]

class Game:

     def __init__(self,window,grid=50,n_bomb=10):
          self.gs_size = [450,450]
          self.grid_scale = grid
          self.finished = False
          self.game_surface = pygame.Surface(self.gs_size)
          self.game_surface.fill([131, 135, 138])
          window.blit(self.game_surface , [250,0])
          self.run = True
          self.lose = False
          self.n_bomb = n_bomb
          self.tab_grid = []
          self.pos_bomb = []
          self.detector = []

          for a in range(0,self.n_bomb):
               final_pos = False
               while not final_pos:
                    pos = [random.randint(0,450/self.grid_scale-1),random.randint(0,450/self.grid_scale-1)]
                    if(not pos in self.pos_bomb):
                         self.pos_bomb.append(pos)
                         final_pos = True

          for j in range(0,int(450/self.grid_scale)):
               for i in range(0,int(450/self.grid_scale)):
                    nada = False
                    for b in self.pos_bomb:
                         if b[0] == i and b[1] == j:
                              self.tab_grid.append([250+i*self.grid_scale , j*self.grid_scale , "BOMB" , False])
                              nada = True
                              break
                    if not nada:
                         self.tab_grid.append([250+i*self.grid_scale , j*self.grid_scale , "NONE", False])
          
          for i in self.tab_grid:
               number = 0
               already_listed = []
               for b in self.pos_bomb:
                    if (i[0]-self.grid_scale-250<=b[0]*self.grid_scale<=i[0]+self.grid_scale-250 and b not in already_listed):
                         if(i[1]-self.grid_scale<=b[1]*self.grid_scale<=i[1]+self.grid_scale):
                              # print(self.tab_grid.index(i),b,"[",int(i[0]/self.grid_scale)-250/self.grid_scale,",",int(i[1]/self.grid_scale),"]")
                              already_listed.append(b)
                              number += 1
               self.detector.append([number,int(i[0]/self.grid_scale)-250/self.grid_scale,int(i[1]/self.grid_scale)])
          
          self.game_surface.fill(GRAY_COLOR_1)
          for b in self.pos_bomb:
               surface = pygame.Surface([self.grid_scale,self.grid_scale])
               surface.fill(RED_COLOR)
               self.game_surface.blit(surface , (b[0]*self.grid_scale,b[1]*self.grid_scale))
          window.blit(self.game_surface , [250,0])
          pygame.display.flip()
          # # time.sleep(5)
     

     def game_event(self,screen):
          n_bomb_demined = 0
          for i in self.tab_grid:
               if self.detector[self.tab_grid.index(i)][0] == 0:
                    surface = pygame.Surface([self.grid_scale,self.grid_scale])
                    surface.fill(GRAY_COLOR_1)
                    self.game_surface.blit(surface , (i[0]-250,i[1])) 
          for i in self.tab_grid:
               if(i[2] == "BOMB" and i[3] == True):
                    n_bomb_demined += 1
          
          if(n_bomb_demined == self.n_bomb):
               self.finished = True

          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    self.run = False
               if event.type == pygame.MOUSEBUTTONUP:
                    pos = event.pos
                    if pos[0] <= 250 :
                         return
                    if event.button == 3:
                         for i in self.tab_grid:
                              if(i[0] < pos[0] < i[0]+self.grid_scale and i[1] < pos[1] < i[1]+self.grid_scale and not i[3]):
                                   surface = pygame.Surface([self.grid_scale,self.grid_scale])
                                   surface.fill(GREEN_COLOR)
                                   self.game_surface.blit(surface , (i[0]-250,i[1]))
                                   self.game_surface.blit(pygame.font.Font(None , 2*int(self.grid_scale/2)).render(f"D",True,(0,0,0)) , [i[0]+int(self.grid_scale/4)-250 , i[1]+int(self.grid_scale/4)])
                                   i[3] = True  
                                   break
                              elif(i[0] < pos[0] < i[0]+self.grid_scale and i[1] < pos[1] < i[1]+self.grid_scale and i[3]):
                                   surface = pygame.Surface([self.grid_scale,self.grid_scale])
                                   surface.fill([131, 135, 138])
                                   self.game_surface.blit(surface , (i[0]-250,i[1]))
                                   i[3] = False  
                                   break

                    elif event.button == 1:
                         for i in self.tab_grid:
                              if(i[0] < pos[0] < i[0]+self.grid_scale and i[1] < pos[1] < i[1]+self.grid_scale and i[2] == "NONE"):
                                   surface = pygame.Surface([self.grid_scale,self.grid_scale])
                                   surface.fill(GRAY_COLOR_1)
                                   self.game_surface.blit(surface , (i[0]-250,i[1]))
                                   self.game_surface.blit(pygame.font.Font(None , 2*int(self.grid_scale/2)).render(f"{self.detector[self.tab_grid.index(i)][0]}",True,(0,0,0)) , [i[0]+int(self.grid_scale/4)-250 , i[1]+int(self.grid_scale/4)])
                                   break

                              elif(i[0] < pos[0] < i[0]+self.grid_scale and i[1] < pos[1] < i[1]+self.grid_scale and i[2] == "BOMB"):
                                   self.game_surface.fill(GRAY_COLOR_1)
                                   for b in self.pos_bomb:
                                        surface = pygame.Surface([self.grid_scale,self.grid_scale])
                                        surface.fill(RED_COLOR)
                                        self.game_surface.blit(surface , (b[0]*self.grid_scale,b[1]*self.grid_scale))
                                   screen.blit(self.game_surface , [250,0])
                                   pygame.display.flip()
                                   time.sleep(5)
                                   self.lose = True
                                   break
