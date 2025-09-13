// Student Dashboard Application - Main JavaScript File

// Global Variables
let currentUser = null;
let currentRole = null;
let students = [];
let notices = [];
let currentStudent = null;

// Initialize application
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

// Application Initialization
async function initializeApp() {
    await loadData();
    setupEventListeners();
    initializeTheme();
    
    // Check if user is already logged in via server-side session
    // The Flask backend handles authentication now
}

// Load data from API
async function loadData() {
    try {
        // Load students data from API
        const studentsResponse = await fetch('/api/students');
        if (studentsResponse.ok) {
            students = await studentsResponse.json();
        }
        
        // Load notices data from API
        const noticesResponse = await fetch('/api/notices');
        if (noticesResponse.ok) {
            notices = await noticesResponse.json();
        }
        
        // If we're on the student dashboard, get the current student's data
        if (document.querySelector('.student-dashboard')) {
            const studentId = document.querySelector('.student-dashboard').dataset.studentId;
            if (studentId) {
                const studentResponse = await fetch(`/api/students/${studentId}`);
                if (studentResponse.ok) {
                    currentStudent = await studentResponse.json();
                }
            }
        }
    } catch (error) {
        console.error('Error loading data from API:', error);
    }
}

// Setup event listeners
function setupEventListeners() {
    // Password toggle
    const togglePasswordButtons = document.querySelectorAll('.toggle-password');
    if (togglePasswordButtons) {
        togglePasswordButtons.forEach(button => {
            button.addEventListener('click', function() {
                const passwordField = document.getElementById(this.getAttribute('data-toggle'));
                if (passwordField) {
                    if (passwordField.type === 'password') {
                        passwordField.type = 'text';
                        this.innerHTML = '<i class="fas fa-eye-slash"></i>';
                    } else {
                        passwordField.type = 'password';
                        this.innerHTML = '<i class="fas fa-eye"></i>';
                    }
                }
            });
        });
    }
    
    // Theme toggle
    const themeToggle = document.getElementById('themeToggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
    }
    
    // Add other event listeners for your application here
}

// Toggle password visibility
function togglePassword(inputId) {
    const passwordInput = document.getElementById(inputId);
    const toggleButton = passwordInput.nextElementSibling;
    
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        toggleButton.innerHTML = '<i class="fas fa-eye-slash"></i>';
    } else {
        passwordInput.type = 'password';
        toggleButton.innerHTML = '<i class="fas fa-eye"></i>';
    }
}

// Initialize theme
function initializeTheme() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.setAttribute('data-theme', 'dark');
        const themeToggle = document.getElementById('themeToggle');
        if (themeToggle) {
            themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
            themeToggle.setAttribute('title', 'Switch to Light Mode');
        }
    }
}

// Toggle theme (light/dark)
function toggleTheme() {
    const currentTheme = document.body.getAttribute('data-theme');
    const themeToggle = document.getElementById('themeToggle');
    
    if (currentTheme === 'dark') {
        document.body.removeAttribute('data-theme');
        localStorage.setItem('theme', 'light');
        if (themeToggle) {
            themeToggle.innerHTML = '<i class="fas fa-moon"></i>';
            themeToggle.setAttribute('title', 'Switch to Dark Mode');
        }
    } else {
        document.body.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
        if (themeToggle) {
            themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
            themeToggle.setAttribute('title', 'Switch to Light Mode');
        }
    }
}