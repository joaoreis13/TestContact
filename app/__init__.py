from flask import Flask,request
from . import Endpoint,Core
import json, sys,os


sys.stdout = sys.stderr

application = Flask(__name__)
application.config.from_object('config')


#SET ENVIRONMENT VARIABLES
if os.environ.get('BLIP_KEY') != None:
    application.config['BLIP_KEY'] = os.environ['BLIP_KEY']

if os.environ.get('CUSTOM_USR') != None:
    application.config['CUSTOM_USR'] = os.environ['CUSTOM_USR']

if os.environ.get('CUSTOM_MSG') != None:
    application.config['CUSTOM_MSG']= os.environ['CUSTOM_MSG']

if os.environ.get('DEBUG') != None:
    application.config['DEBUG']= os.environ['DEBUG']


dbg = application.config['DEBUG']

if dbg:
    print("[INFO] Starting application outside main main method")

@application.route('/message', methods=['POST'])
def receive_msg():

    content = request.get_json()
    if dbg:
        print("[MSG] Recieved Request:"+json.dumps(content))

    Core.processMessage(content)
    return Endpoint.recieveMessage(content)


@application.route('/notification',methods=['POST'])
def receive_not():

    if dbg:
        content = request.get_json()
        print("[NOT] Recieved Request:"+json.dumps(content))

    return Endpoint.recieveNotification(request.get_json())

if __name__ == '__main__':

    if dbg:
        print("[INFO] Starting application inside main method")
    application.run(debug=True)