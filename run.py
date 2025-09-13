"""
Run the Flask application
"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    # Setup database tables
    with app.app_context():
        from app.models.setup_db import setup_database
        setup_database()
    
    # Run the application
    app.run(host='0.0.0.0', port=5000, debug=True)