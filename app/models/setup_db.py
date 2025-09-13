"""
Database setup script for creating MySQL tables
"""

from app import create_app, mysql

def setup_database():
    """Create database tables if they don't exist"""
    app = create_app()
    with app.app_context():
        cursor = mysql.connection.cursor()
        
        # Create users table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(100) NOT NULL UNIQUE,
            password_hash VARCHAR(255) NOT NULL,
            role ENUM('admin', 'student') NOT NULL,
            student_id VARCHAR(10) UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Create students table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id VARCHAR(10) PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            class VARCHAR(20) NOT NULL,
            email VARCHAR(100) UNIQUE,
            phone VARCHAR(20),
            address TEXT,
            attendance FLOAT DEFAULT 0,
            average FLOAT DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Create marks table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS marks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            student_id VARCHAR(10) NOT NULL,
            subject VARCHAR(50) NOT NULL,
            obtained FLOAT NOT NULL,
            total FLOAT NOT NULL,
            grade VARCHAR(5),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
            UNIQUE KEY (student_id, subject)
        )
        ''')
        
        # Create notices table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS notices (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Create initial admin user if not exists
        cursor.execute('SELECT COUNT(*) FROM users WHERE role = "admin"')
        admin_count = cursor.fetchone()[0]
        
        if admin_count == 0:
            from werkzeug.security import generate_password_hash
            admin_password_hash = generate_password_hash('admin123')
            cursor.execute(
                'INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)',
                ('admin', admin_password_hash, 'admin')
            )
        
        mysql.connection.commit()
        cursor.close()
        
        print("Database setup completed successfully!")

if __name__ == '__main__':
    setup_database()