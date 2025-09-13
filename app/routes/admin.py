"""
Admin routes for the application
"""

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app import mysql
import pymysql

admin = Blueprint('admin', __name__)

@admin.route('/dashboard')
@login_required
def dashboard():
    """Admin dashboard route"""
    if current_user.role != 'admin':
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('main.index'))
    
    # Get all students for admin dashboard
    cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    cursor.close()
    
    return render_template('admin.html', students=students)

@admin.route('/add-student', methods=['GET', 'POST'])
@login_required
def add_student():
    """Add a new student route"""
    if current_user.role != 'admin':
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        # Get form data
        student_id = request.form.get('student_id')
        name = request.form.get('name')
        class_name = request.form.get('class')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        
        # Insert into database
        cursor = mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO students (id, name, class, email, phone, address) VALUES (%s, %s, %s, %s, %s, %s)',
            (student_id, name, class_name, email, phone, address)
        )
        mysql.connection.commit()
        cursor.close()
        
        flash('Student added successfully', 'success')
        return redirect(url_for('admin.dashboard'))
    
    return render_template('add_student.html')

@admin.route('/edit-student/<string:student_id>', methods=['GET', 'POST'])
@login_required
def edit_student(student_id):
    """Edit student route"""
    if current_user.role != 'admin':
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('main.index'))
    
    # Get student data
    cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM students WHERE id = %s', (student_id,))
    student = cursor.fetchone()
    cursor.close()
    
    if not student:
        flash('Student not found', 'error')
        return redirect(url_for('admin.dashboard'))
    
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        class_name = request.form.get('class')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        
        # Update database
        cursor = mysql.connection.cursor()
        cursor.execute(
            'UPDATE students SET name = %s, class = %s, email = %s, phone = %s, address = %s WHERE id = %s',
            (name, class_name, email, phone, address, student_id)
        )
        mysql.connection.commit()
        cursor.close()
        
        flash('Student updated successfully', 'success')
        return redirect(url_for('admin.dashboard'))
    
    return render_template('edit_student.html', student=student)