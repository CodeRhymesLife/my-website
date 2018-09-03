from flask import render_template

from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='About Me')

@app.route('/software')
def software():
    return render_template('software.html', title='Software')

@app.route('/healthcare')
def healthcare():
    return render_template('healthcare.html', title='Healthcare')

@app.route('/entrepreneurship')
def entrepreneurship():
    return render_template('entrepreneurship.html', title='Entrepreneurship')

