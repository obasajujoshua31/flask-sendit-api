from server.resources.users.user_controller import UserController
from server.resources.home import HomeController
from server.resources.users.login_controller import LoginController



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
    }
]


