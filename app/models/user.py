"""
User model for authentication
"""

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import mysql, login_manager
import pymysql

class User(UserMixin):
    """User class for authentication"""
    
    def __init__(self, id, username, role, student_id=None):
        self.id = id
        self.username = username
        self.role = role
        self.student_id = student_id
    
    @staticmethod
    def get_admin_by_username(username):
        """Get an admin user by username"""
        cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s AND role = "admin"', (username,))
        user_data = cursor.fetchone()
        cursor.close()
        
        if user_data:
            return User(
                id=user_data['id'],
                username=user_data['username'],
                role='admin'
            )
        return None
    
    @staticmethod
    def get_student_by_id(student_id):
        """Get a student user by student ID"""
        cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT u.id, u.username, s.id as student_id FROM users u JOIN students s ON u.student_id = s.id WHERE s.id = %s', (student_id,))
        user_data = cursor.fetchone()
        cursor.close()
        
        if user_data:
            return User(
                id=user_data['id'],
                username=user_data['username'],
                role='student',
                student_id=user_data['student_id']
            )
        return None
    
    @staticmethod
    def get_by_id(user_id):
        """Get a user by ID"""
        cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
        user_data = cursor.fetchone()
        cursor.close()
        
        if user_data:
            return User(
                id=user_data['id'],
                username=user_data['username'],
                role=user_data['role'],
                student_id=user_data.get('student_id')
            )
        return None
    
    def check_password(self, password):
        """Check password against the stored hash"""
        cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT password_hash FROM users WHERE id = %s', (self.id,))
        user_data = cursor.fetchone()
        cursor.close()
        
        if user_data:
            return check_password_hash(user_data['password_hash'], password)
        return False

@login_manager.user_loader
def load_user(user_id):
    """Load user for Flask-Login"""
    return User.get_by_id(user_id)