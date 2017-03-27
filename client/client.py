import json
import requests

import pandas as pd

# to make this work you have to start the server (via docker run -d -p "6220:8000" --name "RestServer" restserver)
if __name__ == '__main__':
    # some series
    x = pd.Series(index=[0, 1, 2], data=[5, 6, 7])
    response = requests.post(url="http://localhost:6220/performance", data=json.dumps({"series": x.to_json()}))
    print(pd.read_json(response.json()["performance"], typ="series"))
