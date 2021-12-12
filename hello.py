from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# create a Flask instance
app = Flask(__name__)
#  add db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# secret key
app.config['SECRET_KEY'] = 'my secret key nobody needs to know'
# initialize the db
db = SQLAlchemy(app)

# Create Model
class Users(db.Model):
    id= db.column(db.Integer,primary_key=True)
    name= db.column(db.String(200), nullable=False)
    email= db.column(db.String(200), nullable=False, unique=True)
    date_added= db.column(db.DateTime, default=datetime.utcnow)

    # Create a string
    def __repr__(self):
        return '<Name %r>' % self.name



# Create form class
class NamerForm(FlaskForm):
    name = StringField('Whats your name', validators=[DataRequired()])
    submit =  SubmitField('Submit')

# create a route decorator
@app.route('/')

# def index():
#     return '<h1>Hello</h1>'

# safe,capitalize,lower,upper,title,trim,striptags

def index():
    first_name= 'Chunks'
    # stuff = 'This is <strong>Bold</strong> Text' ** wotks with safe and striptag
    stuff = 'This is Bold Text'
    fave_pizza = ['pepperoni', 'Ham', 'hawaiian', 33]
    
    return render_template('index.html', 
    first_name=first_name,
    stuff=stuff,
    fave_pizza=fave_pizza
    )

# localhost:5000/user/Chunks
@app.route('/user/<name>')

def user(name):
    return render_template('user.html',user_name=name)

# Create custom error page
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

# Create Name page
@app.route('/name', methods=['GET','POST'])
def name():
    name = None
    form = NamerForm()
    #Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash('Form submitted successfully')
    return render_template('name.html',
    name = name,
    form = form
    )