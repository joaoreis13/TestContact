from flask import Flask,request
from Endpoint import *
import json
import sys

sys.stdout = sys.stderr

application = Flask(__name__)
application.config.from_object('config')

msgUrl = application.config['MSG_URL']
key = application.config['BLIP_KEY']
notUrl = application.config['NOT_URL']
cmdUrl = application.config['CMD_URL']
dbg = application.config['DEBUG']


@application.route('/message', methods=['POST'])
def receive_msg():

    if dbg:
        content = request.get_json()
        print("[MSG] Recieved Request:"+json.dumps(content))

    return message.handle(content)


@application.route('/notification')
def receive_not():

    if dbg:
        content = request.get_json()
        print("[NOT] Recieved Request:"+json.dumps(content))

    return notification.handle(request.get_json())

if __name__ == '__main__':
    application.run(debug=True)