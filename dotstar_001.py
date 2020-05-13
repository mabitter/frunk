#!/usr/bin/python3
# CircuitPython demo - Dotstar
import time
import adafruit_dotstar as dotstar
import board
import sys


print ("script name     : %s" % (sys.argv[0]))
print ("brightness      : %s" % (sys.argv[1]))

#remember the first argv is the filename
brightness = float(sys.argv[1])
num_pixels = 300

red = (255, 0, 0)
yellow = (255, 150, 0)
orange = (255, 40, 0)
green = (0, 255, 0)
teal = (0, 255, 120)
cyan = (0, 255, 255)
blue = (0, 0, 255)
purple = (180, 0, 255)
magenta = (255, 0, 20)
white = (255, 255, 255)


#pixels = dotstar.DotStar(board.A1, board.A2, num_pixels, brightness=0.1, auto_write=False)
pixels = dotstar.DotStar(board.SCK, board.MOSI, num_pixels, brightness=brightness, auto_write=False)
num_dots = len(pixels)
print(num_dots)


def is_float(value):
    try: 
        float(value)
        return True
    except:
        return False 

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)


def color_fill(color, wait):
    pixels.fill(color)
    pixels.show()
    time.sleep(wait)


def slice_alternating(wait):
    pixels[::2] = [red] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[1::2] = [orange] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[::2] = [yellow] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[1::2] = [green] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[::2] = [teal] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[1::2] = [cyan] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[::2] = [blue] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[1::2] = [purple] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[::2] = [magenta] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[1::2] = [white] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)


def slice_rainbow(wait):
    pixels[::6] = [red] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[1::6] = [orange] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[2::6] = [yellow] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[3::6] = [green] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[4::6] = [blue] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)
    pixels[5::6] = [purple] * (num_pixels // 6)
    pixels.show()
    time.sleep(wait)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


try : 
    while True:
        # Change this number to change how long it stays on each solid color.
        # color_fill(red, 2.0)
        # color_fill(yellow, 2.0)
        # color_fill(orange, 2.0)
        # color_fill(green, 2.0)
        # color_fill(teal, 2.0)
        # color_fill(cyan, 2.0)
        # color_fill(blue, 2.0)
        # color_fill(purple, 2.0)
        # color_fill(magenta, 2.0)
        # color_fill(white, 2.0)

        # Increase or decrease this to speed up or slow down the animation.
        # slice_alternating(0.1)
        # color_fill(white, 0.5)

        # Increase or decrease this to speed up or slow down the animation.
        # slice_rainbow(0.1)
        # time.sleep(0.5)

        # Increase this number to slow down the rainbow animation.
        rainbow_cycle(0.01)
        rainbow_cycle(0.01)
        rainbow_cycle(0.01)

except KeyboardInterrupt:
    print('keyboard interrupt!')

    for dot in range(num_dots):
        pixels[dot] = (0,0,0)
        pixels.show()



