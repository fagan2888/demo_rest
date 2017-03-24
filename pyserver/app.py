from flask import Flask
from flask_restful import Api

from pyserver.srv.performance import Performance
from pyserver.srv.hello import Hello

def app(config):
    app = Flask(__name__)

    app.config.from_object(config)

    for handler in app.config["HANDLER"]:
        app.logger.addHandler(handler)

    api = Api(app)

    api.add_resource(Hello, '/')
    api.add_resource(Performance, '/performance')
    return app
