import pygame as pg
from pygame.locals import *
from random import randint

class Ant:
    def __init__(self, x, y, screen, scale):
        self.x = x
        self.y = y
        self.scale = scale
        self.screen = screen
        self.color = (255,255,255)
        self.mv = ((0,1),(-1,0),(0,-1),(1,0))
        self.dir = randint(0,4)

    def draw(self, c):
        self.screen.set_at((self.x, self.y), c)
        
    def drawRect(self, c):
        pg.draw.rect(self.screen, c, (self.x, self.y, self.scale, self.scale))

    def move(self):
        gcolor = self.screen.get_at((self.x, self.y))
        if gcolor == (0,0,0) or gcolor == (255,255,255):
            self.dir = (self.dir-1)%4
            self.drawRect(self.color)
        else:
            self.dir = (self.dir+1)%4
            self.drawRect((0,0,0))

        self.x += self.mv[self.dir][0] * self.scale
        self.y += self.mv[self.dir][1] * self.scale
        self.x = self.x % self.screen.get_width()
        self.y = self.y % self.screen.get_height()
