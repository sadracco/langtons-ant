#!/usr/bin/python3
from ant import *
from fade import rainbowColor

pg.init()
pg.display.set_caption('Langtons Ant')
pg.event.set_allowed([QUIT, KEYDOWN, MOUSEBUTTONDOWN])
clock = pg.time.Clock()

on = True
animation = False
framerate = 10

SC = 10

screen = pg.display.set_mode((1000, 700), DOUBLEBUF)
screen.set_alpha(None)

ants = []

def setColors(antset):
    screen.fill((0,0,0))
    for i, ant in enumerate(antset):
        ant.color = rainbowColor((1/len(antset))*i)
        ant.drawRect(ant.color)

while(on):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
            on = False

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and animation == False:
            mpos = pg.mouse.get_pos()
            ants.append(Ant(mpos[0] - mpos[0]%SC,mpos[1] - mpos[1]%SC,screen,SC))
            setColors(ants)

        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            animation = not animation

        if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
            animation = False
            ants = []
            screen.fill((0,0,0))

        if event.type == pg.KEYDOWN and event.key == pg.K_UP:
            framerate = (framerate+10)%120

        if event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
            framerate = (framerate-10)%120

    if animation:
        for ant in ants:
            ant.move()

    pg.display.flip()
    clock.tick(framerate)
