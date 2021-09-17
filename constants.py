import pygame
from panel import *

pygame.font.init()

FONT_1 = pygame.font.Font("./fonts/PTSans-Bold.ttf",30)
GRAY_COLOR = [193, 198, 199]
GRAY_COLOR_1 = [190, 196, 196]
GRAY_COLOR_2 = [100, 103, 107]
COLOR_1 = [75, 77, 77]
COLOR_2 = [37, 38, 38]
RED_COLOR = (222, 57, 35)
GREEN_COLOR = [113, 230, 78]

FONT_PTSANS_1 = pygame.font.Font("./fonts/PTSans-Bold.ttf",20)
plabel_1 = Plabel("ez",FONT_PTSANS_1,pos=[25,20],font_color=GRAY_COLOR_1,rect_color=COLOR_1,rect_size=[200,60])
plabel_2 = Plabel("ez",FONT_PTSANS_1,pos=[25,105],font_color=GRAY_COLOR_1,rect_color=COLOR_1,rect_size=[200,60])
pbutton_1 = Pbutton("reset",FONT_PTSANS_1,overflight_color=COLOR_2,pos=[0,400],font_color=GRAY_COLOR_1,rect_color=COLOR_1,rect_size=[250,50])