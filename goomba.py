#-----------importing the required modules --------------------#
from pygame.locals import *
import sys
from functions import * #self created module for cutting function
#----------------------------------------------------------------#

#--------setting up the global variables----------#
WIDTH,HEIGHT=1000,1000
surface=pygame.display.set_mode((WIDTH,HEIGHT),DOUBLEBUF)
images=cut_image("images/goomba.png",n_x=9,n_y=6,position=2)
#--------------------------------------------------#



#-------------------groups------------------------#
enemy_group=pygame.sprite.Group()
goomba_group=pygame.sprite.Group()
all_sprites=pygame.sprite.Group()
background=pygame.Surface((WIDTH,HEIGHT))
#--------------------------------------------------#




#-----------------class definition of enemy goomba groups(all_sprites,enemy_group,goomba_group----------#
class goomba(pygame.sprite.Sprite):
    def __init__(self,x,y,group):
        super(goomba,self).__init__()
        self.index=0
        self.image=images[0][self.index]
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.add(group)

    #check funnction when called to the variable will update the image frame by frame - used for debugging images
    def check_changeframe(self):
        self.image=images[0][self.index]
        print("showing frame:"+str(self.index))
        self.index=(self.index+1)%len(images[0])

#----------------------------------------------------------------------------------------------------------#



#----------------------creating the instances of the classes----------------------------------------------#
g=goomba(WIDTH/2,HEIGHT/2,[enemy_group,goomba_group,all_sprites])                      # $(later there will be several instances here)

#---------------------------------------------------------------------------------------------------------#



#----------------------------------The event loop------------------------------------------------#

#the while loop will continously check the event changes and update the frame
while True:                                                                            # $(later instead of infinite loop add until game not over)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                g.check_changeframe()

    all_sprites.clear(surface, background)
    all_sprites.update()
    all_sprites.draw(surface)
    pygame.display.update()

#---------------------------------------------------------------------------------------------------#
