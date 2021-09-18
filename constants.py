import pygame
from panel import *

pygame.font.init()

texts =["You demined all the bombs !","Enjoy the game ! :)","Tips :",
     "1 - <Right-click> to place flag",
     "2 - <Left-click> to show cases",
     "3 - The case number equals to the ",
     " bomb number around"]
gs_size = [ [450,450] , [500,500] , [600,600] , [650,650]]

FONT_PTSANS_2 = pygame.font.Font("./fonts/PTSans-Bold.ttf",30)
FONT_PTSANS_1 = pygame.font.Font("./fonts/PTSans-Bold.ttf",20)
FONT_PTSANS_3 = pygame.font.Font("./fonts/PTSans-Bold.ttf",15)
FONT_PTSANS_4 = pygame.font.Font("./fonts/PTSans-Bold.ttf",17)

GRAY_COLOR = [193, 198, 199]
GRAY_COLOR_1 = [190, 196, 196]
GRAY_COLOR_2 = [100, 103, 107]
COLOR_1 = [75, 77, 77]
COLOR_2 = [37, 38, 38]
RED_COLOR = (222, 57, 35)
GREEN_COLOR = [113, 230, 78]

tuto1_label = Plabel(texts[3],FONT_PTSANS_3,font_color=[200,200,200],padding=[0,0])
tuto2_label = Plabel(texts[4],FONT_PTSANS_3,font_color=[200,200,200],padding=[0,0])
tuto3_label = Plabel(texts[5],FONT_PTSANS_3,font_color=[200,200,200],padding=[0,0])
tuto4_label = Plabel(texts[6],FONT_PTSANS_3,font_color=[200,200,200],padding=[0,0])
tuto5_label = Plabel(texts[1],FONT_PTSANS_3,font_color=[200,200,200],padding=[50,2])
tuto6_label = Plabel(texts[2],FONT_PTSANS_1,font_color=[245,245,245],padding=[90,10])

game_finished_label = Plabel(texts[0],FONT_PTSANS_2,font_color=[200,200,200],rect_color=[11, 11, 11, 96],rect_size=[450,450])
plabel_1 = Plabel("ez",FONT_PTSANS_1,pos=[25,20],font_color=GRAY_COLOR_1,rect_color=COLOR_1,rect_size=[200,60])
plabel_2 = Plabel("ez",FONT_PTSANS_1,pos=[25,105],font_color=GRAY_COLOR_1,rect_color=COLOR_1,rect_size=[200,60])
pbutton_1 = Pbutton("reset",FONT_PTSANS_1,overflight_color=COLOR_2,pos=[0,400],font_color=GRAY_COLOR_1,rect_color=COLOR_1,rect_size=[250,50])
uplevel_button = Pbutton(">",FONT_PTSANS_1,overflight_color=COLOR_2,pos=[125,350],font_color=GRAY_COLOR_1,rect_color=COLOR_1,rect_size=[125,50])
lowerlevel_button = Pbutton("<",FONT_PTSANS_1,overflight_color=COLOR_2,pos=[0,350],font_color=GRAY_COLOR_1,rect_color=COLOR_1,rect_size=[125,50])