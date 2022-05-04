
from turtle import *
from unittest.result import failfast


bgcolor('black')
speed(0)
hideturtle()

for i in range(2000):
    color('red')
    circle(i)
    color('orange')
    circle(i*0.8)
    right(3)
    forward(3)

done()
