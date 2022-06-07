# Defines the route for the home page of the web application.

from flask import Blueprint, render_template, request, jsonify
from components.exception import CustomException

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    """
    Renders the home page of the web application.
    """
    try:
        return render_template('home.html')
    except Exception as e:
        raise CustomException(e, sys)