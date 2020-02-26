from sense_hat import SenseHat 
import sys

sense = SenseHat()
sense.set_imu_config(False, False, False)

def main():
	while True:
		sense.set_pixel(7,7,255,0,0)
		sense.set_pixel(0,7,0,255,0)
		sense.set_pixel(0,9,0,0,255)

try:
	main()
except (KeyboardInterrupt, SystemExit):
	print('Programma sluiten')
finally:
	print('Opkuisen v/d matrix')
	sense.clear()
	sys.exit(0)