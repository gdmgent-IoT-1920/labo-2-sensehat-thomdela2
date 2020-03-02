from sense_hat import SenseHat 
from time import sleep
from random import randint

sense = SenseHat()

# pinguin_colors
background = (0,0,0)
light_yelow = (255, 255, 179)
orange = (255, 85, 0)
black = (25, 25, 25)
grey = (127, 127, 127)
orange_shadow = (164, 55, 0)
white = (255, 255, 255)
# snowman_colors
grey_shadow = (51, 51, 51)
red = (255, 0, 0)
red_shadow = (127, 0, 0)
# ghost_colors
light_grey = (204, 204, 204)
# scorpio_colors
red_dark = (94, 0, 0)
yello_shadow = (130, 127, 0)

# pinguin
char_1 = [
	background, background, background, background, background, background, background, background, 
	background, background, light_yelow, black, black, background, background, background,
	background, orange, black, black, black, black, background, background,
	background, background, background, white, grey, black, black, background,
	background, background, background, white, white, grey, black, background,
	background, background, background, white, white, grey, black, background,
	background, background, background, white, black, black, background, background,
	background, background, orange_shadow, black, black, orange, background, background
]
# snowman
char_2 = [
	background, background, background, black, grey_shadow, grey, background, background,
	background, black, black, grey_shadow, grey_shadow, grey_shadow, grey, grey,
	background, background, grey_shadow, white, white, white, white, background,
	background, background, black, white, black, white, white, red,
	background, orange_shadow, orange, white, white, white, red, background,
	background, background, red_shadow, red, red, red, white, red,
	background, background, grey_shadow, grey_shadow, white, white, white, background,
	background, background, background, grey_shadow, grey_shadow, white, background, background
]
# ghost
char_3 = [
	background, background, background, light_grey, white, background, background, background,
	background, background, light_grey, white, white, white, background, background,
	background, light_grey, black, white, black, white, white, background,
	background, light_grey, black, white, black, white, white, background,
	background, light_grey, white, white, white, white, white, background,
	background, background, light_grey, white, white, white, background, background,
	background, background, background, light_grey, white, white, background, white,
	background, background, background, background, background, white, white, background
]
#scorpion
char_4 = [
	background, background, background, background, background, red_shadow, red, background,
	background, background, background, background, background, background, red_shadow, red,
	background, background, background, background, background, background, background, red,
	background, background, background, background, background, background, background, red,
	background, background, background, background, background, background, red_shadow, red,
	background, background, light_yelow, red_shadow, red, red_shadow, red, background,
	background, red_dark, red_dark, red_shadow, red, red, background, background,
	yello_shadow, red_dark, yello_shadow, red, red, background, red, background
]

while True:
	sense.set_pixels(char_1)
	sleep(2)
	sense.set_pixels(char_2)
	sleep(2)
	sense.set_pixels(char_3)
	sleep(2)
	sense.set_pixels(char_4)
	sleep(2)