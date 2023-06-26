import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"

coins = [
    {'name': 'Bitcoin', 'symbol': 'BTC', 'worth': ''},
    {'name': 'Tesla', 'symbol': 'TSLA', 'worth': ''}
]


def get_realtime_price(symbol):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if 'Global Quote' in data and '05. price' in data['Global Quote']:
        return data['Global Quote']['05. price']
    else:
        return 'N/A'


@app.route('/')
def index():
    return render_template('index.html', coins=coins)


@app.route('/get_realtime_price')
def get_realtime_price_route():
    symbol = request.args.get('symbol')
    price = get_realtime_price(symbol)
    return jsonify(price)


if __name__ == '__main__':
    app.run(debug=True)
