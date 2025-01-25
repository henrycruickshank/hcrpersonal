import machine
import os
import time

uart = machine.UART(0, baudrate=115200)
os.dupterm(None, 1)  # Disable REPL on USB port

led = machine.Pin(25, machine.Pin.OUT)  # Onboard LED on Pico

while True:
    if uart.any():
        data = uart.read().decode('utf-8')
        led.value(1)  # Turn on the LED
        time.sleep(0.5)  # Keep it on for 0.5 seconds
        led.value(0)  # Turn off the LED
        time.sleep(0.5)  # Wait for 0.5 seconds
