#-----------importing the required modules --------------------#
from functions import * #self created module for cutting function
import pygame
from pygame.locals import *
import random
#----------------------------------------------------------------#

WIDTH,HEIGHT=1000,1000
pygame.display.init()
pygame.display.set_mode((WIDTH,HEIGHT),DOUBLEBUF)
#-----------------class definition of enemy goomba groups(all_sprites,enemy_group,goomba_group----------#
class goomba(pygame.sprite.Sprite):
    def __init__(self,x,y,group,velocity):
        super(goomba,self).__init__()
        self.index=0
        self.default_image=images[0][6]
        self.image=self.default_image
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.add(group)
        self.jump=False
        self.velocity=velocity
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

#-------------------groups------------------------#
enemy_group=pygame.sprite.Group()
goomba_group=pygame.sprite.Group()
all_sprites=pygame.sprite.Group()
#--------------------------------------------------#

#cutting the sprites to the row major order that will return an array 9*6
images=cut_image("images/goomba.png",n_x=9,n_y=6,position=2)

#----------------------function to create goomba instances----------------------------------------------#
def create_goombas(n_goombas):
    list_goombas=[]
    for i in range(n_goombas):
        x=random.randint(20,WIDTH-20)
        velocity=random.randint(1,7)
        g=goomba(x=x,y=HEIGHT-160,group=[enemy_group,goomba_group,all_sprites],velocity=velocity)                      # $(later there will be several instances here)1
        list_goombas.append(g)
    return list_goombas
#---------------------------------------------------------------------------------------------------------#



