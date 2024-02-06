from flask import register_moduls
import routs

def load_routes(app):
    # Register the blueprint with the app
    app.register_blueprint(routes.main, url_prefix=f'{api_rout}/')
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
    



