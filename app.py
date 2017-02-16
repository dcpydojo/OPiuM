import requests
from flask import Flask, abort, jsonify
app = Flask(__name__)


@app.route("/")
def hello():
    resp = requests.get('https://www.opm.gov/json/operatingstatus.json?markup=on')
    if resp.status_code != 200:
        return abort(500)
    opm = resp.json()
    return opm['LongStatusMessage']


if __name__ == "__main__":
    app.run(
        debug=True
    )
