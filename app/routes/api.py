"""
API routes for the application
"""

from flask import Blueprint, jsonify, request
from app import mysql
import pymysql

api = Blueprint('api', __name__)

@api.route('/students', methods=['GET'])
def get_students():
    """Get all students"""
    cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    cursor.close()
    return jsonify(students)

@api.route('/students/<string:student_id>', methods=['GET'])
def get_student(student_id):
    """Get a specific student by ID"""
    cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM students WHERE id = %s', (student_id,))
    student = cursor.fetchone()
    cursor.close()
    
    if student:
        return jsonify(student)
    else:
        return jsonify({'error': 'Student not found'}), 404

@api.route('/students/<string:student_id>/marks', methods=['GET'])
def get_student_marks(student_id):
    """Get marks for a specific student"""
    cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM marks WHERE student_id = %s', (student_id,))
    marks = cursor.fetchall()
    cursor.close()
    
    return jsonify(marks)

@api.route('/notices', methods=['GET'])
def get_notices():
    """Get all notices"""
    cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM notices ORDER BY created_at DESC')
    notices = cursor.fetchall()
    cursor.close()
    return jsonify(notices)

@api.route('/notices', methods=['POST'])
def create_notice():
    """Create a new notice"""
    data = request.get_json()
    
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    
    cursor = mysql.connection.cursor()
    cursor.execute(
        'INSERT INTO notices (title, content) VALUES (%s, %s)',
        (data['title'], data['content'])
    )
    mysql.connection.commit()
    notice_id = cursor.lastrowid
    cursor.close()
    
    return jsonify({'id': notice_id, 'message': 'Notice created successfully'}), 201