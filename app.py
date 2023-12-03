# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html')  # Update with the correct filename if needed

if __name__ == '__main__':
    app.run(debug=True)
