import json
from flask import jsonify

def handle(content):


    tResp = {}

    if content['type'] == 'text/plain' :

        tResp = {'id':content['id'],'status':'recieved'}

    else:
        tResp = {'status':'ok'}

    resp = jsonify(tResp)
    resp.status_code = 202
    return resp