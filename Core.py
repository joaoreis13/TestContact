from flask import current_app as app
import requests,json,uuid

"""
    Core.processMessage(content )

    Receive a json with the content of a request in the
    Blip API format.
"""
def processMessage(content):

    text = ''

    if content['from'] == app.config['CUSTOM_USR']:
        text = config['CUSTOM_MSG']

    else:

        #blip.getUserInfo(content['from'])
        text ='Olá, bem vindo ao Test Bot. Isso é somente um exemplo de um bot em Python+Flask!'

    msg = {

        'id' : str(uuid.uuid4()),
        'to' : content['from'],
        'type': 'text/plain',
        'content' : text
    }

    hdr = {
        'Authorization':'key '+ app.config['BLIP_KEY']
    }
    sent = requests.post(app.config['MSG_URL'],json=msg,headers=hdr)