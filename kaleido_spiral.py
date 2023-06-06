import turtle as t

from itertools import cycle
colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])
               

def draw_circle(size,angle,shift):
    t.bgcolor(next(colors))
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_circle(size+10,angle-5,shift-10)
    
t.bgcolor('black')
t.speed('fast')
t.pensize(6)
draw_circle(30,0,1)



