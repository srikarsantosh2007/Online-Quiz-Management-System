# Online Quiz Management System

A comprehensive web-based application for creating, managing, and taking online quizzes. Built with Flask, SQLite, and Bootstrap 5 with a modern, iOS-style "liquid glass" UI: frosted-glass cards, glossy gradient buttons, animated aurora background and light/dark mode.

## Features

### For Administrators
- **Dashboard**: Overview of students, quizzes, questions, and attempts with modern gradient cards
- **Student Management**: Add, edit, delete, and search students
- **Quiz Management**: Create, edit, and delete quizzes
- **Question Management**: Add, edit, and delete multiple-choice questions
- **Quiz Assignment**: Assign quizzes to students
- **Results View**: View all quiz attempts and results with percentage badges
- **Reports**: Detailed analytics on student performance and quiz statistics
- **Search & Pagination**: Efficient data navigation

### For Students
- **Registration & Login**: Secure authentication system
- **Dashboard**: Personal overview of available quizzes and attempts with enhanced UI
- **Browse Quizzes**: View all available quizzes with details
- **Take Quizzes**: Interactive quiz interface with enhanced option styling and visual feedback
- **Instant Results**: Immediate feedback with detailed score breakdown
- **Quiz History**: View all previous attempts and results with percentage indicators
- **Profile Management**: Update personal information

## UI Highlights (iOS-style)

- Frosted-glass cards and floating glass navbar (`backdrop-filter` blur)
- Glossy gradient buttons, badges and table headers with press / ripple animations
- Animated aurora background, gradient hero banner, floating icons
- Light / Dark mode toggle (remembers your choice, follows system theme by default)
- Scroll-reveal animations, animated count-up numbers, cursor spotlight on cards
- Quiz page: live countdown timer (auto-submits when time is up), live progress bar, animated option selection
- Result page: animated score ring with confetti for scores of 70% and above
- Smooth page transitions; respects `prefers-reduced-motion`; fully responsive

## Technology Stack

### Backend
- Python 3
- Flask (Web Framework)
- SQLite (Database)
- SQLAlchemy (ORM)
- Werkzeug (Password hashing)

### Frontend
- HTML5
- CSS3
- Bootstrap 5 (UI Framework)
- Jinja2 (Templating)
- Bootstrap Icons
- Custom iOS glass theme (`static/css/ios-theme.css`) and vanilla-JS effects (`static/js/ios-effects.js`)

## Installation

1. **Clone or download the project**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the database**
   ```bash
   python seed_database.py
   ```
   This will create the database and populate it with sample data including:
   - 10 students
   - 5 quizzes (Python, SQL, Web Dev, Data Structures, Computer Networks)
   - 40 questions across all quizzes
   - 100 sample quiz attempts with varying performance
   - 780 detailed question results

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your browser and navigate to: `http://127.0.0.1:5000`cd

## Default Login Credentials

### Admin
- **Username**: admin
- **Password**: admin123

### Students
- **Roll Number**: STU001 to STU010
- **Password**: student123

All 10 student accounts (STU001-STU010) are available with the same password.

## Project Structure

```
Online Quiz Management System/
├── app.py                 # Main Flask application
├── models.py              # Database models
├── seed_database.py       # Database seeding script with enhanced data
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/             # Jinja2 templates with modern UI
│   ├── base.html         # Base template with gradient styling
│   ├── home.html         # Home page
│   ├── about.html        # About page
│   ├── admin_login.html  # Admin login
│   ├── admin_register.html # Admin registration
│   ├── admin_dashboard.html # Admin dashboard with enhanced cards
│   ├── admin_students.html # Student management
│   ├── add_student.html  # Add student form
│   ├── edit_student.html # Edit student form
│   ├── admin_quizzes.html # Quiz management
│   ├── add_quiz.html     # Add quiz form
│   ├── edit_quiz.html    # Edit quiz form
│   ├── quiz_questions.html # Question management
│   ├── add_question.html # Add question form
│   ├── edit_question.html # Edit question form
│   ├── assign_quiz.html  # Assign quiz form
│   ├── admin_results.html # Quiz results
│   ├── admin_reports.html # Reports & analytics
│   ├── student_login.html # Student login
│   ├── student_register.html # Student registration
│   ├── student_dashboard.html # Student dashboard with enhanced UI
│   ├── student_quizzes.html # Available quizzes
│   ├── take_quiz.html    # Take quiz interface with enhanced styling
│   ├── quiz_result.html  # Quiz result details
│   ├── student_attempts.html # Quiz history
│   └── student_profile.html # Student profile
└── static/               # Static files
    ├── css/ios-theme.css  # iOS glass theme, animations, dark mode
    └── js/ios-effects.js  # Count-up, reveal, ripple, theme toggle, confetti
```

## Database Schema

### Tables
- **admins**: Administrator accounts
- **students**: Student accounts
- **quizzes**: Quiz information
- **questions**: Quiz questions
- **quiz_attempts**: Quiz attempt records
- **quiz_results**: Detailed question-wise results

## Usage

### Admin Workflow
1. Login as administrator
2. Add students to the system
3. Create quizzes with title, description, duration, and total marks
4. Add questions to each quiz (MCQ format)
5. Assign quizzes to students (optional - quizzes are available to all by default)
6. Monitor quiz attempts and view results
7. Generate reports for performance analysis

### Student Workflow
1. Register as a new student (or use existing credentials)
2. Login to the system
3. Browse available quizzes
4. Take quizzes by selecting options for each question with enhanced visual feedback
5. Submit quiz to receive instant results
6. View detailed breakdown of answers
7. Track quiz history and performance

## Features Highlights

### Security
- Password hashing using Werkzeug
- Session-based authentication
- Role-based access control (Admin/Student)

### User Experience
- Modern gradient-based UI design
- Responsive Bootstrap 5 design
- Enhanced card styling with hover effects
- Improved button designs with gradient backgrounds
- Better form controls with focus states
- Flash messages for feedback
- Form validation
- Search functionality
- Pagination for large datasets
- Intuitive navigation with breadcrumbs
- Percentage badges for scores (green for 70%+, yellow for 50-69%, red for below 50%)

### Quiz Features
- Multiple Choice Questions (MCQ)
- Configurable quiz duration
- Custom marks per question
- Instant scoring
- Detailed result analysis
- Enhanced quiz-taking interface with visual feedback for selected options

### Sample Data
The seed database script creates comprehensive sample data for testing:
- 10 students with unique roll numbers
- 5 diverse quizzes covering different topics
- 40 questions across all quizzes
- 100 randomized quiz attempts with varying performance levels
- 780 detailed question results for comprehensive reporting

## Development

To add new features or modify existing ones:

1. **Routes**: Add new routes in `app.py`
2. **Models**: Modify database models in `models.py`
3. **Templates**: Create/modify templates in the `templates/` directory
4. **Static Files**: Add CSS/JS/images in the `static/` directory

## License

This project is created for educational purposes.

## Author

Student Mini Project - Online Quiz Management System

## to get to the project location 

cd "D:\PROGRAMMING\INTERNSHIP PROJECT\Onine Quiz Management System"
