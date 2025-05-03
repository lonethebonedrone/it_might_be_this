from app import app
from flask import render_template

# This is for rendering the home page
@app.route('/')
def index():
    return render_template('index.html')

# Here's the basics for making any new route
# It's a good idea to use the same name/word, and same capitalization conventions
# Add a route name, function name, and html template name 
# (then go make that html template)
@app.route('/projectaboutus')
def projectaboutus():
    return render_template('projectaboutus.html')

@app.route('/projectpage')
def projectpage():
    return render_template('projectpage.html')

@app.route('/projectquiz')
def projectquiz():
    return render_template('projectquiz.html')

@app.route('/review')
def projectaboutus():
    return render_template('review.html')
