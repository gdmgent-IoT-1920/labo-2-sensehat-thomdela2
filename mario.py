from sense_hat import SenseHat 
from time import sleep
from random import randint

sense = SenseHat()

b = (51, 102, 255) # Blauw
a = (49, 205, 202) # Azuurblauw
z = (0, 0, 0) # Zwart
s = (252, 204, 156) # skin

user = [
	z,z,b,b,a,b,z,z,
	z,b,b,s,a,s,b,z,
	z,b,s,z,s,z,s,z,
	z,a,s,s,s,s,s,z,
	b,b,a,z,z,s,a,b,
	b,z,b,a,a,b,z,b,
	z,z,a,b,b,a,z,z,
	z,b,b,z,z,b,b,z
]

jump = [
	z,b,b,s,a,s,b,z,
	z,b,s,z,s,z,s,z,
	z,a,s,s,s,s,s,z,
	b,b,a,z,z,s,a,b,
	b,z,b,a,a,b,z,b,
	z,z,a,b,b,a,z,z,
	z,b,b,z,z,b,b,z,
	z,z,z,z,z,z,z,z
]

sense.set_pixels(user)

while True:
  for event in sense.stick.get_events():
	if event.direction == 'up':
		sense.set_pixels(jump)
		sleep(0.1)
		sense.set_pixels(user)
