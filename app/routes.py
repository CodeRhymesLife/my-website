from flask import render_template, url_for

from app import app


@app.route('/cv')
def cv():
    return render_template('cv.html', title='CV')

@app.route('/entrepreneurship')
def entrepreneurship():
    return render_template('entrepreneurship.html', title='Entrepreneurship')

@app.route('/hmd-navigation')
def hmdNavigation():
    return render_template(
        'hmd-navigation.html',
        title='HMD Navigation',
        videos=[
            'https://drive.google.com/file/d/1Pss_oNLa64zbB8OdCJjUB1zj7Vb4KNYv/preview',
            'https://drive.google.com/file/d/1lUXK06cWIYIcm8cMJcoedTnnCohcmmdV/preview',
        ]
    )

@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html',
        title='About Me',
        interests=[
            {
                'name': 'Software Engineering',
                'glyphicon': 'glyphicon-console',
                'url': url_for('software'),
            },
            {
                'name': 'HMD Navigation',
                'glyphicon': 'glyphicon-sunglasses',
                'url': url_for('hmdNavigation'),
            },
            {
                'name': 'Entrepreneurship',
                'glyphicon': 'glyphicon-globe',
                'url': url_for('entrepreneurship'),
            },
        ]
    )

@app.route('/software')
def software():
    return render_template('software.html', title='Software')

