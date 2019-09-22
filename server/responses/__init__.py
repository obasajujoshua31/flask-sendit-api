from flask import jsonify
from email_validator import validate_email, EmailNotValidError

class Response:
    def client_response(self, status_code, success, data):
        response = jsonify({
            "success": success,
            "data": data
        })
        response.status_code = status_code
        return response

    def is_valid_email(self, email):
        try:
            validate_email(email)
            return True
        except EmailNotValidError:
            return False