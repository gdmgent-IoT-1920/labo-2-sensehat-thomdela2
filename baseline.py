from sense_hat import SenseHat 
from time import sleep
from random import randint

sense = SenseHat()

random_colour1 = (randint(0, 255), randint(0, 255), randint(0, 255)) 
random_colour2 = (randint(0, 255), randint(0, 255), randint(0, 255)) 

sense.show_message("Hello! We are New Media Development :)",text_colour=random_colour1,back_colour=random_colour2)