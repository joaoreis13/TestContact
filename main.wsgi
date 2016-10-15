from flask import Flask,request
from Endpoint import *
import json

application = Flask(__name__)
application.config.from_object('config')

msgUrl = application.config['MSG_URL']
key = application.config['BLIP_KEY']
notUrl = application.config['NOT_URL']
cmdUrl = application.config['CMD_URL']


@application.route('/message')
def receive_msg():

    return msg.handle(request.get_json())


@application.route('/notification')
def receive_not():

    return ntf.handle(request.get_json())