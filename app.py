"""
Student Dashboard System - Main Flask Application

This is the main entry point for the Flask application. It initializes the app
and registers all the blueprints.
"""

from flask import Flask
from app.config.config import Config
from flask_mysqldb import MySQL
from flask_login import LoginManager

# Initialize extensions
mysql = MySQL()
login_manager = LoginManager()

def create_app(config_class=Config):
    """Create and configure the Flask application"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions with app
    mysql.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    # Register blueprints
    from app.routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from app.routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from app.routes.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')
    
    from app.routes.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    
    from app.routes.student import student as student_blueprint
    app.register_blueprint(student_blueprint, url_prefix='/student')
    
    @app.route('/test')
    def test_route():
        """Test route to verify the app is running"""
        return 'Flask application is running correctly!'
        
    return app