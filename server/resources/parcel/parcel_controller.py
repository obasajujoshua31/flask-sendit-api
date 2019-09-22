from server.responses import Response
from flask_restful import Resource
from server.form import form_get, confirm_is_json
from flask_jwt_extended import (
        jwt_required
)


class ParcelController(Resource, Response):
    @jwt_required
    def get(self, parcel_id):
        from server.resources.parcel.parcel_model import Parcel
        parcel = Parcel.get_one_by_id(parcel_id)
        if parcel:
            return Response.client_response(self, 200, True, Response.parcel_response(self, parcel))
        else:
            return Response.client_response(self, 400, False, f"No Parcel found for parcel_id {parcel_id}")

    @jwt_required
    def put(self, parcel_id):
        if not confirm_is_json():
            return Response.client_response(self, 422, False, {"message": "please supply json"})
        destination = form_get("destination")
        if not destination:
            return Response.client_response(self, 400, False, {"message": "destination is empty"})
        from server.resources.parcel.parcel_model import Parcel

        parcel = Parcel.get_one_by_id(parcel_id)
        if not parcel:
            return Response.client_response(self, 400, False, f"No Parcel found for parcel_id {parcel_id}")
        else:
            parcel.update_parcel_destination(destination)
            return Response.client_response(self, 200, True, Response.parcel_response(self, parcel))

    @jwt_required
    def delete(self, parcel_id):
        from server.resources.parcel.parcel_model import Parcel
        parcel = Parcel.get_one_by_id(parcel_id)
        if not parcel:
            return Response.client_response(self, 400, False, f"No Parcel found for parcel_id {parcel_id}")
        else:
            parcel.cancel_parcel()
            return Response.client_response(self, 200, True, Response.parcel_response(self, parcel))

    # class
