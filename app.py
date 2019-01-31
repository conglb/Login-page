from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)
Bootstrap(app)

# database init
db_path = os.path.join(os.path.dirname(__file__), 'app.db')
db_uri = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri


@app.route('/')
def homepage(name = ''):
    return render_template('homepage.html', name = name)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/forget-password')
def forgot_password():
    return render_template('forget-password.html')
