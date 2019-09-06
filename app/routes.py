from flask import render_template, url_for

from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html',
        title='Ryan James',
        tileRows = [
            [
                {
                    'title': 'Telerobotics',
                    'type': 'Article',
                    'img': 'static/images/tiles/catheye.png',
                    'url': '#',
                },
                {
                    'title': 'Guidance',
                    'type': 'Article',
                    'img': 'static/images/tiles/catheye.png',
                    'url': '#',
                },
            ],
            [
                {
                    'title': 'Planning',
                    'type': 'Video',
                    'img': 'static/images/tiles/bosc.png',
                    'url': '#',
                },
                {
                    'title': 'Model Service',
                    'type': 'GitHub',
                    'img': 'static/images/tiles/catheye.png',
                    'url': '#',
                },
            ],
            [
                {
                    'title': 'Gallery',
                    'type': 'Photos',
                    'img': 'static/images/tiles/catheye.png',
                    'url': url_for('gallery'),
                },
            ],
        ]
    )

@app.route('/aboutMe')
def aboutMe():
    return render_template(
        'aboutMe.html',
        title='About Me'
    )

@app.route('/cv')
def cv():
    return render_template(
        'cv.html',
        title='CV'
    )

@app.route('/gallery')
def gallery():
    return render_template(
        'gallery.html',
        title='Photo Gallery'
    )
