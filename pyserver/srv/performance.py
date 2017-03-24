import json

import pandas as pd
from flask import jsonify, request
from flask_restful import Resource


class Performance(Resource):
    def post(self):
        # be more explicit...
        data = json.loads(request.data.decode("utf-8"))
        series = pd.read_json(data["series"], typ="series")
        return jsonify({"performance": series.describe().to_json()})
