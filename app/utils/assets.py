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
        
            'entrepreneurship_js': Bundle(
                'js/common.js',
                output='gen/entrepreneurship.js'),
        
            'entrepreneurship_css': Bundle(
                'css/bootstrap-extensions.css',
                'css/common.css',
                output='gen/entrepreneurship.css'),
        
            'gallery_js': Bundle(
                'js/jquery.min.js',
                'js/jquery.nanogallery2.min.js',
                'js/common.js',
                'js/gallery.js',
                output='gen/gallery.js'),
        
            'gallery_css': Bundle(
                'css/bootstrap-extensions.css',
                'css/nanogallery2.min.css',
                'css/common.css',
                output='gen/gallery.css'),
        
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
         
        env.register(bundles)
        return bundles

if __name__ == '__main__':
    bundles = init_assets()
    for bundleKey in bundles:
        bundles[bundleKey].build()
