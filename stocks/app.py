from flask import Flask, request, jsonify, send_file, send_from_directory
import os

app = Flask(__name__)

STOCK_FILE = 'stocks.txt'

# Load stocks from file
def load_stocks():
    if os.path.exists(STOCK_FILE):
        with open(STOCK_FILE, 'r') as file:
            stocks = file.read().splitlines()
    else:
        stocks = []
    return stocks

# Save stocks to file
def save_stocks(stocks):
    with open(STOCK_FILE, 'w') as file:
        file.write('\n'.join(stocks))

@app.route('/')
def home():
    try:
        return send_file('index.html')
    except Exception as e:
        return str(e), 500

@app.route('/stocks', methods=['GET', 'POST'])
def manage_stocks():
    if request.method == 'POST':
        stock = request.json['stock']
        stocks = load_stocks()
        stocks.append(stock)
        save_stocks(stocks)
        return '', 204
    else:
        stocks = load_stocks()
        return jsonify(stocks)

@app.route('/stocks/<int:index>', methods=['DELETE'])
def delete_stock(index):
    stocks = load_stocks()
    if 0 <= index < len(stocks):
        stocks.pop(index)
        save_stocks(stocks)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
