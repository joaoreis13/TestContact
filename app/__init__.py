from flask import Flask,request
from . import Endpoint,Core
import json, sys,os


sys.stdout = sys.stderr

application = Flask(__name__)
application.config.from_object('config')


#SET ENVIRONMENT VARIABLES
application.config['BLIP_KEY'] = os.getenv( 'BLIP_KEY',application.config['BLIP_KEY'] )

application.config['CUSTOM_USR'] = os.getenv('CUSTOM_USR',application.config['CUSTOM_USR'])

application.config['CUSTOM_MSG']= os.getenv('CUSTOM_MSG',application.config['CUSTOM_MSG'])

application.config['DEBUG']= os.getenv('DEBUG',False)


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