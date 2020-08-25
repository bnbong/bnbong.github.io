from turtle import *
speed (10)
up()
x = -200
v_x = 30
for i in range (20):
   x = x+v_x
   goto (x,0)
   down ()
   circle (5)
   up ()
done()
