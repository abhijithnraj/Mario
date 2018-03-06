#-----------importing the required modules --------------------#
from pygame.locals import *
import sys
from functions import * #self created module for cutting function
import pygame
import random
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



#-------------------groups------------------------#
enemy_group=pygame.sprite.Group()
goomba_group=pygame.sprite.Group()
all_sprites=pygame.sprite.Group()
#--------------------------------------------------#




#-----------------class definition of enemy goomba groups(all_sprites,enemy_group,goomba_group----------#
class goomba(pygame.sprite.Sprite):
    def __init__(self,x,y,group):
        super(goomba,self).__init__()
        self.index=0
        self.default_image=images[0][6]
        self.image=self.default_image
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.add(group)
        self.jump=False
        self.velocity=3
        self.jump_velocity=0
        self.jump_counter=0
    #the update function will make the goomba dance around the screen (randomly for now)
    def update(self):
        x,y=self.rect.center
        x+=self.velocity
        y+=self.jump_velocity
        if x>WIDTH:
            self.velocity*=-1
            self.default_image=images[0][0]
        if x<0:
            self.velocity*=-1
            self.default_image=images[0][6]
        r=random.randint(0,10000)
        if not self.jump:
            if r<50:
                self.jump=True
                self.image=images[4][2]
                self.jump_velocity=-10
        if y<650:
            self.jump_velocity*=-1
        if y>HEIGHT-160:
            y=HEIGHT-160
            self.jump=False
            self.image=self.default_image
        self.image=self.default_image
        self.rect.center = x, y




    #check funnction when called to the variable will update the image frame by frame - used for debugging images
    def check_changeframe(self):
        self.image=images[0][self.index]
        print("showing frame:"+str(self.index))
        self.index=(self.index+1)%len(images[0])

#----------------------------------------------------------------------------------------------------------#



#----------------------creating the instances of the classes----------------------------------------------#
g=goomba(100,HEIGHT-160,[enemy_group,goomba_group,all_sprites])                      # $(later there will be several instances here)

#---------------------------------------------------------------------------------------------------------#



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
