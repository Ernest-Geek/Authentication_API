#!/usr/bin/env python3
"""A simple end-to-end (E2E) integration test for `app.py`.
"""
import requests


#Constants for testing
EMAIL = "ernestampene1@gmail.com"
PASSWD = "Cable@123"
NEW_PASSWD = "hOME@3"
BASE_URL = "http://0.0.0.0:5000"


def user_registration(email:str, password: str) -> None:
    """
    For testing user registration
    """
    url = f"{BASE_URL}/users"
    body = {
        'email': email,
        'password': password,
    }
    #Sends post rquest to the user
    try:
        res = requests.post(url, data=body)
        res.raise_for_status()  # Raise exception for non-200 status codes
        assert res.status_code == 200, f"Unexpected status code: {res.status_code}"
        assert res.json() == {"email": email, "message": "user created"}, "Unexpected response"
        print("User registration successful")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")


if __name__ == '__main__':
    register_user(EMAIL, PASSWD)
