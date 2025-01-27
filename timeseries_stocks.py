import pandas as pd 
import numpy as np
from twelvedata import TDClient
import sqlite3

api_key = '7b6bcde9fd6f474d96b8031f19334af2'
td = TDClient(apikey=api_key)

def timeseries(s,interval='1min'):
    t = (td.time_series(symbol=s,interval=interval,outputsize=5000)).as_pandas()
    storedata(t)

def storedata(parsed_data):
    if parsed_data:
        try:
            # Dump data into database
            conn = sqlite3.connect('stock_db.db')
            cursor = conn.cursor()

# Create table if not exists
            cursor.execute('''CREATE TABLE IF NOT EXISTS nseData
                  (id INTEGER PRIMARY KEY,
                  timestamp INTEGER,
                  date TEXT,
                  identifier TEXT,
                  name TEXT,
                  grapthData TEXT)''')
            # Get the current timestamp
            timestamp = int(time.time())
            today_date = datetime.date.today().strftime('%Y-%m-%d')
            # Insert data into table
            cursor.execute("INSERT INTO nseData (timestamp, date, identifier, name, grapthData) VALUES (?, ?, ?, ?, ?)",
               (timestamp, today_date, parsed_data['identifier'], parsed_data['name'], json.dumps(parsed_data['grapthData'])))
            # Commit changes and close connection
            conn.commit()
            conn.close()
            print("Data has been dumped into the database.")
        except Exception as e:
            print("Error occurred while storing data in the database:", e)


if __name__ == "__main__":
    with open('stocks\stocks.txt', 'r') as file: 
        stocks = file.read()
        stocks = stocks.split('\n')
        for s in stocks:
            timeseries(s)


