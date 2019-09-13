from flask import render_template, url_for

from app import app

@app.route('/')
@app.route('/index')
def index():
    projects = [
        {
            'title': 'Telerobotics',
            'type': 'Album',
            'img': 'static/images/tiles/telerobotics.png',
            'url': 'https://photos.app.goo.gl/g1MVGr28j87cH8am7',
        },
        {
            'title': 'VR Guidance',
            'type': 'Article',
            'img': 'static/images/tiles/catheye.png',
            'url': 'https://medium.com/@ryanjameshealth/a-virtual-reality-surgical-guidance-system-9621e4b7b9ea',
        },
        {
            'title': 'VR Planning',
            'type': 'Video',
            'img': 'static/images/tiles/bosc.png',
            'url': 'https://www.youtube.com/watch?v=H1NS6GyttLg',
        },
        {
            'title': 'Model Service',
            'type': 'GitHub',
            'img': 'static/images/tiles/3d-model-service.png',
            'url': '',
        },
        {
            'title': 'Simulation',
            'type': 'Album',
            'img': 'static/images/tiles/gallery.png',
            'url': 'https://photos.app.goo.gl/KKUFqXMm7V1jNt5J8',
        },
    ]

    isReady = lambda p: 'url' in p.keys() and p['url']

    return render_template(
        'index.html',
        title='Ryan James',
        readyProjects=filter(isReady, projects),
        comingSoonProjects=filter(lambda p: not isReady(p), projects),
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
