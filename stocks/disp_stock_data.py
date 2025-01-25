from machine import I2C, Pin
import lcd_api
import utime
from stock_data import get_stock_data

i2c = I2C(0,sda=Pin(20),scl=Pin(21),freq=400000)

def display_stock_data():
    stock_data = get_stock_data()
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("stock price")
    lcd.move_to(0,1)
    lcd.putstr(stock_data)

while True:
    display_stock_data
