import flask
import requests 

print('... loading flask app ...', flask.__version__)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


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