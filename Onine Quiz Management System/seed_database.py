from app import app
from models import db, Admin, Student, Quiz, Question, QuizAttempt, QuizResult
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta

def seed_database():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Create Admin
        admin = Admin(
            name='Admin User',
            username='admin',
            password=generate_password_hash('admin123'),
            email='admin@quiz.com'
        )
        db.session.add(admin)
        
        # Create Students
        students = [
            Student(
                name='John Doe',
                roll_number='STU001',
                email='john@example.com',
                password=generate_password_hash('student123')
            ),
            Student(
                name='Jane Smith',
                roll_number='STU002',
                email='jane@example.com',
                password=generate_password_hash('student123')
            ),
            Student(
                name='Bob Johnson',
                roll_number='STU003',
                email='bob@example.com',
                password=generate_password_hash('student123')
            ),
            Student(
                name='Alice Williams',
                roll_number='STU004',
                email='alice@example.com',
                password=generate_password_hash('student123')
            ),
            Student(
                name='Charlie Brown',
                roll_number='STU005',
                email='charlie@example.com',
                password=generate_password_hash('student123')
            ),
            Student(
                name='Diana Prince',
                roll_number='STU006',
                email='diana@example.com',
                password=generate_password_hash('student123')
            ),
            Student(
                name='Edward Stone',
                roll_number='STU007',
                email='edward@example.com',
                password=generate_password_hash('student123')
            ),
            Student(
                name='Fiona Green',
                roll_number='STU008',
                email='fiona@example.com',
                password=generate_password_hash('student123')
            ),
            Student(
                name='George King',
                roll_number='STU009',
                email='george@example.com',
                password=generate_password_hash('student123')
            ),
            Student(
                name='Hannah White',
                roll_number='STU010',
                email='hannah@example.com',
                password=generate_password_hash('student123')
            )
        ]
        for student in students:
            db.session.add(student)
        
        # Create Quizzes
        quiz1 = Quiz(
            title='Python Programming Basics',
            description='Test your knowledge of Python programming fundamentals',
            duration=30,
            total_marks=20
        )
        db.session.add(quiz1)
        
        quiz2 = Quiz(
            title='Database Management',
            description='Questions about SQL and database concepts',
            duration=25,
            total_marks=15
        )
        db.session.add(quiz2)
        
        quiz3 = Quiz(
            title='Web Development Fundamentals',
            description='HTML, CSS, and JavaScript basics',
            duration=20,
            total_marks=10
        )
        db.session.add(quiz3)
        
        quiz4 = Quiz(
            title='Data Structures',
            description='Arrays, linked lists, stacks, queues, trees, and graphs',
            duration=35,
            total_marks=25
        )
        db.session.add(quiz4)
        
        quiz5 = Quiz(
            title='Computer Networks',
            description='OSI model, TCP/IP, protocols, and network security',
            duration=30,
            total_marks=20
        )
        db.session.add(quiz5)
        
        db.session.commit()
        
        # Add Questions for Quiz 1 (Python)
        questions_quiz1 = [
            Question(
                quiz_id=quiz1.id,
                question='What is the correct file extension for Python files?',
                option_a='.python',
                option_b='.pt',
                option_c='.py',
                option_d='.pyt',
                correct_answer='C',
                marks=2
            ),
            Question(
                quiz_id=quiz1.id,
                question='Which keyword is used to define a function in Python?',
                option_a='func',
                option_b='def',
                option_c='function',
                option_d='define',
                correct_answer='B',
                marks=2
            ),
            Question(
                quiz_id=quiz1.id,
                question='What is the output of print(2 ** 3)?',
                option_a='6',
                option_b='8',
                option_c='9',
                option_d='5',
                correct_answer='B',
                marks=2
            ),
            Question(
                quiz_id=quiz1.id,
                question='Which data type is mutable in Python?',
                option_a='Tuple',
                option_b='String',
                option_c='List',
                option_d='Integer',
                correct_answer='C',
                marks=2
            ),
            Question(
                quiz_id=quiz1.id,
                question='What does the len() function do in Python?',
                option_a='Returns the length of an object',
                option_b='Returns the type of an object',
                option_c='Returns the value of an object',
                option_d='Returns the memory address of an object',
                correct_answer='A',
                marks=2
            ),
            Question(
                quiz_id=quiz1.id,
                question='Which symbol is used for comments in Python?',
                option_a='//',
                option_b='/* */',
                option_c='#',
                option_d='--',
                correct_answer='C',
                marks=2
            ),
            Question(
                quiz_id=quiz1.id,
                question='What is the result of bool(0)?',
                option_a='True',
                option_b='False',
                option_c='Error',
                option_d='None',
                correct_answer='B',
                marks=2
            ),
            Question(
                quiz_id=quiz1.id,
                question='Which method is used to add an element to the end of a list?',
                option_a='append()',
                option_b='add()',
                option_c='insert()',
                option_d='push()',
                correct_answer='A',
                marks=2
            ),
            Question(
                quiz_id=quiz1.id,
                question='What is the correct way to create a dictionary in Python?',
                option_a='dict = {}',
                option_b='dict = []',
                option_c='dict = ()',
                option_d='dict = <>',
                correct_answer='A',
                marks=2
            ),
            Question(
                quiz_id=quiz1.id,
                question='Which operator is used for exponentiation in Python?',
                option_a='^',
                option_b='**',
                option_c='^^',
                option_d='exp',
                correct_answer='B',
                marks=2
            )
        ]
        for question in questions_quiz1:
            db.session.add(question)
        
        # Add Questions for Quiz 2 (Database)
        questions_quiz2 = [
            Question(
                quiz_id=quiz2.id,
                question='What does SQL stand for?',
                option_a='Structured Query Language',
                option_b='Simple Query Language',
                option_c='Standard Query Language',
                option_d='Structured Question Language',
                correct_answer='A',
                marks=3
            ),
            Question(
                quiz_id=quiz2.id,
                question='Which SQL statement is used to retrieve data from a database?',
                option_a='GET',
                option_b='OPEN',
                option_c='SELECT',
                option_d='EXTRACT',
                correct_answer='C',
                marks=3
            ),
            Question(
                quiz_id=quiz2.id,
                question='Which clause is used to filter records in SQL?',
                option_a='WHERE',
                option_b='FILTER',
                option_c='HAVING',
                option_d='GROUP BY',
                correct_answer='A',
                marks=3
            ),
            Question(
                quiz_id=quiz2.id,
                question='What is the primary key in a database table?',
                option_a='A unique identifier for each record',
                option_b='The first column in the table',
                option_c='A foreign key reference',
                option_d='An index for faster search',
                correct_answer='A',
                marks=3
            ),
            Question(
                quiz_id=quiz2.id,
                question='Which SQL command is used to delete a table?',
                option_a='REMOVE TABLE',
                option_b='DELETE TABLE',
                option_c='DROP TABLE',
                option_d='CLEAR TABLE',
                correct_answer='C',
                marks=3
            )
        ]
        for question in questions_quiz2:
            db.session.add(question)
        
        # Add Questions for Quiz 3 (Web Development)
        questions_quiz3 = [
            Question(
                quiz_id=quiz3.id,
                question='What does HTML stand for?',
                option_a='Hyper Text Markup Language',
                option_b='High Tech Modern Language',
                option_c='Hyper Transfer Markup Language',
                option_d='Home Tool Markup Language',
                correct_answer='A',
                marks=2
            ),
            Question(
                quiz_id=quiz3.id,
                question='Which HTML tag is used to define an internal style sheet?',
                option_a='<script>',
                option_b='<style>',
                option_c='<css>',
                option_d='<link>',
                correct_answer='B',
                marks=2
            ),
            Question(
                quiz_id=quiz3.id,
                question='What is the correct CSS syntax for changing the text color?',
                option_a='color: red;',
                option_b='text-color: red;',
                option_c='font-color: red;',
                option_d='text: red;',
                correct_answer='A',
                marks=2
            ),
            Question(
                quiz_id=quiz3.id,
                question='Which JavaScript method is used to write into the browser console?',
                option_a='console.write()',
                option_b='console.log()',
                option_c='print()',
                option_d='document.write()',
                correct_answer='B',
                marks=2
            ),
            Question(
                quiz_id=quiz3.id,
                question='Which HTML element is used for the largest heading?',
                option_a='<heading>',
                option_b='<h6>',
                option_c='<h1>',
                option_d='<head>',
                correct_answer='C',
                marks=2
            )
        ]
        for question in questions_quiz3:
            db.session.add(question)
        
        # Add Questions for Quiz 4 (Data Structures)
        questions_quiz4 = [
            Question(
                quiz_id=quiz4.id,
                question='Which data structure follows LIFO principle?',
                option_a='Queue',
                option_b='Stack',
                option_c='Array',
                option_d='Linked List',
                correct_answer='B',
                marks=3
            ),
            Question(
                quiz_id=quiz4.id,
                question='What is the time complexity of binary search in a sorted array?',
                option_a='O(n)',
                option_b='O(log n)',
                option_c='O(n^2)',
                option_d='O(1)',
                correct_answer='B',
                marks=3
            ),
            Question(
                quiz_id=quiz4.id,
                question='Which data structure uses key-value pairs?',
                option_a='Array',
                option_b='Stack',
                option_c='Hash Table',
                option_d='Queue',
                correct_answer='C',
                marks=2
            ),
            Question(
                quiz_id=quiz4.id,
                question='In a binary tree, each node can have at most how many children?',
                option_a='1',
                option_b='2',
                option_c='3',
                option_d='4',
                correct_answer='B',
                marks=2
            ),
            Question(
                quiz_id=quiz4.id,
                question='Which traversal visits root, left subtree, then right subtree?',
                option_a='Inorder',
                option_b='Preorder',
                option_c='Postorder',
                option_d='Level order',
                correct_answer='B',
                marks=3
            ),
            Question(
                quiz_id=quiz4.id,
                question='What is the worst-case time complexity for inserting into a linked list?',
                option_a='O(1)',
                option_b='O(n)',
                option_c='O(log n)',
                option_d='O(n^2)',
                correct_answer='B',
                marks=2
            ),
            Question(
                quiz_id=quiz4.id,
                question='Which data structure is best for implementing priority queue?',
                option_a='Array',
                option_b='Linked List',
                option_c='Heap',
                option_d='Stack',
                correct_answer='C',
                marks=3
            ),
            Question(
                quiz_id=quiz4.id,
                question='What is a graph with directed edges called?',
                option_a='Undirected graph',
                option_b='Directed graph',
                option_c='Weighted graph',
                option_d='Complete graph',
                correct_answer='B',
                marks=2
            ),
            Question(
                quiz_id=quiz4.id,
                question='Which algorithm is used to find shortest path in weighted graphs?',
                option_a='BFS',
                option_b='DFS',
                option_c='Dijkstra',
                option_d='Prim',
                correct_answer='C',
                marks=3
            ),
            Question(
                quiz_id=quiz4.id,
                question='What is the space complexity of recursive algorithms?',
                option_a='O(1)',
                option_b='O(n)',
                option_c='O(log n)',
                option_d='O(n^2)',
                correct_answer='B',
                marks=2
            )
        ]
        for question in questions_quiz4:
            db.session.add(question)
        
        # Add Questions for Quiz 5 (Computer Networks)
        questions_quiz5 = [
            Question(
                quiz_id=quiz5.id,
                question='How many layers are in the OSI model?',
                option_a='5',
                option_b='6',
                option_c='7',
                option_d='8',
                correct_answer='C',
                marks=2
            ),
            Question(
                quiz_id=quiz5.id,
                question='Which protocol is used for secure web browsing?',
                option_a='HTTP',
                option_b='FTP',
                option_c='HTTPS',
                option_d='SMTP',
                correct_answer='C',
                marks=2
            ),
            Question(
                quiz_id=quiz5.id,
                question='What is the default port for HTTPS?',
                option_a='80',
                option_b='443',
                option_c='21',
                option_d='25',
                correct_answer='B',
                marks=2
            ),
            Question(
                quiz_id=quiz5.id,
                question='Which layer of OSI model is responsible for routing?',
                option_a='Data Link',
                option_b='Network',
                option_c='Transport',
                option_d='Session',
                correct_answer='B',
                marks=3
            ),
            Question(
                quiz_id=quiz5.id,
                question='What is the purpose of DNS?',
                option_a='File transfer',
                option_b='Domain name resolution',
                option_c='Email transmission',
                option_d='Web hosting',
                correct_answer='B',
                marks=2
            ),
            Question(
                quiz_id=quiz5.id,
                question='Which protocol is used for email transmission?',
                option_a='HTTP',
                option_b='FTP',
                option_c='SMTP',
                option_d='DNS',
                correct_answer='C',
                marks=2
            ),
            Question(
                quiz_id=quiz5.id,
                question='What is a firewall used for?',
                option_a='Speed up network',
                option_b='Network security',
                option_c='Data compression',
                option_d='Load balancing',
                correct_answer='B',
                marks=2
            ),
            Question(
                quiz_id=quiz5.id,
                question='Which IP address class supports the most hosts?',
                option_a='Class A',
                option_b='Class B',
                option_c='Class C',
                option_d='Class D',
                correct_answer='A',
                marks=2
            ),
            Question(
                quiz_id=quiz5.id,
                question='What is the purpose of MAC address?',
                option_a='Network layer addressing',
                option_b='Data link layer addressing',
                option_c='Transport layer addressing',
                option_d='Application layer addressing',
                correct_answer='B',
                marks=2
            ),
            Question(
                quiz_id=quiz5.id,
                question='Which protocol is connectionless?',
                option_a='TCP',
                option_b='UDP',
                option_c='FTP',
                option_d='HTTP',
                correct_answer='B',
                marks=3
            )
        ]
        for question in questions_quiz5:
            db.session.add(question)
        
        db.session.commit()
        
        # Add sample quiz attempts with results
        # Get all students and quizzes
        all_students = Student.query.all()
        all_quizzes = Quiz.query.all()
        
        # Create quiz attempts for each student with varying performance
        import random
        
        for i, student in enumerate(all_students):
            for quiz in all_quizzes:
                # Each student takes each quiz 1-3 times
                num_attempts = random.randint(1, 3)
                
                for attempt_num in range(num_attempts):
                    # Calculate a random score (between 30% and 100%)
                    percentage = random.uniform(0.3, 1.0)
                    score = int(quiz.total_marks * percentage)
                    
                    # Create attempt with random date in the past 30 days
                    days_ago = random.randint(1, 30)
                    attempt_date = datetime.now() - timedelta(days=days_ago)
                    
                    attempt = QuizAttempt(
                        student_id=student.id,
                        quiz_id=quiz.id,
                        score=score,
                        attempt_date=attempt_date
                    )
                    db.session.add(attempt)
                    db.session.flush()  # Get the attempt ID
                    
                    # Get questions for this quiz
                    questions = Question.query.filter_by(quiz_id=quiz.id).all()
                    
                    # Create results for each question
                    for question in questions:
                        # Randomly decide if answer is correct based on overall performance
                        is_correct = random.random() < percentage
                        
                        if is_correct:
                            student_answer = question.correct_answer
                            marks_obtained = question.marks
                        else:
                            # Pick a wrong answer
                            options = ['A', 'B', 'C', 'D']
                            options.remove(question.correct_answer)
                            student_answer = random.choice(options)
                            marks_obtained = 0
                        
                        result = QuizResult(
                            attempt_id=attempt.id,
                            question_id=question.id,
                            student_answer=student_answer,
                            is_correct=is_correct,
                            marks_obtained=marks_obtained
                        )
                        db.session.add(result)
        
        db.session.commit()
        
        print("Database seeded successfully!")
        print("\nLogin Credentials:")
        print("=" * 40)
        print("Admin:")
        print("  Username: admin")
        print("  Password: admin123")
        print("\nStudents:")
        for student in students:
            print(f"  Roll Number: {student.roll_number}")
            print(f"  Password: student123")
        print("=" * 40)
        print(f"\nSample Data Created:")
        print(f"- {len(students)} students")
        print(f"- {len(all_quizzes)} quizzes")
        print(f"- {Question.query.count()} questions")
        print(f"- {QuizAttempt.query.count()} quiz attempts")
        print(f"- {QuizResult.query.count()} question results")
        print("=" * 40)

if __name__ == '__main__':
    seed_database()
