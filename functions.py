
from PIL import Image
import pygame
import numpy as np


#function to cut the sprites from image file_name with n_sprites across and n_y sprites down
def cut_image(file_name,n_x,n_y,position):
    img=Image.open(file_name)
    x_original,y_original=img.size
    #if the images are linear then there is no need of calculating the difference also to avoid division by zero
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
    #resizing it to a sizable format
    img=img.resize((x,y))
    img.save("images/new.png")
    #loading the image againt to blit to the surface
    sheet = pygame.image.load("images/new.png").convert_alpha()
    images=[]
    new_images = []
    #checking whether its row major or column major kind of representation
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


def image_at(images,row,column):
    return images[row-1][column-1]