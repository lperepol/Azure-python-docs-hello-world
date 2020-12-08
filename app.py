from flask import Flask
import requests


app = Flask(__name__)

@app.route("/")
def hello():
    entity_name = "Person"
    username = "lperepolkin"
    password = "z4a*cGtajLkZxCFYb!5-32s=wp@bPbm"
    payload = {'username': username, 'password': password}
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Cache-Control': 'no-cache'}
    baseurl = "https://u4sm-accept01-skc.unit4cloud.com"
    url = baseurl + "/U4SMAPI/api/Authentication/Login"
    r = requests.post(url, headers=headers, data=payload)
    if r.status_code == 200:
        cookie = r.cookies
        pageSize = 97  # Prime number
        pageNumber = 1
        url = baseurl + '/u4smapi/api/' + entity_name + '/Get?config={"b":' + str(pageSize) + ',"c":' + str(
            pageNumber) + ',"e":1 }&criteria={"Info":{}}'
        r = requests.get(url, cookies=cookie)
        if r.status_code == 200:
            return r.text
    return "You're Screwed! to"
