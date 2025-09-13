"""
Authentication routes for the application
"""

from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user, current_user, login_required
from app.models.user import User

auth = Blueprint('auth', __name__)

@auth.route('/login-admin', methods=['GET', 'POST'])
def login_admin():
    """Admin login route"""
    if current_user.is_authenticated and current_user.role == 'admin':
        return redirect(url_for('admin.dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Authenticate admin user (implement with your database later)
        user = User.get_admin_by_username(username)
        
        if user and user.check_password(password):
            login_user(user)
            session['user_role'] = 'admin'
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login-admin.html')

@auth.route('/login-student', methods=['GET', 'POST'])
def login_student():
    """Student login route"""
    if current_user.is_authenticated and current_user.role == 'student':
        return redirect(url_for('student.dashboard'))
    
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        password = request.form.get('password')
        
        # Authenticate student user (implement with your database later)
        user = User.get_student_by_id(student_id)
        
        if user and user.check_password(password):
            login_user(user)
            session['user_role'] = 'student'
            return redirect(url_for('student.dashboard'))
        else:
            flash('Invalid student ID or password', 'error')
    
    return render_template('login-student.html')

@auth.route('/logout')
@login_required
def logout():
    """Logout route"""
    logout_user()
    session.pop('user_role', None)
    return redirect(url_for('main.index'))