import pygame
import time
import  math

GRAY_COLOR = [193, 198, 199]
GRAY_COLOR_1 = [190, 196, 196]
COLOR_1 = [75, 77, 77]
COLOR_2 = [37, 38, 38]

class Panel:

     def __init__(self):
          
          self.surface = pygame.Surface([250,450])
          self.surface.fill(GRAY_COLOR)
          self.FONT_PTSANS_1 = pygame.font.Font("./fonts/PTSans-Bold.ttf",22)
          self.FONT_PTSANS_2 = pygame.font.Font("./fonts/PTSans-Bold.ttf",20)
          self.FONT_PTSANS_3 = pygame.font.Font("./fonts/PTSans-Bold.ttf",20)
          self.plabel_1 = Plabel("ez",self.FONT_PTSANS_1,pos=[25,50],font_color=GRAY_COLOR_1,rect_color=COLOR_1,rect_size=[200,80])
          self.plabel_2 = Plabel("ez",self.FONT_PTSANS_2,pos=[25,180],font_color=GRAY_COLOR_1,rect_color=COLOR_1,rect_size=[200,80])
          self.pbutton_1 = Pbutton("reset",self.FONT_PTSANS_3,overflight_color=COLOR_2,pos=[0,400],font_color=GRAY_COLOR_1,rect_color=COLOR_1,rect_size=[250,50])

class Plabel:

     def __init__(self ,text,font,rect_color=[255,255,255],font_color=[0,0,0], pos=[0,0] , rect_size=[50,50]):

          self.text = text
          self.rect_size = rect_size
          self.rect_color = rect_color
          self.font_color = font_color
          self.pos = pos
          self.surface = pygame.Surface(rect_size)
          self.surface.fill(rect_color)
          self.font = font

     def apply(self,panel):
          
          self.surface.fill(self.rect_color)
          render = self.font.render(self.text,True,self.font_color)
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
          self.surface = pygame.Surface(rect_size)
          self.surface.fill(rect_color)
          self.font = font

     def apply(self,panel):
          
          self.surface.fill(self.rect_color)
          render = self.font.render(self.text,True,self.font_color)
          text_pos= [ self.rect_size[0]/2 - self.font.size(self.text)[0]/2, self.rect_size[1]/2 - self.font.size(self.text)[1]/2 ]
          self.surface.blit(render , text_pos)
          panel.blit(self.surface,self.pos)
     
     def overfly(self,panel):

          self.surface.fill(self.overflight_color)
          render = self.font.render(self.text,True,self.overflight_font_color)
          text_pos= [ self.rect_size[0]/2 - self.font.size(self.text)[0]/2, self.rect_size[1]/2 - self.font.size(self.text)[1]/2 ]
          self.surface.blit(render , text_pos)
          panel.blit(self.surface,self.pos)
     
     def clicked(self):
          self.function_target()
