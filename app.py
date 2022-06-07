# Main entry point for the application, responsible for setting up and running the Flask server.

from flask import Flask
from routes.home import home_bp
from routes.astrological_insights import astrological_insights_bp
from components.exception import CustomException
import sys

# Initialize Flask app
app = Flask(__name__)

# Register routes
try:
    app.register_blueprint(home_bp)
    app.register_blueprint(astrological_insights_bp)
except Exception as e:
    raise CustomException(e, sys)

# Start the Flask server
if __name__ == '__main__':
    app.run(debug=True)
