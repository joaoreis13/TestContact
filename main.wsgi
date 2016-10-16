from flask import Flask,request
from Endpoint import *
import json
import sys

sys.stdout = sys.stderr

application = Flask(__name__)
application.config.from_object('config')

dbg = application.config['DEBUG']

if dbg:
    content = request.get_json()
    print("[INFO] Starting application outside main main method")

@application.route('/message', methods=['POST'])
def receive_msg():

    if dbg:
        content = request.get_json()
        print("[MSG] Recieved Request:"+json.dumps(content))

    return message.process(content)


@application.route('/notification')
def receive_not():

    if dbg:
        content = request.get_json()
        print("[NOT] Recieved Request:"+json.dumps(content))

    return notification.process(request.get_json())

if __name__ == '__main__':

    if dbg:
        content = request.get_json()
        print("[INFO] Starting application inside main method")
    application.run(debug=True)