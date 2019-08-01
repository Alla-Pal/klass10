from drawman import *
from time import sleep
pen_up()
to_point(4,0)
pen_down()
to_point(4,4)
for x in range(2,7):
    pen_down()
    to_point(x,6)
    pen_up()
    to_point(4,4)
t.hideturtle()
sleep(20)
