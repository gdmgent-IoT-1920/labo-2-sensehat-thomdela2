from sense_hat import SenseHat 
from time import sleep
from random import randint

random_color1 = (randint(0, 255), randint(0, 255), randint(0, 255)) 
random_color2 = (randint(0, 255), randint(0, 255), randint(0, 255)) 
random_color3 = (randint(0, 255), randint(0, 255), randint(0, 255)) 

sense = SenseHat()

while True:
	sense.show_letter("N", random_color1)
	sleep(1)
	sense.show_letter("M", random_color2)
	sleep(1)
	sense.show_letter("D", random_color3)
	sleep(3)
