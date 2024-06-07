AuthApi
AuthApi is a simple web application for user authentication, including features like registration, login, and password reset. The application is built using Flask for the backend and HTML/CSS/JavaScript for the frontend.

Table of Contents
Features
Setup
Usage
Routes
Project Structure
Screenshots
Contributing
License
Features
User Registration
User Login
Password Reset
Responsive design with Bootstrap
Setup
Prerequisites
Python 3.8+
Flask
Flask-Mail (for sending reset password emails)
Installation
Clone the repository:

git clone https://github.com/yourusername/AuthApi.git
cd AuthApi

Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:

pip install -r requirements.txt
Set environment variables for Flask:

export FLASK_APP=app.py
export FLASK_ENV=development  # For development environment
Run the application:

flask run
Usage
Open your browser and navigate to http://127.0.0.1:5000/.
Register a new user.
Login with the registered user credentials.
Use the "Forgot Password" feature to reset the password if needed.
Routes
Home: / - The landing page with options to register or login.
Register: /register - Registration page for new users.
Login: /login - Login page for existing users.
Forgot Password: /forgot_password - Page to request password reset instructions.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

License
This project is licensed under the MIT License - see the LICENSE file for details.
