"""
Configuration settings for the application.
"""

import os

class Config:
    """Base configuration class"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-for-development'
    
    # MySQL Configuration
    MYSQL_HOST = os.environ.get('MYSQL_HOST') or 'localhost'
    MYSQL_USER = os.environ.get('MYSQL_USER') or 'root'
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or ''
    MYSQL_DB = os.environ.get('MYSQL_DB') or 'student_dashboard'
    
    # Additional Flask and app settings
    DEBUG = os.environ.get('FLASK_DEBUG') or True
    
class DevelopmentConfig(Config):
    """Development configuration settings"""
    DEBUG = True
    
class ProductionConfig(Config):
    """Production configuration settings"""
    DEBUG = False
    
class TestingConfig(Config):
    """Testing configuration settings"""
    TESTING = True
    DEBUG = True
    MYSQL_DB = 'student_dashboard_test'