from server.responses import Response
from flask_restful import Resource
from server.form import form_get, confirm_is_json
from flask_jwt_extended import (
        get_jwt_identity, jwt_required
)


class ParcelsController(Resource, Response):
    @jwt_required
    def get(self):
        from server.resources.parcel.parcel_model import Parcel
        parcels = Parcel.get_all()
        response = []
        if parcels:
            for parcel in parcels:
                response.append(Response.parcel_response(self, parcel))
            return Response.client_response(self, 200, True, response)
        else:
            return Response.client_response(self, 400, False, "No Parcels")

    @jwt_required
    def post(self):
        if not confirm_is_json():
            return Response.client_response(self, 422, False, {"message": "please supply json"})
        name = form_get("name")
        pick_up_location = form_get("pick_up_location")
        destination = form_get("destination")

        from server.resources.parcel.parcel_model import Parcel

        if not name:
            return Response.client_response(self, 400, False, {"message": "name is empty"})
        if not pick_up_location:
            return Response.client_response(self, 400, False, {"message": "pick_up_location is empty"})
        if not destination:
            return Response.client_response(self, 400, False, {"message": "destination is empty"})

        current_user = get_jwt_identity()
        try:
            parcel = Parcel(name=name,
                            destination=destination,
                            pick_up_location=pick_up_location,
                            placed_by=current_user)
            parcel.save()
            return Response.client_response(self, 201, True, Response.parcel_response(self, parcel))
        except Exception as e:
            return Response.client_response(self, 500, False, {"message": "the unexpected happened"})

    # class
