from flask import Flask, request, render_template
import logging
import serial
# import serial
import time

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.DEBUG)


# A list of guests and their unique LED numbers
guests = {
    "Alice": 1,
    "Bob": 2,
    "Charlie": 3,
    "Emily":4,
    "Henry":5,
    "Ian Cruickshank":6,
    "Ian Daniells":7,
    "Sarah Martin":8
}

@app.route('/')
def index():
    try:
        return render_template('index.html', guests=guests.keys())
    except Exception as e:
        app.logger.error(f"Error rendering template: {e}")
        return f"An error occurred: {e}"

@app.route('/select', methods=['POST'])
def select_guest():
    try:
        name = request.form['name']
        led_number = guests.get(name, -1)
        if led_number != -1:
            # Send the unique number via serial to the Pico
            print (f'seat number is {led_number}')
            # ser.write(f"{led_number}\n".encode())
        return f"<h1>Thank you, {name}! Please find your seat.</h1>"
    except Exception as e:
        app.logger.error(f"Error in select_guest: {e}")
        return f"An error occurred: {e}"

if __name__ == '__main__':
    while True:
        app.run(host='0.0.0.0', port=5000)

