from drawman import *
from time import sleep
A=[(0,0), (200,0), (200,200), (0,200),(0,0)]
pen_down()
for x,y in A:
    to_point(x,y)
pen_up()
sleep(20)

