import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 20)

pixels[3] = (235, 235, 52)
