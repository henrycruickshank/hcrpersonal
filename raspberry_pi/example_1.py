# Example using PIO to drive a set of WS2812 LEDs.

import array, time
from machine import Pin
import rp2

led = 15

# Configure the number of WS2812 LEDs.
NUM_LEDS = led+1
PIN_NUM = 0
brightness = 0.1

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()


# Create the StateMachine with the ws2812 program, outputting on pin
sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(PIN_NUM))

# Start the StateMachine, it will wait for data on its FIFO.
sm.active(1)

# Display a pattern on the LEDs via an array of LED RGB values.
ar = array.array("I", [0 for _ in range(NUM_LEDS)])

##########################################################################
def pixels_show():
    dimmer_ar = array.array("I", [0 for _ in range(NUM_LEDS)])
    for i,c in enumerate(ar):
        r = int(((c >> 8) & 0xFF) * brightness)
        g = int(((c >> 16) & 0xFF) * brightness)
        b = int((c & 0xFF) * brightness)
        dimmer_ar[i] = (g<<16) + (r<<8) + b
    sm.put(dimmer_ar, 8)
    time.sleep_ms(2)

def pixels_set(i, color):
    ar[i] = (color[1]<<16) + (color[0]<<8) + color[2]

def pixels_fill(color):
    for i in range(len(ar)):
        pixels_set(i, color)

def color_chase(WHITE,BLACK, wait):
    for i in range(NUM_LEDS):
        if i <= led:
            pixels_set(i, WHITE)
            time.sleep(wait)
            pixels_show()
    for i in range(NUM_LEDS):
        if i < led:
            pixels_set(i, BLACK)  
            time.sleep(wait)
            pixels_show()
    pixels_set(led,BLACK)
    time.sleep(5)
    pixels_show()
            
 
 
BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# YELLOW = (255, 150, 0)
# GREEN = (0, 255, 0)
# CYAN = (0, 255, 255)
# BLUE = (0, 0, 255)
# PURPLE = (180, 0, 255)
WHITE = (220, 150, 40)
# COLORS = (RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE)
# COLORS = (RED,YELLOW)


print("chases")    
color_chase(WHITE,BLACK, 0.01)

