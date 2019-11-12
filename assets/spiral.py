# importing the packages from the third parties is the same as local files

from matplotlib import pyplot
from turtle import *
from random import randint

speed(0)
bgcolor('black')

x = 1

while x < 400:
	r = randint(0,255)
	g = randint(0,255)
	b = randint(0,255)

	colormode(255)

	pencolor(r, g, b)

	fd(200 + x)
	rt(90.911)

	x = x + 1