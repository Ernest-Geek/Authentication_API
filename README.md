# Authentication_API

## Overview

The Authentication API is a Python-based application designed to handle user authentication. It supports user registration, login, and token-based authentication using JWT (JSON Web Tokens).

## Features

- User Registration: Create a new user account.
- User Login: Authenticate users and provide a JWT token.
- Protected Routes: Access routes that require authentication using the JWT token.

## Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)

## Setup

1.  Clone the repository:

bash
Copy code
git clone https://github.com/Ernest-Geek/Authentication_API.git
cd Authentication_API
2. Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install the dependencies:

bash
Copy code
pip install -r requirements.txt
4. Run the application:

bash
Copy code
python app/main.py

## Usage

### User Registration

To register a new user, make a POST request to the /register endpoint with the following JSON payload:

json
Copy code
{
    "username": "newuser",
    "password": "newpassword"
}
### Example using curl:

bash
Copy code
curl -X POST http://localhost:5000/register -H "Content-Type: application/json" -d '{"username":"newuser","password":"newpassword"}'

## User Login

To log in, make a POST request to the /login endpoint with the following JSON payload:

json
Copy code
{
    "username": "newuser",
    "password": "newpassword"
}
Example using curl:

bash
Copy code
curl -X POST http://localhost:5000/login -H "Content-Type: application/json" -d '{"username":"newuser","password":"newpassword"}'
The response will include a JWT token:

json
Copy code
{
    "token": "your.jwt.token.here"
}
## Protected Routes

To access protected routes, include the JWT token in the Authorization header:

bash
Copy code
curl -X GET http://localhost:5000/protected -H "Authorization: Bearer your.jwt.token.here"

## Running Tests
To run the tests, use the following command:

bash
Copy code
python -m unittest discover -s test

## Contributors

- Ernest Ampene Junior
- Emmanuel Kisanda
- Hussein Abdullahi

## License

This project is licensed under the MIT License. See the LICENSE file for details.