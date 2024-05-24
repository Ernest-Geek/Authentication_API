from flask import Flask, jsonify, request, session
from app import create_app, db
from app.auth.auth import Auth  # Corrected import path

app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

AUTH = Auth()

@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    return jsonify({"message": "Page successfully created"})

@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    app.logger.info(f"Request data: {request.data}")
    data = request.get_json()
    if not data:
        return jsonify({"error": "Email and password are required"}), 400

    email = data.get("email")
    password = data.get("password")
    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    except Exception as e:
        app.logger.error(f"Exception: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/login", methods=["POST"])
def login() -> str:
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    if not AUTH.valid_login(email, password):
        return jsonify({"error": "Invalid email or password"}), 401

    session_id = AUTH.create_session(email)
    if not session_id:
        return jsonify({"error": "Unable to create session"}), 500

    response = jsonify({"message": "Login successful"})
    response.set_cookie("session_id", session_id)
    return response

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

