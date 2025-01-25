# import network
# import socket
import array, time
from machine import Pin
import rp2

# Configure the number of WS2812 LEDs.
NUM_LEDS = 60
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
    time.sleep_ms(10)

def pixels_set(i, color):
    ar[i] = (color[1]<<16) + (color[0]<<8) + color[2]


def color_chase(led,BLACK,WHITE, wait):
    for i in range(led):
        pixels_set(i, WHITE)
        time.sleep(wait)
        pixels_show()
    for i in range(led-1):
        pixels_set(i, BLACK)
        time.sleep(wait)
        pixels_show()
    for i in range(NUM_LEDS):
        pixels_set(i, BLACK)
        time.sleep(wait)
        pixels_show()
    time.sleep_ms(1)
 

BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# YELLOW = (255, 150, 0)
# GREEN = (0, 255, 0)
# CYAN = (0, 255, 255)
# BLUE = (0, 0, 255)
# PURPLE = (180, 0, 255)
WHITE = (240, 240, 240)
# COLORS = (BLACK, WHITE)


print("chases")
led = 20  
while True:   
    color_chase(led,BLACK, WHITE, 0.01)

# def web_page():
#     html = f"""
#     <!DOCTYPE html>
#     <html>
#     <form action="/select" method="post">
#         <select name="name">
#             {% for guest in guests %}
#             <option value="{{ guest }}">{{ guest }}</option>
#             {% endfor %}
#         </select>
#         <button type="submit">Find My Seat</button>
#     </form>
#     </body>
#     </html>
#     """
# @app.route('/select', methods=['POST'])
# def select_guest():
#     try:
#         name = request.form['name']
#         led_number = guests.get(name, -1)
#         if led_number != -1:
#             # Send the unique number via serial to the Pico
#             ser.write(f"{led_number}\n".encode())
#         return f"<h1>Thank you, {name}! Please find your seat.</h1>"
#     except Exception as e:
#         app.logger.error(f"Error in select_guest: {e}")
#         return f"An error occurred: {e}"
