import os

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/test')
def test_page():
    return render_template('test_page.html')

if __name__ == "__main__":
    app.run()
