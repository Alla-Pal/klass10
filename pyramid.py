from drawman import *
from time import sleep
to_point(7,7)
a=6
for i in range (1,7):
    pen_down()
    on_vector(a,-a)
    on_vector(-a,a)
    on_vector(-a,-a)
    on_vector(a,a)
    pen_up()
    on_vector(0,-1)
    a=a-1











sleep(20)
