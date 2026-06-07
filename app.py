from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "secret123"

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), default='pending')
    user = db.Column(db.String(100), nullable=False)

# Home → login page
@app.route('/')
def home():
    return render_template('login.html')

# Register page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('register.html')

# Login check
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username, password=password).first()

    if user:
        session['user'] = username
        return redirect(url_for('dashboard'))
    else:
        return "Invalid credentials"

# Dashboard
@app.route('/dashboard')
def dashboard():
    if 'user' in session:

        tasks = Task.query.filter_by(user=session['user']).all()

        total_tasks = len(tasks)

        completed_tasks = len(
            [task for task in tasks if task.status == "Completed"]
        )

        if total_tasks > 0:
            productivity_score = int((completed_tasks / total_tasks) * 100)
        else:
            productivity_score = 0

        # AI Suggestions
        if productivity_score >= 80:
            suggestion = "Excellent productivity detected."
        elif productivity_score >= 50:
            suggestion = "Average productivity. Improvement recommended."
        else:
            suggestion = "Low productivity alert. Focus on pending tasks."

        return render_template(
            'dashboard.html',
            user=session['user'],
            tasks=tasks,
            productivity_score=productivity_score,
            suggestion=suggestion
        )

    return redirect(url_for('home'))


# add task
@app.route('/add_task', methods=['POST'])
def add_task():
    if 'user' in session:
        title = request.form['title']

        new_task = Task(title=title,
                        status='pending',
                         user=session['user'])
        db.session.add(new_task)
        db.session.commit()

    return redirect(url_for('dashboard'))


#COMPLETE TASK
@app.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    task = Task.query.get(task_id)
    task.status = "Completed"
    db.session.commit()
    return redirect(url_for('dashboard'))

#DELETE TASK
@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('dashboard'))


#logout route
@app.route('/logout')
def logout():
        session.pop('user', None)
        return redirect(url_for('home'))

# Create DB
@app.route('/create_db')
def create_db():
    db.create_all()
    return "Database Created"

if __name__ == '__main__':
    app.run(debug=True)



