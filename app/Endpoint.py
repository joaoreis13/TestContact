import json
from flask import jsonify

def recieveMessage(content):

    tResp = {} #inicialize response to avoid error in jsonify


    if content['type'] == 'text/plain' :

        tResp = {'id':content['id'],'status':'recieved'}

    else:
        tResp = {'status':'ok'}

    resp = jsonify(tResp)
    resp.status_code = 202
    return resp

def recieveNotification(content):

    tResp = {'status':'ok'}

    resp = jsonify(tResp)
    resp.status_code = 202
    return resp