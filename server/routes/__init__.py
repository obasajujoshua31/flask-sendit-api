from server.resources.users.user_controller import UserController
from server.resources.home import HomeController




routes = [
    {
        "URL": "/users",
        "handler": UserController
    },
    {
        "URL": "/",
        "handler": HomeController
    },
]


