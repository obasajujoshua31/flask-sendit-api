from server.resources.users.user_controller import UserController
from server.resources.home import HomeController
from server.resources.users.login_controller import LoginController
from server.resources.parcel.parcels_controller import ParcelsController
from server.resources.parcel.parcel_controller import ParcelController



routes = [
    {
        "URL": "/users",
        "handler": UserController
    },
    {
        "URL": "/",
        "handler": HomeController
    },
    {
        "URL": "/users/login",
        "handler": LoginController
    },
    {
        "URL": "/parcels",
        "handler": ParcelsController
    },
    {
        "URL": "/parcels/<parcel_id>",
        "handler": ParcelController
    }
]


