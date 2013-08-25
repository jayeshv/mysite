import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

# @app.route('/test')
# def test_page():
#     return render_template('test.html')

# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('page_not_found.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
