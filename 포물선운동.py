from turtle import *
speed (10)
up ()
x = -200
y = 100
v_x = 30
v_y = 0
a_y = -10
for i in range (30):
    x = x+v_x
    y = y+v_y
    goto (x,y)
    down()
    circle (5)
    up()
    v_y = v_y + a_y
done()
