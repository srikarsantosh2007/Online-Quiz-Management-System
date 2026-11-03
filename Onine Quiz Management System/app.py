from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from functools import wraps
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Import db and models
from models import db, Admin, Student, Quiz, Question, QuizAttempt, QuizResult

# Initialize db with app
db.init_app(app)

# Login required decorators
def admin_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_id' not in session:
            flash('Please login as admin to access this page.', 'danger')
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function

def student_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'student_id' not in session:
            flash('Please login as student to access this page.', 'danger')
            return redirect(url_for('student_login'))
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Admin Routes
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        admin = Admin.query.filter_by(username=username).first()
        if admin and check_password_hash(admin.password, password):
            session['admin_id'] = admin.id
            session['admin_name'] = admin.name
            flash('Login successful!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid username or password.', 'danger')
    
    return render_template('admin_login.html')

@app.route('/admin/register', methods=['GET', 'POST'])
def admin_register():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        
        if Admin.query.filter_by(username=username).first():
            flash('Username already exists.', 'danger')
            return redirect(url_for('admin_register'))
        
        admin = Admin(
            name=name,
            username=username,
            password=generate_password_hash(password),
            email=email
        )
        db.session.add(admin)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('admin_login'))
    
    return render_template('admin_register.html')

@app.route('/admin/dashboard')
@admin_login_required
def admin_dashboard():
    total_students = Student.query.count()
    total_quizzes = Quiz.query.count()
    total_questions = Question.query.count()
    total_attempts = QuizAttempt.query.count()
    
    recent_attempts = QuizAttempt.query.order_by(QuizAttempt.attempt_date.desc()).limit(5).all()
    
    return render_template('admin_dashboard.html', 
                         total_students=total_students,
                         total_quizzes=total_quizzes,
                         total_questions=total_questions,
                         total_attempts=total_attempts,
                         recent_attempts=recent_attempts)

@app.route('/admin/students')
@admin_login_required
def admin_students():
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    
    query = Student.query
    if search:
        query = query.filter(
            (Student.name.contains(search)) | 
            (Student.email.contains(search)) |
            (Student.roll_number.contains(search))
        )
    
    students = query.paginate(page=page, per_page=10)
    
    return render_template('admin_students.html', students=students, search=search)

@app.route('/admin/students/add', methods=['GET', 'POST'])
@admin_login_required
def add_student():
    if request.method == 'POST':
        name = request.form.get('name')
        roll_number = request.form.get('roll_number')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if Student.query.filter_by(roll_number=roll_number).first():
            flash('Roll number already exists.', 'danger')
            return redirect(url_for('add_student'))
        
        student = Student(
            name=name,
            roll_number=roll_number,
            email=email,
            password=generate_password_hash(password)
        )
        db.session.add(student)
        db.session.commit()
        
        flash('Student added successfully!', 'success')
        return redirect(url_for('admin_students'))
    
    return render_template('add_student.html')

@app.route('/admin/students/edit/<int:id>', methods=['GET', 'POST'])
@admin_login_required
def edit_student(id):
    student = Student.query.get_or_404(id)
    
    if request.method == 'POST':
        student.name = request.form.get('name')
        student.roll_number = request.form.get('roll_number')
        student.email = request.form.get('email')
        
        if request.form.get('password'):
            student.password = generate_password_hash(request.form.get('password'))
        
        db.session.commit()
        flash('Student updated successfully!', 'success')
        return redirect(url_for('admin_students'))
    
    return render_template('edit_student.html', student=student)

@app.route('/admin/students/delete/<int:id>')
@admin_login_required
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash('Student deleted successfully!', 'success')
    return redirect(url_for('admin_students'))

@app.route('/admin/quizzes')
@admin_login_required
def admin_quizzes():
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    
    query = Quiz.query
    if search:
        query = query.filter(Quiz.title.contains(search))
    
    quizzes = query.paginate(page=page, per_page=10)
    
    return render_template('admin_quizzes.html', quizzes=quizzes, search=search)

@app.route('/admin/quizzes/add', methods=['GET', 'POST'])
@admin_login_required
def add_quiz():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        duration = request.form.get('duration', type=int)
        total_marks = request.form.get('total_marks', type=int)
        
        quiz = Quiz(
            title=title,
            description=description,
            duration=duration,
            total_marks=total_marks
        )
        db.session.add(quiz)
        db.session.commit()
        
        flash('Quiz added successfully!', 'success')
        return redirect(url_for('admin_quizzes'))
    
    return render_template('add_quiz.html')

@app.route('/admin/quizzes/edit/<int:id>', methods=['GET', 'POST'])
@admin_login_required
def edit_quiz(id):
    quiz = Quiz.query.get_or_404(id)
    
    if request.method == 'POST':
        quiz.title = request.form.get('title')
        quiz.description = request.form.get('description')
        quiz.duration = request.form.get('duration', type=int)
        quiz.total_marks = request.form.get('total_marks', type=int)
        
        db.session.commit()
        flash('Quiz updated successfully!', 'success')
        return redirect(url_for('admin_quizzes'))
    
    return render_template('edit_quiz.html', quiz=quiz)

@app.route('/admin/quizzes/delete/<int:id>')
@admin_login_required
def delete_quiz(id):
    quiz = Quiz.query.get_or_404(id)
    
    # Delete associated questions
    Question.query.filter_by(quiz_id=id).delete()
    
    db.session.delete(quiz)
    db.session.commit()
    flash('Quiz deleted successfully!', 'success')
    return redirect(url_for('admin_quizzes'))

@app.route('/admin/quizzes/<int:quiz_id>/questions')
@admin_login_required
def quiz_questions(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = Question.query.filter_by(quiz_id=quiz_id).all()
    return render_template('quiz_questions.html', quiz=quiz, questions=questions)

@app.route('/admin/quizzes/<int:quiz_id>/questions/add', methods=['GET', 'POST'])
@admin_login_required
def add_question(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    
    if request.method == 'POST':
        question_text = request.form.get('question')
        option_a = request.form.get('option_a')
        option_b = request.form.get('option_b')
        option_c = request.form.get('option_c')
        option_d = request.form.get('option_d')
        correct_answer = request.form.get('correct_answer')
        marks = request.form.get('marks', type=int)
        
        question = Question(
            quiz_id=quiz_id,
            question=question_text,
            option_a=option_a,
            option_b=option_b,
            option_c=option_c,
            option_d=option_d,
            correct_answer=correct_answer,
            marks=marks
        )
        db.session.add(question)
        db.session.commit()
        
        flash('Question added successfully!', 'success')
        return redirect(url_for('quiz_questions', quiz_id=quiz_id))
    
    return render_template('add_question.html', quiz=quiz)

@app.route('/admin/questions/edit/<int:id>', methods=['GET', 'POST'])
@admin_login_required
def edit_question(id):
    question = Question.query.get_or_404(id)
    
    if request.method == 'POST':
        question.question = request.form.get('question')
        question.option_a = request.form.get('option_a')
        question.option_b = request.form.get('option_b')
        question.option_c = request.form.get('option_c')
        question.option_d = request.form.get('option_d')
        question.correct_answer = request.form.get('correct_answer')
        question.marks = request.form.get('marks', type=int)
        
        db.session.commit()
        flash('Question updated successfully!', 'success')
        return redirect(url_for('quiz_questions', quiz_id=question.quiz_id))
    
    return render_template('edit_question.html', question=question)

@app.route('/admin/questions/delete/<int:id>')
@admin_login_required
def delete_question(id):
    question = Question.query.get_or_404(id)
    quiz_id = question.quiz_id
    db.session.delete(question)
    db.session.commit()
    flash('Question deleted successfully!', 'success')
    return redirect(url_for('quiz_questions', quiz_id=quiz_id))

@app.route('/admin/assign-quiz', methods=['GET', 'POST'])
@admin_login_required
def assign_quiz():
    if request.method == 'POST':
        quiz_id = request.form.get('quiz_id')
        student_ids = request.form.getlist('student_ids')
        
        for student_id in student_ids:
            # Check if already assigned
            existing = Quiz.query.filter_by(id=quiz_id).first()
            if existing:
                # Quiz is already available to all students by default
                pass
        
        flash('Quiz assigned successfully!', 'success')
        return redirect(url_for('admin_quizzes'))
    
    quizzes = Quiz.query.all()
    students = Student.query.all()
    return render_template('assign_quiz.html', quizzes=quizzes, students=students)

@app.route('/admin/results')
@admin_login_required
def admin_results():
    page = request.args.get('page', 1, type=int)
    
    attempts = QuizAttempt.query.order_by(QuizAttempt.attempt_date.desc()).paginate(page=page, per_page=10)
    
    return render_template('admin_results.html', attempts=attempts)

@app.route('/admin/reports')
@admin_login_required
def admin_reports():
    students = Student.query.all()
    quizzes = Quiz.query.all()
    
    student_performance = []
    for student in students:
        attempts = QuizAttempt.query.filter_by(student_id=student.id).all()
        total_score = sum(attempt.score for attempt in attempts)
        avg_score = total_score / len(attempts) if attempts else 0
        student_performance.append({
            'student': student,
            'attempts': len(attempts),
            'total_score': total_score,
            'avg_score': avg_score
        })
    
    quiz_stats = []
    for quiz in quizzes:
        attempts = QuizAttempt.query.filter_by(quiz_id=quiz.id).all()
        avg_score = sum(attempt.score for attempt in attempts) / len(attempts) if attempts else 0
        quiz_stats.append({
            'quiz': quiz,
            'attempts': len(attempts),
            'avg_score': avg_score
        })
    
    return render_template('admin_reports.html', 
                         student_performance=student_performance,
                         quiz_stats=quiz_stats)

@app.route('/admin/logout')
def admin_logout():
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('home'))

# Student Routes
@app.route('/student/register', methods=['GET', 'POST'])
def student_register():
    if request.method == 'POST':
        name = request.form.get('name')
        roll_number = request.form.get('roll_number')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if Student.query.filter_by(roll_number=roll_number).first():
            flash('Roll number already exists.', 'danger')
            return redirect(url_for('student_register'))
        
        student = Student(
            name=name,
            roll_number=roll_number,
            email=email,
            password=generate_password_hash(password)
        )
        db.session.add(student)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('student_login'))
    
    return render_template('student_register.html')

@app.route('/student/login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        roll_number = request.form.get('roll_number')
        password = request.form.get('password')
        
        student = Student.query.filter_by(roll_number=roll_number).first()
        if student and check_password_hash(student.password, password):
            session['student_id'] = student.id
            session['student_name'] = student.name
            flash('Login successful!', 'success')
            return redirect(url_for('student_dashboard'))
        else:
            flash('Invalid roll number or password.', 'danger')
    
    return render_template('student_login.html')

@app.route('/student/dashboard')
@student_login_required
def student_dashboard():
    student_id = session.get('student_id')
    student = Student.query.get(student_id)
    
    available_quizzes = Quiz.query.all()
    attempts = QuizAttempt.query.filter_by(student_id=student_id).order_by(QuizAttempt.attempt_date.desc()).limit(5).all()
    
    return render_template('student_dashboard.html', 
                         student=student,
                         available_quizzes=available_quizzes,
                         attempts=attempts)

@app.route('/student/quizzes')
@student_login_required
def student_quizzes():
    quizzes = Quiz.query.all()
    student_id = session.get('student_id')
    
    # Add attempt count for each quiz
    for quiz in quizzes:
        quiz.attempt_count = QuizAttempt.query.filter_by(
            student_id=student_id, 
            quiz_id=quiz.id
        ).count()
    
    return render_template('student_quizzes.html', quizzes=quizzes)

@app.route('/student/quiz/<int:quiz_id>')
@student_login_required
def take_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = Question.query.filter_by(quiz_id=quiz_id).all()
    
    return render_template('take_quiz.html', quiz=quiz, questions=questions)

@app.route('/student/quiz/<int:quiz_id>/submit', methods=['POST'])
@student_login_required
def submit_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = Question.query.filter_by(quiz_id=quiz_id).all()
    student_id = session.get('student_id')
    
    total_score = 0
    total_marks = sum(q.marks for q in questions)
    
    # Create quiz attempt
    attempt = QuizAttempt(
        student_id=student_id,
        quiz_id=quiz_id,
        score=0,
        attempt_date=datetime.now()
    )
    db.session.add(attempt)
    db.session.commit()
    
    # Calculate score and save answers
    for question in questions:
        answer = request.form.get(f'question_{question.id}')
        is_correct = answer == question.correct_answer
        
        if is_correct:
            total_score += question.marks
        
        result = QuizResult(
            attempt_id=attempt.id,
            question_id=question.id,
            student_answer=answer,
            is_correct=is_correct,
            marks_obtained=question.marks if is_correct else 0
        )
        db.session.add(result)
    
    # Update attempt score
    attempt.score = total_score
    db.session.commit()
    
    flash(f'Quiz submitted successfully! Your score: {total_score}/{total_marks}', 'success')
    return redirect(url_for('quiz_result', attempt_id=attempt.id))

@app.route('/student/result/<int:attempt_id>')
@student_login_required
def quiz_result(attempt_id):
    attempt = QuizAttempt.query.get_or_404(attempt_id)
    results = QuizResult.query.filter_by(attempt_id=attempt_id).all()
    quiz = Quiz.query.get(attempt.quiz_id)
    
    return render_template('quiz_result.html', attempt=attempt, results=results, quiz=quiz)

@app.route('/student/attempts')
@student_login_required
def student_attempts():
    student_id = session.get('student_id')
    attempts = QuizAttempt.query.filter_by(student_id=student_id).order_by(QuizAttempt.attempt_date.desc()).all()
    
    return render_template('student_attempts.html', attempts=attempts)

@app.route('/student/profile', methods=['GET', 'POST'])
@student_login_required
def student_profile():
    student_id = session.get('student_id')
    student = Student.query.get(student_id)
    
    if request.method == 'POST':
        student.name = request.form.get('name')
        student.email = request.form.get('email')
        
        if request.form.get('password'):
            student.password = generate_password_hash(request.form.get('password'))
        
        db.session.commit()
        session['student_name'] = student.name
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('student_dashboard'))
    
    return render_template('student_profile.html', student=student)

@app.route('/student/logout')
def student_logout():
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
