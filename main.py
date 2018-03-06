#MAIN FILE


#-----------importing the required modules --------------------#
from pygame.locals import *
import sys
from functions import * #self created module for cutting function
import pygame
import random
from goomba import *
#----------------------------------------------------------------#

#--------setting up the global variables----------#
WIDTH,HEIGHT=1000,1000
surface=pygame.display.set_mode((WIDTH,HEIGHT),DOUBLEBUF)
#creating the background ********very important******** to mention the pygame.SRCAPLHA here to avoid background color for sprites
background=pygame.Surface((WIDTH,HEIGHT),pygame.SRCALPHA,32)
#adding background image to the game
background_image=pygame.image.load("images/background.png")
background_image=pygame.transform.scale(background_image,(WIDTH,HEIGHT  ))


#cutting the sprites to the row major order that will return an array 9*6
images=cut_image("images/goomba.png",n_x=9,n_y=6,position=2)
print(images.shape)

#setting up frames per second and clock
clock=pygame.time.Clock()
FPS=60
#--------------------------------------------------#




#------------------creating instances------------#
g=create_goombas(3)
#------------------------------------------------#



#----------------------------------The event loop------------------------------------------------#

#the while loop will continously check the event changes and update the frame
while True:                                                                            # $(later instead of infinite loop add until game not over)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    surface.blit(background_image, dest=(0, 0), area=(0, 0, WIDTH, HEIGHT))
    all_sprites.clear(surface, background)
    all_sprites.update()
    all_sprites.draw(surface)
    pygame.display.update()
    clock.tick(FPS)

#---------------------------------------------------------------------------------------------------#
