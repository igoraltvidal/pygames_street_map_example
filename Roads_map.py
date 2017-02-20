import pygame
from pygame.locals import *

screen = pygame.display.set_mode((1200, 700), 0, 32)

background_colour = (0,122,20)
screen.fill(background_colour)

class Street:

    def __init__(self,pos_x,pos_y,name_complement):
        self.image_filename = 'roads/road' + name_complement + '.tga'
        self.image = pygame.image.load(self.image_filename).convert()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.center_x = pos_x + 50
        self.center_y = pos_y + 50
        self.pos = self.image.get_rect()
        self.pos.x = pos_x
        self.pos.y = pos_y
        screen.blit(self.image,self.pos)


street1 = Street(0,200,'TE')
street2 = Street(0,0,'SE')
street3 = Street(0,100,'NS')
street4 = Street(0,300,'NS')
street5 = Street(0,400,'NE')
street6 = Street(100,400,'EW')
street7 = Street(200,400,'NEWS')
street8 = Street(200,500,'NS')
street9 = Street(200,600,'NE')
street10 = Street(100,200,'EW')
street11 = Street(200,200,'TS')
street12 = Street(200,300,'NS')
street13 = Street(300,200,'EW')
street14 = Street(400,200,'TS')
street15 = Street(400,300,'NS')
street16 = Street(400,400,'NW')
street17 = Street(300,400,'EW')
street18 = Street(500,200,'EW')
street19 = Street(600,200,'TW')
street20 = Street(400,600,'EW')
street21 = Street(300,600,'EW')
street22 = Street(500,600,'EW')
street23 = Street(600,600,'TN')
street24 = Street(600,500,'NS')
street25 = Street(600,400,'NS')
street26 = Street(600,300,'NS')
street27 = Street(600,100,'NS')
street28 = Street(600,0,'TS')
street29 = Street(500,0,'EW')
street30 = Street(400,0,'EW')
street31 = Street(300,0,'EW')
street32 = Street(200,0,'EW')
street33 = Street(100,0,'EW')
street34 = Street(700,0,'EW')
street35 = Street(700,600,'EW')
street36 = Street(800,0,'TS')
street37 = Street(800,600,'TN')
street38 = Street(800,100,'NS')
street39 = Street(800,200,'TE')
street40 = Street(800,300,'NS')
street41 = Street(800,400,'TE')
street42 = Street(800,500,'NS')
street43 = Street(900,0,'EW')
street44 = Street(1000,0,'EW')
street45 = Street(1100,0,'SW')
street46 = Street(1100,100,'NS')
street47 = Street(1100,200,'TW')
street48 = Street(1100,300,'NS')
street49 = Street(1100,400,'TW')
street50 = Street(1100,500,'NS')
street51 = Street(1100,600,'NW')
street52 = Street(1000,600,'EW')
street53 = Street(900,600,'EW')
street54 = Street(900,200,'EW')
street55 = Street(1000,200,'EW')
street56 = Street(900,400,'EW')
street57 = Street(1000,400,'EW')

while True:

    pygame.display.update()
