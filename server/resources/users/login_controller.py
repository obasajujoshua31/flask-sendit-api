from server.responses import Response, validate_email
from flask_restful import Resource
from flask_jwt_extended import (create_access_token)
from server.form import form_get



class LoginController(Resource, Response):
    def post(self):
        email = form_get("email")
        password = form_get("password")

        if not email:
            return Response.client_response(self, 400, False, "Email required")
        if not password:
            return Response.client_response(self, 400, False, "Password required")
        if not validate_email(email):
            return Response.client_response(self, 400, False, "Invalid Email")

        from server.resources.users.users_model import User
        from app import secure_password
        found_user = User.get_one_by_email(email)
        if not found_user:
            return Response.client_response(self, 401, False, "Invalid Login Credentials")
        elif not secure_password.check_password_hash(found_user.password, password):
            return Response.client_response(self, 401, False, "Invalid Login Credentials")
        else:
            return Response.client_response(self, 200, True, {
                "access_token": create_access_token(identity=found_user.id),
                "id": found_user.id
            })




