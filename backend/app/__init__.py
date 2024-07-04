from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from .routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

@login_manager.user_loader
def load_user(user_id):
    from .models import User  # Import here to avoid circular import
    return User.query.get(int(user_id))

login_manager.login_view = 'api.login'
