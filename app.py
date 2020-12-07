from flask import Flask
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

@app.route("/")
def hello():
    user = 'MACHINE1'
    passwrd = '1%sdf^2Hfasd(&^HapPnY@?'
    url = "https://ubw.unit4cloud.com/ca_skc_prod_webapi/v1/objects/employees?companyId=sk&select=birthDate"
    r = requests.get(url, auth=HTTPBasicAuth(user, passwrd))
    if r.status_code == 200:
        #json_normalize(data['results'])
        return r.text
    return "You're Screwed!"
