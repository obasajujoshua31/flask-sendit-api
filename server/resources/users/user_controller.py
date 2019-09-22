from server.responses import Response
from flask_jwt_extended import (create_access_token)
from flask_restful import Resource
from server.form import form_get, confirm_is_json


#


class UserController(Resource, Response):
    def get(self):
        from server.resources.users.users_model import User
        users = User.get_all()
        response = []
        for user in users:
            response.append({
                "id": user.id,
                "email": user.email,
                "name": user.name
            })
        return Response.client_response(self, 200, True, response)

    def post(self):
        if not confirm_is_json():
            return Response.client_response(self, 422, False, {"message": "please supply json"})
        name = form_get("name")
        email = form_get("email")
        password = form_get("password")
        #  Add validation function
        # Check if email is Available to complete Signup
        from server.resources.users.users_model import User

        if not name:
            return Response.client_response(self, 400, False, {"message": "name is empty"})
        if not email:
            return Response.client_response(self, 400, False, {"message": "email is empty"})
        if not Response.is_valid_email(self, email):
            return Response.client_response(self, 400, False, {"message": "Invalid email"})
        if not password:
            return Response.client_response(self, 400, False, {"message": "password is empty"})

        try:
            found_user = User.get_one_by_email(email)
            if found_user:
                return Response.client_response(self, 401, False, {"message": "Email is not available"})
            else:
                user = User(name=name,
                            email=email,
                            password=password)
                user.save()

                access_token = create_access_token(identity=user.id)
                return Response.client_response(self, 201, True, {
                    "name": user.name,
                    "id": user.id,
                    "access_token": access_token
                })

        except Exception as e:
            return Response.client_response(self, 500, False, {"message": "the unexpected happened"})

    # class
