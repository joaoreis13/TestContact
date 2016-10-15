import json
from flask import jsonify

def handle(content):

    tmpResponse = jsonify({'id':content['id'], 'status':'recieved'})
    tmpResponse.status_code = 202

    return tmpResponse