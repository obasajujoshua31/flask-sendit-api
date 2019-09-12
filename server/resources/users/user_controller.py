from server.responses import Response
from flask_restful import Resource

class UserController(Resource, Response):
    def get(self):
        return Response.success_response(self, 200, True, {"success": "love"})