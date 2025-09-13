"""
Student routes for the application
"""

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import mysql
import pymysql

student = Blueprint('student', __name__)

@student.route('/dashboard')
@login_required
def dashboard():
    """Student dashboard route"""
    if current_user.role != 'student':
        flash('Access denied. Student privileges required.', 'error')
        return redirect(url_for('main.index'))
    
    # Get student details
    cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM students WHERE id = %s', (current_user.student_id,))
    student_data = cursor.fetchone()
    
    # Get student marks
    cursor.execute('''
        SELECT subject, obtained, total, grade 
        FROM marks 
        WHERE student_id = %s
    ''', (current_user.student_id,))
    marks = cursor.fetchall()
    
    # Get notices
    cursor.execute('SELECT * FROM notices ORDER BY created_at DESC LIMIT 5')
    notices = cursor.fetchall()
    
    cursor.close()
    
    return render_template('student.html', 
                          student=student_data, 
                          marks=marks, 
                          notices=notices)