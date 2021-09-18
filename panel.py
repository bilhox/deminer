import pygame
import time
import  math
from constants import *

class Plabel:

     def __init__(self ,text,font,rect_color=[255,255,255],font_color=[0,0,0], pos=[0,0] , rect_size=[50,50]):

          self.text = text
          self.rect_size = rect_size
          self.rect_color = rect_color
          self.font_color = font_color
          self.pos = pos
          self.surface = pygame.Surface(rect_size,pygame.SRCALPHA)
          self.surface.fill(rect_color)
          self.font = font

     def apply(self,panel):
          
          render = self.font.render(self.text,True,self.font_color)
          self.surface = pygame.Surface(self.rect_size,pygame.SRCALPHA)
          self.surface.fill(self.rect_color)
          text_pos= [ self.rect_size[0]/2 - self.font.size(self.text)[0]/2, self.rect_size[1]/2 - self.font.size(self.text)[1]/2 ]
          self.surface.blit(render , text_pos)
          panel.blit(self.surface,self.pos)

class Pbutton:
     
     def __init__(self ,text,font,function_target=None,overflight_font_color=[255,255,255],overflight_color=[0,0,0],rect_color=[255,255,255],font_color=[0,0,0], pos=[0,0] , rect_size=[50,50]):

          self.text = text
          self.rect_size = rect_size
          self.rect_color = rect_color
          self.font_color = font_color
          self.pos = pos
          self.function_target = function_target
          self.overflight_font_color = overflight_font_color
          self.overflight_color = overflight_color
          self.is_overflight = False
          self.over_time = 0
          self.surface = pygame.Surface(self.rect_size)
          self.surface.fill(self.rect_color)
          self.font = font

     def apply(self,panel):
          
          self.surface.fill(self.rect_color)
          render = self.font.render(self.text,True,self.font_color)
          text_pos= [ self.rect_size[0]/2 - self.font.size(self.text)[0]/2, self.rect_size[1]/2 - self.font.size(self.text)[1]/2 ]
          self.surface.blit(render , text_pos)
          panel.blit(self.surface,self.pos)
     
     def overflight(self,panel):

          self.surface.fill(self.overflight_color)
          render = self.font.render(self.text,True,self.overflight_font_color)
          text_pos= [ self.rect_size[0]/2 - self.font.size(self.text)[0]/2, self.rect_size[1]/2 - self.font.size(self.text)[1]/2 ]
          self.surface.blit(render , text_pos)
          panel.blit(self.surface,self.pos)
     
     def overfly(mouse_pos,panel,*button_list):
          for button in button_list:
               if button.pos[0] < mouse_pos[0] < button.pos[0]+button.rect_size[0] and button.pos[1] < mouse_pos[1] < button.pos[1]+button.rect_size[1]:
                    button.is_overflight = True
               else:
                    button.is_overflight = False
          
          for button in button_list:
               if button.is_overflight:
                    button.overflight(panel)
               else:
                    button.apply(panel)
     
     def clicked(self):
          self.function_target()
     
     def on_click(mouse_case , *button_list):

          for button in button_list:

               if button.is_overflight and mouse_case:
                    button.function_target()
