import machine
import time
import lcd128_32_fonts
from lcd128_32 import lcd128_32
# from stock_data import get_stock_data
#i2c config
clock_pin = 21
data_pin = 20
bus = 0
i2c_addr = 0x3f
use_i2c = True

def get_stock_data():

    # # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    # url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IAG&interval=5min&apikey=6S7LUTV6SNQY0UQN'
    # r = requests.get(url)
    # data = r.json()
    # item = data['Meta Data']['2. Symbol']
    item = 'AAPL is good'
    return (item)

def scan_for_devices():
    i2c = machine.I2C(bus,sda=machine.Pin(data_pin),scl=machine.Pin(clock_pin))
    devices = i2c.scan()
    if devices:
        for d in devices:
            print(hex(d))
    else:
        print('no i2c devices')
if use_i2c:
    scan_for_devices()
    lcd = lcd128_32(data_pin, clock_pin, bus, i2c_addr)
text = get_stock_data()
lcd.Clear()
lcd.Cursor(0, 4)
lcd.Display(str(text))
lcd.Cursor(1, 4)
lcd.Display("whoop whoop")
lcd.Cursor(2, 4)
lcd.Display("yee haa")
lcd.Cursor(3, 4)
lcd.Display("yippee")


"""
while True:
    scan_for_devices()
    time.sleep(0.5)
"""