import flask
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests 


print('... loading flask app ...', flask.__version__)

app = Flask(__name__)
app.config["DEBUG"] = True
# relative path to the database file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    complete = db.Column(db.Boolean)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    # def __init__(self, title, complete, content):
    #     self.title = title
    #     self.content = content
    #     self.complete = complete
    def __repr__(self):
        return '<Task %r>' % self.id

db.create_all()
print(db)

@app.route('/', methods=['GET', 'POST']) # route decorators to allow for GET and POST requests
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all() # get all tasks from the database
        return render_template('index.html', tasks=tasks)
    # Flask knows to look in templates folder.

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
   return ''

@app.route('/hello')
def hello():
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