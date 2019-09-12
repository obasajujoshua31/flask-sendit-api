from server.responses import Response
from flask_restful import Resource
from server.form import form_get
#


class UserController(Resource, Response):
    def get(self):
        return Response.success_response(self, 200, True, {"success": "love"})

    def post(self):
        name = form_get("name")
        email = form_get("email")
        password = form_get("password")
        from server.resources.users.users_model import User

        user = User(name=name,
                    email=email,
                    password=password)
        user.save()
        return Response.success_response(self, 200, True, {
            "name": user.name,
            "password": user.password,
            "id": user.id,
            "email": user.email
        })
