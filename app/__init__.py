from flask import Flask, Response
from flask_cors import CORS


class MyResponse(Response):
    default_mimetype = 'application/xml'


# http://flask.pocoo.org/docs/0.10/patterns/appfactories/
def create_app(config_filename):
    app = Flask(__name__, static_url_path='', static_folder='../static', template_folder='../static')

    app.config.from_object(config_filename)
    # app.response_class = MyResponse

    from app.users.models import db
    db.init_app(app)

    # Blueprints
    from app.auth.views import auth_bp
    from app.users.views import users_bp
    from app.schools.views import schools_bp
    from app.meals.views import meals_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(users_bp, url_prefix='/api/users')
    app.register_blueprint(schools_bp, url_prefix='/api/schools')
    app.register_blueprint(meals_bp, url_prefix='/api/meals')

    CORS(app)
    return app
