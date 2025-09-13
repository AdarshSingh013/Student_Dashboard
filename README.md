# Student Dashboard Web Application

A professional-grade Student Dashboard Web Application built with Flask, MySQL, HTML, CSS, and JavaScript, featuring two distinct user roles: Admin and Student. The application provides a clean, modern UI with responsive design and interactive user experience.

## 🌟 Features

### 👩‍💼 Admin Panel
- **Professional Login Page** with secure authentication
- **Dashboard Overview** with key statistics and quick actions
- **Student Management** with add/edit/delete functionality
- **Table View** of student records with sorting and filtering
- **Notice Management** to send notices to specific students, classes, or all students
- **Analytics Dashboard** with interactive charts
- **Data Export** functionality (JSON format)
- **Form Validation** with real-time feedback

### 🎓 Student Dashboard
- **Student Login** using Student ID/Roll Number
- **Personalized Dashboard** with academic overview
- **Profile Summary** with student information
- **Academic Performance** with subject-wise marks and charts
- **Attendance Tracking** with visual progress indicators
- **Notice Board** for important announcements
- **Report Download** functionality (TXT format)

### 🖌 UI/UX Features
- **Modern Design** with clean, professional layout
- **Responsive Design** for mobile, tablet, and desktop
- **Dark/Light Mode Toggle** for user preference
- **Smooth Animations** and transitions
- **Interactive Charts** using Chart.js
- **Card-based Layout** with consistent styling
- **Font Awesome Icons** for enhanced visual appeal

## � Technology Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Database**: MySQL
- **Authentication**: Flask-Login
- **CSS Framework**: Custom CSS with modern design principles

## 📂 Project Structure

```
Student-Dashboard-System/
├── app/                      # Main application package
│   ├── config/               # Configuration files
│   ├── models/               # Database models
│   ├── routes/               # Route definitions
│   ├── static/               # Static files (CSS, JS, images)
│   └── templates/            # HTML templates
├── data/                     # Data files (for development)
├── venv/                     # Python virtual environment
├── .env                      # Environment variables
├── .gitignore                # Git ignore file
├── app.py                    # Application entry point
├── requirements.txt          # Python dependencies
└── run.py                    # Script to run the application
```

## 🚀 Setup and Installation

### Prerequisites

- Python 3.7 or higher
- MySQL server
- Git

### Installation Steps

1. Clone the repository:
   ```
   git clone https://github.com/AdarshSingh013/Student-Dashboard-System.git
   cd Student-Dashboard-System
   ```

2. Create and activate a virtual environment:
   ```
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure MySQL:
   - Create a database named `student_dashboard`
   - Update the `.env` file with your MySQL credentials

5. Initialize the database:
   ```
   python run.py
   ```

6. Run the application:
   ```
   flask run
   ```
   or
   ```
   python run.py
   ```

7. Access the application:
   - Open a web browser and go to `http://localhost:5000`

### Default Credentials

- **Admin**:
  - Username: admin
  - Password: admin123

## 🧑‍💻 Development

1. Make sure you have activated the virtual environment
2. Run the application in development mode:
   ```
   flask run --debug
   ```

## 🔐 Authentication

### Admin Login
- **Username:** `admin`
- **Password:** `admin123`

### Student Login
Use any of the sample student IDs:
- `STU001` - John Doe (Grade 10)
- `STU002` - Jane Smith (Grade 9)
- `STU003` - Mike Johnson (Grade 10)
- `STU004` - Sarah Wilson (Grade 8)
- `STU005` - David Brown (Grade 9)

## 📱 Usage

### For Administrators
1. Select "Administrator" role on the landing page
2. Login with admin credentials
3. Access the admin dashboard with:
   - Student management (add, edit, delete)
   - Notice creation and management
   - Analytics and reporting
   - Data export functionality

### For Students
1. Select "Student" role on the landing page
2. Enter your Student ID to login
3. Access your personalized dashboard with:
   - Academic performance overview
   - Subject-wise marks and grades
   - Attendance records
   - Important notices
   - Profile information

## 🛠 Technical Details

### Technologies Used
- **HTML5** - Semantic structure and accessibility
- **CSS3** - Modern styling with Flexbox/Grid layout
- **JavaScript (ES6+)** - Application logic and interactions
- **Chart.js** - Interactive charts and graphs
- **Font Awesome** - Icon library
- **Google Fonts** - Typography (Poppins)

### Key Features
- **localStorage** for data persistence
- **Responsive Design** with mobile-first approach
- **Progressive Web App** ready
- **No Backend Required** - client-side only
- **Modular JavaScript** architecture
- **Form Validation** and error handling
- **Real-time Updates** and notifications

### Browser Compatibility
- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## 🎨 Customization

### Color Scheme
The application uses CSS custom properties for easy theming:
```css
:root {
    --primary-color: #4f46e5;
    --secondary-color: #06b6d4;
    --accent-color: #f59e0b;
    --success-color: #10b981;
    --error-color: #ef4444;
}
```

### Adding New Features
1. **New Student Fields:** Modify the student object structure in `script.js`
2. **Additional Charts:** Add new Chart.js implementations
3. **Custom Notifications:** Extend the notification system
4. **Export Formats:** Add new export functionality

## 📊 Sample Data

The application comes with pre-loaded sample data including:
- 5 sample students with complete academic records
- 4 sample notices with different target audiences
- Attendance records for the past 30 days
- Subject-wise marks and grades

## 🔧 Development

### Adding New Students
1. Login as admin
2. Navigate to Students section
3. Click "Add Student" button
4. Fill in the required information
5. Save to add to the system

### Sending Notices
1. Login as admin
2. Navigate to Notices section
3. Click "Send Notice" button
4. Choose target audience (All, Class, or Individual)
5. Compose and send the notice

### Data Persistence
All data is automatically saved to localStorage and persists between browser sessions. To reset data, clear browser localStorage or refresh the page (sample data will reload).

## 🚀 Future Enhancements

Potential features for future development:
- **Backend Integration** with REST API
- **User Authentication** with JWT tokens
- **Email Notifications** for notices
- **PDF Report Generation** with jsPDF
- **Advanced Analytics** with more chart types
- **Bulk Data Import/Export** (CSV, Excel)
- **Real-time Notifications** with WebSocket
- **Mobile App** with React Native/Flutter

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For support or questions, please open an issue in the project repository.

---

**Built with ❤️ for educational institutions and student management.**
