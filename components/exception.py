# Defines a custom exception class and provides utilities for logging detailed error messages.

import sys
import logging

def error_message_detail(error, error_detail: sys):
    """
    Returns a detailed error message containing the script name and line number where the error occurred.
    Parameters:
        error (Exception): The exception object.
        error_detail (sys): The sys module for extracting traceback information.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in script: {file_name} at line number: {exc_tb.tb_lineno} - Error Message: {str(error)}"
    return error_message

class CustomException(Exception):
    """
    Custom exception class to provide detailed error messages and handle exceptions in the application.
    """
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
