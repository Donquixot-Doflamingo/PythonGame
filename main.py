from random import *
from turtle import *

# extracting vector class from base file
from base import vector

player = vector(0,0)
print(player.x)
aim = vector(2,0)

def wrap(value):

    if value == 210:
        dot(10, 'red')
    return value

def draw():
    #move and draw player
    player.move(aim)

    player.x = wrap(player.x)
    player.y = wrap(player.y)

    aim.move(random() - 0.5)
    aim.rotate(random()*10 - 5)

    clear()
    goto(player.x, player.y)
    dot(10)

    if True:
        ontimer(draw, 100)


#setup a screen for us width height startx and starty as parameter
setup(420,420,370,0)
hideturtle()
tracer(False)
up()
draw()
done()

