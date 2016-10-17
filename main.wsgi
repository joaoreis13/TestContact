from flask import Flask,Request
import Endpoint,Core, json, sys


sys.stdout = sys.stderr

application = Flask(__name__)
application.config.from_object('config')

dbg = application.config['DEBUG']

if dbg:
    print("[INFO] Starting application outside main main method")

@application.route('/message', methods=['POST'])
def receive_msg():

    if dbg:
        content = request.get_json()
        print("[MSG] Recieved Request:"+json.dumps(content))

    Core.processMessage(content,application.config)
    return Endpoint.recieveMessage(content)


@application.route('/notification')
def receive_not():

    if dbg:
        content = request.get_json()
        print("[NOT] Recieved Request:"+json.dumps(content))

    return Endpoint.recieveNotification(request.get_json())

if __name__ == '__main__':

    if dbg:
        print("[INFO] Starting application inside main method")
    application.run(debug=True)