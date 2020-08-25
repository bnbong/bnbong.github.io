from turtle import *

v= [int(0),int(0)]

def power_up():
     v[0] = v[0] + 1
     print("x축 속력:",v[0],"/","y축 속력:",v[1])

def power_down():
    v[0] = v[0] - 1
    print("x축 속력:",v[0],"/","y축 속력:",v[1])

def turn_up():
    v[1] = v[1] + 1
    print("x축 속력:",v[0],"/","y축 속력:",v[1])

def turn_down():
    v[1] = v[1] - 1
    print("x축 속력:",v[0],"/", "y축 속력:",v[1])

def fire():
    x = -320
    y = 0

    v_x = v[0]
    v_y = v[1]

    a_y = -1

    while(y > -300):
        x = x + v_x
        v_y = v_y + a_y
        y = y + v_y
        goto(x, y)
        down()
        circle(3)
        up()
   
speed(100)
up()
goto(-320,0)
down()
up()
goto (320, 0)
down()
circle (5)
up()
goto (380,0)
down()
circle (5)
goto (388,0)
goto(388,-500)
up()


onkeypress(power_up,"Right")
onkeypress(power_down,"Left")
onkeypress(turn_up,"Up")
onkeypress(turn_down,"Down")
onkeypress(fire, "space")
listen()
done()

    
