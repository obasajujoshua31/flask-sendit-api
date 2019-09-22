def install_routes(api, routes):
    for route in routes:
        api.add_resource(route["handler"], route["URL"])

def create_app(app_name, config_file, api, flask, app_config, routes, db, secret_key):
    app = flask(__name__,instance_relative_config=True)
    app.config.from_object(app_config[app_name])
    app.config.from_pyfile(config_file)
    app.config['JWT_SECRET_KEY'] = secret_key
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    endpoints = api(app)
    install_routes(endpoints, routes)
    import models
    db.init_app(app)
    return app
