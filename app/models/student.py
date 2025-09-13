"""
Student model for database operations
"""

from app import mysql
import pymysql

class Student:
    """Student model class"""
    
    @staticmethod
    def get_all():
        """Get all students"""
        cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()
        cursor.close()
        return students
    
    @staticmethod
    def get_by_id(student_id):
        """Get a student by ID"""
        cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM students WHERE id = %s', (student_id,))
        student = cursor.fetchone()
        cursor.close()
        return student
    
    @staticmethod
    def create(student_data):
        """Create a new student"""
        cursor = mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO students (id, name, class, email, phone, address) VALUES (%s, %s, %s, %s, %s, %s)',
            (
                student_data['id'],
                student_data['name'],
                student_data['class'],
                student_data['email'],
                student_data['phone'],
                student_data['address']
            )
        )
        mysql.connection.commit()
        cursor.close()
        return student_data['id']
    
    @staticmethod
    def update(student_id, student_data):
        """Update a student"""
        cursor = mysql.connection.cursor()
        cursor.execute(
            'UPDATE students SET name = %s, class = %s, email = %s, phone = %s, address = %s WHERE id = %s',
            (
                student_data['name'],
                student_data['class'],
                student_data['email'],
                student_data['phone'],
                student_data['address'],
                student_id
            )
        )
        mysql.connection.commit()
        cursor.close()
        return True
    
    @staticmethod
    def delete(student_id):
        """Delete a student"""
        cursor = mysql.connection.cursor()
        cursor.execute('DELETE FROM students WHERE id = %s', (student_id,))
        mysql.connection.commit()
        cursor.close()
        return True
    
    @staticmethod
    def get_marks(student_id):
        """Get marks for a student"""
        cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM marks WHERE student_id = %s', (student_id,))
        marks = cursor.fetchall()
        cursor.close()
        return marks
    
    @staticmethod
    def update_marks(student_id, subject, obtained, total, grade):
        """Update marks for a student"""
        cursor = mysql.connection.cursor()
        cursor.execute(
            '''
            INSERT INTO marks (student_id, subject, obtained, total, grade) 
            VALUES (%s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE obtained = %s, total = %s, grade = %s
            ''',
            (student_id, subject, obtained, total, grade, obtained, total, grade)
        )
        mysql.connection.commit()
        cursor.close()
        return True
        
    @staticmethod
    def update_attendance(student_id, attendance):
        """Update attendance for a student"""
        cursor = mysql.connection.cursor()
        cursor.execute(
            'UPDATE students SET attendance = %s WHERE id = %s',
            (attendance, student_id)
        )
        mysql.connection.commit()
        cursor.close()
        return True