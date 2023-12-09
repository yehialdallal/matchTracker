from flask import Flask
from config import Config
from app.models.user import User
from app.extensions import db
from app.extensions import login_manager

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize Flask extensions here

    db.init_app(app)
    login_manager.login_view = 'main.index'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints here

    from app.main import bp as main_bp
    from app.auth import bp as auth_bp
    
    app.register_blueprint(main_bp)

    app.register_blueprint(auth_bp , url_prefix='/auth')

    #from app.posts import bp as posts_bp
    #app.register_blueprint(posts_bp, url_prefix='/posts')



    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app