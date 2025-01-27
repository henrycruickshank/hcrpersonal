import numpy as np
import os
from twelvedata import TDClient
import pandas as pd
import time
import sqlite3
from datetime import datetime


api_key = '7b6bcde9fd6f474d96b8031f19334af2'
td = TDClient(apikey=api_key)

def main(stocks):
    while True:
        current_time = time.time()  # Get the current time in seconds since the Epoch
        readable_time = time.strftime('%H:%M:%S', time.gmtime(current_time % 86400))
        print(readable_time)
        # if readable_time.endswith(':00') or readable_time.endswith(':30'):
        next_run = current_time + 60  # Schedule the next run in 30 seconds
        # Run the task at the start
        monitor(stocks)

        # Calculate sleep time until the next run
        sleep_time = next_run - time.time()

        time.sleep(sleep_time)

        # Run the task at the 60-second mark
        print (readable_time)
        monitor(stocks)

        # Calculate the next run time for the minute mark
        next_run += 60
        sleep_time = next_run - time.time()
        time.sleep(sleep_time)

def database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('stocks_db.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Create a table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS stocks (
        id INTEGER PRIMARY KEY,
        symbol TEXT NOT NULL,
        price REAL NOT NULL,
        date TEXT NOT NULL
    )
    ''')
    # Commit changes and close the connection
    conn.commit()
    conn.close()


def get_info(s):
    info = td.symbol_search(symbol=s).as_json()[0]
    info['market_open'] = td.get_market_state(exchange = info['exchange']).as_json()[0]['is_market_open'] 
    return info

def get_live_price(s,info):
    p = td.price(
        symbol=s
    )   
    data = p.as_json()
    price = round((float(data['price'])),2)
    print(f"{s} price is {price} {info['currency']}")

def get_closing_price(s,info):
    eod= td.eod(
        symbol=s
    )
    data = eod.as_pandas()
    data['timestamp'] = datetime.utcfromtimestamp(int(data['timestamp'])).strftime('%Y-%m-%d %H:%M:%S')
    return data

def monitor(stocks):
    for ind,s in enumerate(stocks):
        info = get_info(s)
        if info['market_open'] == True:
            price = get_live_price(s,info)
        else:
            closing_price = get_closing_price(s,info)
        

    


if __name__ == "__main__":
    # file_path = os.path.abspath("webpage.html")
    # webbrowser.open(f"file://{file_path}")
    with open('stocks\stocks.txt', 'r') as file: 
        stocks = file.read()
        stocks = stocks.split('\n')
    while True:
        main(stocks)
    # database()