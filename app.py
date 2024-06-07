from app import create_app

# Create an instance of the Flask application using the factory function
app = create_app()

# Entry point for running the Flask application
if __name__ == "__main__":
    # Run the Flask application in debug mode
    app.run(debug=True)
