import requests, json,uuid

def awnser(content):

    text = ''

    if (content['from'] == application.config['CUSTOM_USR'])
        text = application.config['CUSTOM_MSG']

    else

        blip.getUserInfo(content['from'])
        text ='Olá, bem vindo ao Test Bot. Isso é somente um exemplo de um bot em Python+Flask!'

    msg = {

        'id' = str(uuid.uuid4()),
        'to' = content['from'],
        'type' = 'text/plain',
        'content' = text
    }

    hdr{
        'Authorization':'key '+application.config['BLIP_KEY']
    }
    sent = requests.post(application.config['BLIP_URL'],json=msg,headers=hdr)