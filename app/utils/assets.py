from flask_assets import Bundle, Environment
from .. import app

bundles = {

    'cv_js': Bundle(
        'js/common.js',
        output='gen/cv.js'),

    'cv_css': Bundle(
        'css/bootstrap-extensions.css',
        'css/common.css',
        'css/cv.css',
        output='gen/cv.css'),

    'entrepreneurship_js': Bundle(
        'js/common.js',
        output='gen/entrepreneurship.js'),

    'entrepreneurship_css': Bundle(
        'css/bootstrap-extensions.css',
        'css/common.css',
        output='gen/entrepreneurship.css'),

    'hmd-navigation_js': Bundle(
        'js/common.js',
        output='gen/hmd-navigation.js'),

    'hmd-navigation_css': Bundle(
        'css/bootstrap-extensions.css',
        'css/common.css',
        'css/hmd-navigation.css',
        output='gen/hmd-navigation.css'),

    'index_js': Bundle(
        'js/common.js',
        output='gen/index.js'),

    'index_css': Bundle(
        'css/bootstrap-extensions.css',
        'css/common.css',
        'css/index.css',
        output='gen/index.css'),

    'software_js': Bundle(
        'js/common.js',
        output='gen/software.js'),

    'software_css': Bundle(
        'css/bootstrap-extensions.css',
        'css/common.css',
        'css/software.css',
        output='gen/software.css'),
}

assets = Environment(app)

assets.register(bundles)
