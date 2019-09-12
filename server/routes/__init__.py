from server.resources.users.user_controller import UserController


routes = [{
    "URL": "/",
    "handler": UserController
}]


def application_routes(api):
    for route in routes:
        api.add_resource(route["handler"], route["URL"])