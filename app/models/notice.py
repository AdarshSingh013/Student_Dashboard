"""
Notice model for database operations
"""

from app import mysql
import pymysql
from datetime import datetime

class Notice:
    """Notice model class"""
    
    @staticmethod
    def get_all():
        """Get all notices"""
        cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM notices ORDER BY created_at DESC')
        notices = cursor.fetchall()
        cursor.close()
        return notices
    
    @staticmethod
    def get_by_id(notice_id):
        """Get a notice by ID"""
        cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM notices WHERE id = %s', (notice_id,))
        notice = cursor.fetchone()
        cursor.close()
        return notice
    
    @staticmethod
    def create(title, content):
        """Create a new notice"""
        cursor = mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO notices (title, content, created_at) VALUES (%s, %s, %s)',
            (title, content, datetime.now())
        )
        mysql.connection.commit()
        notice_id = cursor.lastrowid
        cursor.close()
        return notice_id
    
    @staticmethod
    def update(notice_id, title, content):
        """Update a notice"""
        cursor = mysql.connection.cursor()
        cursor.execute(
            'UPDATE notices SET title = %s, content = %s WHERE id = %s',
            (title, content, notice_id)
        )
        mysql.connection.commit()
        cursor.close()
        return True
    
    @staticmethod
    def delete(notice_id):
        """Delete a notice"""
        cursor = mysql.connection.cursor()
        cursor.execute('DELETE FROM notices WHERE id = %s', (notice_id,))
        mysql.connection.commit()
        cursor.close()
        return True