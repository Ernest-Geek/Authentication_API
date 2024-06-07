from flask import request, jsonify, render_template, current_app, redirect, url_for
from .models import User
from . import db_session

@current_app.route('/')
def home():
    return render_template('index.html')

@current_app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        if not data or not all(k in data for k in ('name', 'surname', 'email', 'password')):
            return jsonify({'message': 'Missing required parameters'}), 400

        name = data['name']
        surname = data['surname']
        email = data['email']
        password = data['password']

        existing_user = db_session.query(User).filter_by(email=email).first()
        if existing_user:
            return jsonify({'message': 'User already exists'}), 400

        new_user = User(name=name, surname=surname, email=email, password=password)
        db_session.add(new_user)
        db_session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    return render_template('register.html')

@current_app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        if not data or not all(k in data for k in ('email', 'password')):
            return jsonify({'message': 'Missing required parameters'}), 400

        email = data['email']
        password = data['password']

        user = db_session.query(User).filter_by(email=email).first()
        if user and user.password == password:
            return jsonify({'message': 'Login successful', 'user_id': user.id}), 200
        return jsonify({'message': 'Invalid credentials'}), 401
    return render_template('login.html')

@current_app.route('/profile/<int:user_id>')
def profile(user_id):
    user = db_session.query(User).get(user_id)
    if user:
        return render_template('profile.html', user=user)
    else:
        return render_template('not_found.html'), 404

@current_app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        # Handle password reset logic here
        # Example: Send reset password email to the provided email address
        return jsonify({'message': 'Password reset email sent successfully'}), 200
    return render_template('forgot_password.html')
