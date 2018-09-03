from flask_assets import Bundle, Environment
from .. import app

bundles = {

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
