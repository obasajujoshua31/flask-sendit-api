from server.responses import Response
from flask_restful import Resource

class HomeController(Resource, Response):
    def get(self):
        return Response.success_response(self, 200, True, {"message": "Welcome to SendIT Api V2"})