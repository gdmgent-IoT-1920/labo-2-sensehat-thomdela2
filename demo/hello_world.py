# Importeer de SenseHat
from sense_hat import SenseHat
# Initailiseer
sense = SenseHat()
# Rotate 180°
sense.set_rotation(270)
# Toon bericht
sense.show_message("Hello NMD!")