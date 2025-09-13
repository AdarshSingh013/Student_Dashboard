"""
Main routes for the application
"""

from flask import Blueprint, render_template, redirect, url_for

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():
    """Route for the home page"""
    return render_template('index.html')