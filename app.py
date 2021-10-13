import flask
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import requests 

print('... loading flask app ...', flask.__version__)

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/hello')
def hello():
    # Flask knows to look in templates folder.
    return render_template('index.html')

# @app.route('/', methods=['GET'])
# def home():
#     return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# @app.route('/api/post/<uuid>', methods=['GET', 'POST'])
# def add_message(uuid):
#     content = request.json
#     print(content)
#     return uuid

# @app.route('api/tree-data', methods=['POST'])
# def tree_data():
#     return flask.jsonify({"data": "test"})

app.run()