import time
from rpi_ws281x import PixelStrip, Color

# LED strip configuration:
LED_COUNT = 60        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800kHz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)

# Create PixelStrip object with appropriate configuration.
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()

# Define some colors


def colour_chase(strip, wait_ms=50):
    BLACK = Color(0, 0, 0)
    WHITE = Color(240, 240, 240)    
    """Chase one color down the strip."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, WHITE)
        strip.show()
        time.sleep(wait_ms / 1000.0)
    time.sleep(0.5)
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, BLACK)
        strip.show()
        time.sleep(wait_ms / 1000.0)

# print("Starting color chase")
# led = 20  
# while True:
#     color_chase(strip, WHITE, 50)

###################################################
#  import time
# import board
# import neopixel
# import numpy 

# # Pin where the data line is connected
# pixel_pin = board.D4

# # Number of LEDs
# num_pixels = 60

# # Brightness of the LEDs
# brightness = 0.1

# # Create NeoPixel object with the pin and number of LEDs
# pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=brightness, auto_write=False)

# # Define some colors
# BLACK = (0, 0, 0)
# WHITE = (240, 240, 240)

# def pixels_show():
#     pixels.show()

# def pixels_set(i, color):
#     pixels[i] = color

# def colour_chase(led, wait):
#     for i in range(led):
#         pixels_set(i, WHITE)
#         time.sleep(wait)
#         pixels_show()
#     for i in range(led):
#         pixels_set(i, BLACK)
#         time.sleep(wait)
#         pixels_show()
#     for i in range(num_pixels):
#         pixels_set(i, BLACK)
#         time.sleep(wait)
#         pixels_show()
#     time.sleep(1)

# print("Starting color chase")
# led = 20  
# while True:
#     color_chase(led, 0.01)


#####################################################################
# import array, time
# import RPi.GPIO as GPIO 
# import time

# GPIO.setmode(GPIO.BCM)

# BLACK = (0, 0, 0)
# # RED = (255, 0, 0)
# # YELLOW = (255, 150, 0)
# # GREEN = (0, 255, 0)
# # CYAN = (0, 255, 255)
# # BLUE = (0, 0, 255)
# # PURPLE = (180, 0, 255)
# WHITE = (240, 240, 240)
# # COLORS = (BLACK, WHITE)

# # Configure the number of WS2812 LEDs.
# NUM_LEDS = 60
# PIN_NUM = 4
# brightness = 0.1

# @rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
# def ws2812():
#     T1 = 2
#     T2 = 5
#     T3 = 3
#     wrap_target()
#     label("bitloop")
#     out(x, 1)               .side(0)    [T3 - 1]
#     jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
#     jmp("bitloop")          .side(1)    [T2 - 1]
#     label("do_zero")
#     nop()                   .side(0)    [T2 - 1]
#     wrap()


# # Create the StateMachine with the ws2812 program, outputting on pin
# sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(PIN_NUM))

# # Start the StateMachine, it will wait for data on its FIFO.
# sm.active(1)

# # Display a pattern on the LEDs via an array of LED RGB values.
# ar = array.array("I", [0 for _ in range(NUM_LEDS)])

# ##########################################################################
# def pixels_show():
#     dimmer_ar = array.array("I", [0 for _ in range(NUM_LEDS)])
#     for i,c in enumerate(ar):
#         r = int(((c >> 8) & 0xFF) * brightness)
#         g = int(((c >> 16) & 0xFF) * brightness)
#         b = int((c & 0xFF) * brightness)
#         dimmer_ar[i] = (g<<16) + (r<<8) + b
#     sm.put(dimmer_ar, 8)
#     time.sleep_ms(10)

# def pixels_set(i, color):
#     ar[i] = (color[1]<<16) + (color[0]<<8) + color[2]


# def colour_chase(led,BLACK,WHITE, wait):
#     for i in range(led):
#         pixels_set(i, WHITE)
#         time.sleep(wait)
#         pixels_show()
#     for i in range(led-1):
#         pixels_set(i, BLACK)
#         time.sleep(wait)
#         pixels_show()
#     for i in range(NUM_LEDS):
#         pixels_set(i, BLACK)
#         time.sleep(wait)
#         pixels_show()
#     time.sleep_ms(1)
 


# print("chases")
# led = 20  
# while True:   
#     colour_chase(led,BLACK, WHITE, 0.01)

