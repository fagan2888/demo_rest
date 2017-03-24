#!/usr/bin/env python

from waitress import serve
from pyserver.app import app
from config.restserver_settings import Config

if __name__ == '__main__':
    # It always run on port 8000 within the container.
    # You need to define the port the container will expose...
    serve(app=app(Config), port=8000)