from flask import Flask, jsonify, request, session
from app import create_app, db
from app.models import User  # Import the User model
from werkzeug.security import generate_password_hash, check_password_hash

app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Auth:
    @staticmethod
    def get_user_from_session_id(session_id):
        return User.query.filter_by(session_id=session_id).first()

    @staticmethod
    def destroy_session(user_id):
        user = User.query.get(user_id)
        if user:
            user.session_id = None
            db.session.commit()

AUTH = Auth()

@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    return jsonify({"message": "Page successfully created"})

@app.route("/register", methods=["POST"], strict_slashes=False)
def register() -> str:
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not password or not email:
        return jsonify({"error": "email and password required"}), 400

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"error": "User already exist"}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(email=email, hashed_password=hashed_password)  # Corrected typo in 'hashed_password'
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User Account successfully created"}), 201

@app.route("/login", methods=["POST"])
def login() -> str:
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not password or not email:
        return jsonify({"error": "email and password are required"}), 400
    
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.hashed_password, password):
        return jsonify({"error": "invalid email and password"}), 400

    return jsonify({"message": "login successful"})

@app.route("/logout", methods=["POST"])
def logout() -> str:
    session_id = request.cookies.get("session_id")
    if not session_id:
        return jsonify({"error": "Not logged in"}), 401

    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        return jsonify({"error": "Invalid session"}), 403

    AUTH.destroy_session(user.id)
    response = jsonify({"message": "Logout successful"})
    response.delete_cookie("session_id")
    return response

@app.route("/profile", methods=["GET"])
def profile() -> str:
    session_id = request.cookies.get("session_id")
    if not session_id:
        return jsonify({"error": "Not logged in"}), 401

    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        return jsonify({"error": "Invalid session"}), 403

    return jsonify({"email": user.email})

if __name__ == "__main__":
    app.run(debug=True)