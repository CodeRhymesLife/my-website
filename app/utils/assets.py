from flask_assets import Bundle, Environment
from os import path

def init_assets(app):
    with app.app_context():
        env = Environment(app)
        env.load_path = [path.join(path.dirname(__file__), '..', 'static')]

        # App Enging doesn't support automatic building
        # so only auto build if in debug mode
        env.auto_build = app.debug
        app.logger.info('auto_build set to {}'.format(
            env.auto_build
        ))

        # Make sure this file is shipped
        env.manifest = 'file'

        bundles = {
        
            'cv_js': Bundle(
                'js/common.js',
                'js/cv.js',
                output='gen/cv.js'),
        
            'cv_css': Bundle(
                'css/bootstrap-extensions.css',
                'css/common.css',
                'css/cv.css',
                output='gen/cv.css'),
        
            'aboutMe_js': Bundle(
                'js/common.js',
                output='gen/aboutMe.js'),
        
            'aboutMe_css': Bundle(
                'css/bootstrap-extensions.css',
                'css/common.css',
                'css/aboutMe.css',
                output='gen/aboutMe.css'),

            'index_js': Bundle(
                'js/common.js',
                output='gen/index.js'),
        
            'index_css': Bundle(
                'css/bootstrap-extensions.css',
                'css/common.css',
                'css/index.css',
                output='gen/index.css'),
        }
         
        env.register(bundles)
        return bundles

if __name__ == '__main__':
    from flask import Flask

    app = Flask("asset_builder")
    bundles = init_assets(app)
    for bundleKey in bundles:
        bundles[bundleKey].build()
