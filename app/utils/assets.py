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
}

assets = Environment(app)

assets.register(bundles)
