from flask import Flask, jsonify, request, abort, redirect

from auth import Auth

app = Flask(__name__)
AUTH = Auth()

@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """GET /
    Return:
        - The home page's payload.
    """
    return jsonify({"message": "Page successfully created"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """POST /users
    Return:
        - The account creation payload.
    """
    email, password = request.form.get("email"), request.form.get("password")
    try:
        AUTH.register_user(email, password)  # Update this line
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

@app.route("/login", methods=['POST'])
def login() -> str:
    """POST /login
    Log in a user.
    Returns:
        - The login status.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    # Validate email and password
    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    # Check if user exists
    user = auth.get_user(email)
    if not user:
        return jsonify({"error": "User does not exist"}), 401

    # Verify password
    if not auth.verify_password(user.password, password):
        return jsonify({"error": "Invalid password"}), 401

    # Create session
    session["email"] = email

    return jsonify({"message": "Login successful"}), 200


@app.route("/logout", methods=['POST'])
def logout() -> str:
    """POST /logout
    Log out a user.
    Returns:
        - The logout status.
    """
    # Check if user is logged in
    if "email" not in session:
        return jsonify({"error": "Not logged in"}), 401

    # Clear session
    session.pop("email", None)

    return jsonify({"message": "Logout successful"}), 200

# Update Profile Endpoint
@app.route("/profile", methods=["PUT"])
def update_profile():
    if "email" not in session:
        return jsonify({"error": "Not logged in"}), 401
    
    email = session["email"]
    new_profile_data = request.json  # Assuming JSON payload
    try:
        AUTH.update_profile(email, new_profile_data)  # Update this line with your update profile logic
        return jsonify({"message": "Profile updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Change Password Endpoint
@app.route("/change-password", methods=["POST"])
def change_password():
    if "email" not in session:
        return jsonify({"error": "Not logged in"}), 401
    
    email = session["email"]
    old_password = request.json.get("old_password")
    new_password = request.json.get("new_password")
    try:
        AUTH.change_password(email, old_password, new_password)  # Update this line with your change password logic
        return jsonify({"message": "Password changed successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Manage Account Settings Endpoint
@app.route("/settings", methods=["PUT"])
def manage_settings():
    if "email" not in session:
        return jsonify({"error": "Not logged in"}), 401
    
    email = session["email"]
    new_settings = request.json  # Assuming JSON payload
    try:
        AUTH.manage_settings(email, new_settings)  # Update this line with your manage settings logic
        return jsonify({"message": "Settings updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
