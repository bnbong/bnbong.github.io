from turtle import *
speed (10)
up ()
y = 100
v_y = 0
a_y = -10
for i in range (20):
    y = y+v_y
    goto (0,y)
    down ()
    circle (5)
    up()
    v_y = v_y + a_y
done()
          
