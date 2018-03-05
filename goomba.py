import pygame
from PIL import Image
from pygame.locals import *
import sys
from pprint import pprint
import numpy as np

WIDTH,HEIGHT=1000,1000
surface=pygame.display.set_mode((WIDTH,HEIGHT),DOUBLEBUF)

debug=[]
def cut_image(file_name,n_x,n_y,position):
    img=Image.open(file_name)
    x_original,y_original=img.size
    if n_x!=0:
        x_change=int(x_original/n_x)
        x = x_change * n_x
    else:
        x_change = x_original
        y=x_original
    if n_y!=0:
        y_change=int(y_original/n_y)
        y = y_change * n_y
    else:
        y_change=y_original
        y=y_original


    img=img.resize((x,y))
    img.save("images/new.png")
    sheet = pygame.image.load("images/new.png").convert_alpha()
    images=[]
    l = []
    new_images = []
    if position==1:
        for i in range(0, x_original-x_change, x_change):
            for j in range(0,y_original-y_change,y_change):
                img = pygame.Surface((x_change,y_change), pygame.SRCALPHA).convert_alpha()
                img.blit(sheet, dest=(0, 0), area=(i, j, i +x_change,j+y_change))
                debug.append([i, j, i +x_change,j+y_change])
                images.append(img)
        a=np.array(images)
        a=a.reshape((n_x,n_y))

    elif position == 2:
        for j in range(0, y_original - y_change, y_change):
            for i in range(0, x_original-x_change, x_change):
                img = pygame.Surface((x_change,y_change), pygame.SRCALPHA).convert_alpha()
                img.blit(sheet, dest=(0, 0), area=(i, j, i +x_change,j+y_change))
                images.append(img)
        a=np.array(images)
        a=a.reshape((n_y,n_x))
    return a

images=cut_image("images/goomba.png",n_x=9,n_y=6,position=2)

enemy_group=pygame.sprite.Group()
goomba_group=pygame.sprite.Group()
all_sprites=pygame.sprite.Group()
background=pygame.Surface((WIDTH,HEIGHT))


class goomba(pygame.sprite.Sprite):
    def __init__(self,x,y,group):
        super(goomba,self).__init__()
        self.index=0
        self.image=images[0][self.index]
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.add(group)
        #print(len(images[0]))
    #def update(self):
    #    self.image=images[self.index]
    #    self.index=(self.index+1)%len(images)
    def check_changeframe(self):
        self.image=images[0][self.index]
        print("showing frame:"+str(self.index))
        self.index=(self.index+1)%len(images[0])

def image_at(images,row,column):
    return images[row-1][column-1]

g=goomba(WIDTH/2,HEIGHT/2,[enemy_group,goomba_group,all_sprites])

while True:
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

