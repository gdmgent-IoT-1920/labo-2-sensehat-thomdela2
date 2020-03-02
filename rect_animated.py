from sense_hat import SenseHat 
from time import sleep
from random import randint

sense = SenseHat()

r = (randint(0, 255), randint(0, 255), randint(0, 255)) 
z = (0, 0, 0)

start_end = [
	z,z,z,z,z,z,z,z,
	z,z,z,z,z,z,z,z,
	z,z,z,z,z,z,z,z,
	z,z,z,z,z,z,z,z,
	z,z,z,z,z,z,z,z,
	z,z,z,z,z,z,z,z,
	z,z,z,z,z,z,z,z,
	z,z,z,z,z,z,z,z
]

rect_1 = [
	z,z,z,z,z,z,z,z,
	z,z,z,z,z,z,z,z,
	z,z,z,z,z,z,z,z,
	z,z,z,r,r,z,z,z,
	z,z,z,r,r,z,z,z,
	z,z,z,z,z,z,z,z,
	z,z,z,z,z,z,z,z,
	z,z,z,z,z,z,z,z
]

rect_2 = [
	z,z,z,z,z,z,z,z,
	z,z,z,z,z,z,z,z,
	z,z,r,r,r,r,z,z,
	z,z,r,z,z,r,z,z,
	z,z,r,z,z,r,z,z,
	z,z,r,r,r,r,z,z,
	z,z,z,z,z,z,z,z,
	z,z,z,z,z,z,z,z
]

rect_3 = [
	z,z,z,z,z,z,z,z,
	z,r,r,r,r,r,r,z,
	z,r,z,z,z,z,r,z,
	z,r,z,z,z,z,r,z,
	z,r,z,z,z,z,r,z,
	z,r,z,z,z,z,r,z,
	z,r,r,r,r,r,r,z,
	z,z,z,z,z,z,z,z
]

rect_4 = [
	r,r,r,r,r,r,r,r,
	r,z,z,z,z,z,z,r,
	r,z,z,z,z,z,z,r,
	r,z,z,z,z,z,z,r,
	r,z,z,z,z,z,z,r,
	r,z,z,z,z,z,z,r,
	r,z,z,z,z,z,z,r,
	r,r,r,r,r,r,r,r
]

while True:
	sense.set_pixels(start_end)
	sleep(1)
	sense.set_pixels(rect_1)
	sleep(1)
	sense.set_pixels(rect_2)
	sleep(1)
	sense.set_pixels(rect_3)
	sleep(1)
	sense.set_pixels(rect_4)
	sleep(1)
	sense.set_pixels(rect_3)
	sleep(1)
	sense.set_pixels(rect_2)
	sleep(1)
	sense.set_pixels(rect_1)
	sleep(1)