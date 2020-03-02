from sense_hat import SenseHat 
from time import sleep
from random import randint

sense = SenseHat()

r = (randint(0, 255), randint(0, 255), randint(0, 255))

x = 0
y = 0

while True:
  sense.set_pixel(x, y, r)
  sleep(1)
  sense.clear()
        
  if y == 7 and x == 7:
    x = 0
    y = 0
  elif y == 7:
    y = 0
    x += 1
  else:
    y +=1