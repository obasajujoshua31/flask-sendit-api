from flask import jsonify


class Response:
    def success_response(self, status_code, success, data):
        response = jsonify({
            "success": success,
            "data": data
        })
        response.status_code = status_code
        return response