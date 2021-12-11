from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)

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