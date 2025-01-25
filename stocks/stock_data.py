import webbrowser
import os
from twelvedata import TDClient
import pandas as pd
import time
import json

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
        request_data(stocks)

        # Calculate sleep time until the next run
        sleep_time = next_run - time.time()

        time.sleep(sleep_time)

        # Run the task at the 60-second mark
        print (readable_time)
        request_data(stocks)

        # Calculate the next run time for the minute mark
        next_run += 60
        sleep_time = next_run - time.time()
        time.sleep(sleep_time)

def get_info(s):
    info = td.symbol_search(symbol=s).as_json()[0]
    info['market_open'] = td.get_market_state(exchange = info['exchange']).as_json()[0]['is_market_open'] 
    return info

def request_data(stocks):
    # Initialize client - apikey parameter is requiered
    for ind,s in enumerate(stocks):
        info = get_info(s)
        if info['market_open'] == False:
        # if status is closed - gets end of day price for stocks
            eod= td.eod(
                symbol=s
            )
            data = eod.as_pandas()
            print(f"{s} closing price {float(data.close.values[0].round(2))} {info['currency']}")
        else: #gets live price 
            p = td.price(
                symbol=s
            )   
            data = p.as_json()
            price = round((float(data['price'])),2)
            print(f"{s} price is {price} {info['currency']}")

if __name__ == "__main__":
    # file_path = os.path.abspath("webpage.html")
    # webbrowser.open(f"file://{file_path}")
    with open('stocks.txt', 'r') as file: 
        stocks = file.read()
        stocks = stocks.split('\n')
    while True:
        main(stocks)