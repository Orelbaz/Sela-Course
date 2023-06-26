from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    coins = [
        {'name': 'Bitcoin', 'worth': '$30,000'},
        {'name': 'Tesla', 'worth': '$700'},
        # Add more coins here
    ]
    return render_template('index.html', coins=coins)

if __name__ == '__main__':
    app.run(debug=True)
