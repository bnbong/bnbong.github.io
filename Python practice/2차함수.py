from turtle import *
speed (10)
up()
x = -200
y = 400
v_x = 30
v_y = -100
a_y = 10
for i in range (20):
    x = x+v_x
    y = y+v_y
    goto (x,y)
    down()
    circle (5)
    up()
    v_y = v_y + a_y
done()
